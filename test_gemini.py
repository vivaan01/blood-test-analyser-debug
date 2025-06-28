import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

response = gemini.invoke("Hello! Can you summarize what you are?")
print("Gemini Response:", response) 