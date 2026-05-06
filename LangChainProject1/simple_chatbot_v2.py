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

#create chat history 
chat_history = []

print("Chat assistant ready! Type bye or exit to stop \n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["bye", "exit"]:
        print("Assistant: Goodbye!")
        break

    messages = chat_history + [{"role": "user", "content": user_input}]
    result = agent.invoke({"messages": messages})
    
    try:
        reply = result['messages'][-1].content
    except  Exception as e:
        print("Error processing response:", e)
        reply = str(e)

    print(f'Assistant: {reply} \n')
    print('-' * 60)

    #update chat history 
    chat_history.append({"role": "user", "content":user_input})
    chat_history.append({"role": "assistant", "content": reply})
    
# result = agent.invoke(
#     {
#         "messages": [{"role": "user", "content": "Explain machine learning in short"}]
#     }
# )

#print(result)

print(result['messages'][1].content)