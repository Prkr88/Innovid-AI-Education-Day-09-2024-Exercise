from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic


# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# ---- LangChain OpenAI Chat Model Example ----

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o")

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from OpenAI: {result.content}")

# Create a Anthropic model
model = ChatAnthropic(model="claude-3-opus-20240229")

result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")


# Google Chat Model Example
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result = model.invoke(messages)
print(f"Answer from Google: {result.content}")
