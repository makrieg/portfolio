import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

agent = create_agent(
    model=model,
    tools=[],
    system_prompt="You are a helpful chat assistant. Be clear, consise, and polite. " \
    "Understand the user's intent and respond directly. Stay professional and safe."
    )
result = agent.invoke(
    {
        "messages": [{"role": "user", "content": "Explain machine learning in short"}]
    }
)

#print(result)

print(result['messages'][1].content)