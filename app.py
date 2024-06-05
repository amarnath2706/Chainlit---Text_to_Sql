import os
from openai import AsyncOpenAI  
from chainlit.playground.providers.openai import ChatOpenAI
from dotenv import load_dotenv
print("ok")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client=AsyncOpenAI(api_key=OPENAI_API_KEY)
print("client created")