from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import AzureChatOpenAI
import os

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = AzureChatOpenAI(openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                        deployment_name=os.getenv("CHAT_MODEL"),
                        openai_api_version=os.getenv("OPENAI_API_VERSION")
                        )

print("\n----- Prompt with System and Human Messages (Tuple) -----\n")

# Define prompt templates
messages = [
    ("system", "You are an assistant for debugging and fixing code."),
    ("human", "This is the {code}, this is the error {error}, how to fix the code?"),
]

# Create a prompt template from messages
prompt_template = ChatPromptTemplate.from_messages(messages)

# Invoke the prompt template with the provided context
prompt = prompt_template.invoke({"code": "print(‘Hello World)", "error": "Missing closing quote [']"})

# Invoke the model with the prompt
result = model.invoke(prompt)

print(result.content)
