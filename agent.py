from google.adk.agents import Agent
from google.adk.sessions import Session
from utils import update_csv
from pydantic import PrivateAttr
import asyncio

QUESTIONS = [
    "What is your age?",
    "Which country are you from?",
    "What product or service are you interested in?"
]

class SalesAgent(Agent):
    _context: dict = PrivateAttr(default_factory=dict)

    def __init__(self):
        super().__init__(name="sales_agent")

    async def handle_message(self, session: Session, message):
        lead_id = session.session_id
        text = message.text.strip().lower()

        # Cancel any existing follow-up timer when user responds
        if lead_id in self._context and self._context[lead_id].get("followup_task"):
            self._context[lead_id]["followup_task"].cancel()
            self._context[lead_id]["followup_task"] = None

        if lead_id not in self._context:
            self._context[lead_id] = {"step": 0, "responses": {}, "followup_task": None}
            await session.send_text("Hey! Thank you for filling out the form. I'd like to gather some information from you. Is that okay?")
            # Start follow-up timer
            self._context[lead_id]["followup_task"] = asyncio.create_task(self.start_followup(session))
            return

        step = self._context[lead_id]["step"]

        if step == 0:
            if "yes" in text:
                self._context[lead_id]["step"] += 1
                await session.send_text(QUESTIONS[0])
                # Start follow-up timer
                self._context[lead_id]["followup_task"] = asyncio.create_task(self.start_followup(session))
            else:
                await session.send_text("Alright, no problem. Have a great day!")
                update_csv(lead_id, {}, "no_response")
                del self._context[lead_id]
        else:
            q_index = step - 1
            self._context[lead_id]["responses"][q_index] = message.text.strip()
            if step < len(QUESTIONS):
                self._context[lead_id]["step"] += 1
                await session.send_text(QUESTIONS[q_index + 1])
                # Start follow-up timer again after asking next question
                self._context[lead_id]["followup_task"] = asyncio.create_task(self.start_followup(session))
            else:
                responses = self._context[lead_id]["responses"]
                age, country, interest = responses[0], responses[1], responses[2]
                update_csv(lead_id, {"age": age, "country": country, "interest": interest}, "secured")
                await session.send_text("Thank you! Your information has been recorded.")
                del self._context[lead_id]

    async def start_followup(self, session: Session):
        try:
            await asyncio.sleep(10)  # ⏰ Wait for 10 seconds
            await session.send_text("Just checking in to see if you're still interested. Let me know when you're ready to continue.")
        except asyncio.CancelledError:
            # Timer was cancelled because the user replied
            pass
