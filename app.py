import os
from openai import AsyncOpenAI  
from chainlit.playground.providers.openai import ChatOpenAI

print("ok")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client=AsyncOpenAI(OPENAI_API_KEY)
print("client created")