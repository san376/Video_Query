from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",  # this usually always exists
    temperature=0.2
)

print(llm.invoke("Say hello").content)
