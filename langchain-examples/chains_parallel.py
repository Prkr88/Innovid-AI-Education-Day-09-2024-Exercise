from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_openai import ChatOpenAI
from pydantic import Field, BaseModel
import json
from pydantic.v1 import validator

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert travel advisor."),
        ("human", "List the key attractions of the vacation destination {destination_name}."),
    ]
)


# Define pros analysis step
def analyze_pros(attractions):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert travel advisor. "),
            (
                "human",
                "Given these attractions: {attractions}, list the advantages of visiting this destination.",
            ),
        ]
    )
    return pros_template.format_prompt(attractions=attractions)


# Define cons analysis step
def analyze_cons(attractions):
    cons_template = ChatPromptTemplate.from_messages(
        messages=[
            ("system", "You are an expert travel advisor."),
            (
                "human",
                "Given these attractions: {attractions}, list the disadvantages of visiting this destination.",
            ),
        ]
    )
    return cons_template.format_prompt(attractions=attractions)


# Define a custom output parser that returns a ProsConsOutputParser class
class ProsConsOutputParser(BaseModel):
    pros: str = Field(description="The advantages of visiting the destination.")
    cons: str = Field(description="The disadvantages of visiting the destination.")

    @validator("pros")
    def not_empty(cls, pros):
        if not pros:
            raise ValueError("Pros cannot be empty.")
        return pros


pros_cons_output_parser = PydanticOutputParser(pydantic_object=ProsConsOutputParser)

# Simplify branches with LCEL
pros_branch_chain = (
        RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser()
)

cons_branch_chain = (
        RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser()
)


def combine_pros_cons(pros, cons):
    # Combine pros and cons into a JSON string
    return json.dumps({"pros": pros, "cons": cons})


# Create the combined chain using LangChain Expression Language (LCEL)
chain = (
        prompt_template
        | model
        | StrOutputParser()
        | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain})
        | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
        | pros_cons_output_parser
)

# Run the chain
result = chain.invoke({"destination_name": "Hawaii"})

# Output
print(result)
print("Type of result:", type(result))
