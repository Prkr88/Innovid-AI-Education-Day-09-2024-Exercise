from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI  # Update the import to use the new package

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4")

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=model, memory=memory, verbose=True)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    llm_response = conversation.predict(input=query)

    print(f"AI: {llm_response}")
