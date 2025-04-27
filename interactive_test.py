import asyncio
import aioconsole
from agent import SalesAgent

class ConsoleSession:
    def __init__(self, session_id):
        self.session_id = session_id

    async def send_text(self, text):
        print(f"Agent: {text}")

class Message:
    def __init__(self, text):
        self.text = text

async def chat():
    agent = SalesAgent()
    session = ConsoleSession("manual_lead")

    print("🧠 Sales Agent is ready. Start chatting (type 'exit' to quit):")

    while True:
        user_input = await aioconsole.ainput("You: ")  # 🔥 Non-blocking input
        if user_input.lower() == "exit":
            break
        await agent.handle_message(session, Message(user_input))

asyncio.run(chat())
