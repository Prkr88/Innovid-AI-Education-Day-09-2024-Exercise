from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import find_dotenv, load_dotenv
from langchain_community.chat_models import AzureChatOpenAI
import os

# Load environment variables from a .env file
load_dotenv(find_dotenv())

def generate_poem(subject):
    # Initialize the OpenAI LLM with the API key loaded from the environment
    llm = AzureChatOpenAI(openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                 azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                 deployment_name=os.getenv("CHAT_MODEL"),
                 openai_api_version=os.getenv("OPENAI_API_VERSION")
                 )

    # Define the prompt template that will be used to generate the story
    template = """
    You are a funny poet. Please create a humorous poem based on the following scenario.
    Ensure it’s lighthearted, with a playful twist. The poem should be more than 20 words but fewer than 50 words.
    
    CONTEXT: {subject}
    STORY:
    """
    # Create a PromptTemplate object with the template and input variables
    prompt = PromptTemplate(template=template, input_variables=["subject"])
    # Create the LLMChain with the prompt and the AzureOpenAI model
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain with the scenario to generate a story
    story = chain.run(subject)


    print(story)
    return story

if __name__ == "__main__":
    generate_poem("the tastiest ice-cream ever!")