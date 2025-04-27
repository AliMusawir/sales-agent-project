# simulate_leads.py
import asyncio
from agent import SalesAgent

class DummySession:
    def __init__(self, session_id):
        self.session_id = session_id

    async def send_text(self, text):
        print(f">> Agent: {text}")

async def simulate():
    agent = SalesAgent()
    session = DummySession("lead123")

    async def send(msg):
        print(f">> User: {msg}")
        await agent.handle_message(session, DummyMessage(msg))

    await send("Hi")           # triggers greeting
    await send("yes")          # consent
    await send("25")           # age
    await send("Pakistan")     # country
    await send("Cloud Storage") # interest

class DummyMessage:
    def __init__(self, text):
        self.text = text

asyncio.run(simulate())
