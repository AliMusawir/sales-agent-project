# Sales Agent using Google ADK

## Project Overview
This project implements a conversational Sales Agent using Google's Agent Development Kit (ADK) in Python.

The agent:
- Activates when a new lead sends a message, simulating a form submission.
- Asks for consent before collecting any information.
- Collects specific information through a step-by-step flow:
  - Age
  - Country
  - Interested Product or Service
- Handles multiple lead interactions concurrently by managing separate sessions using session IDs.
- Saves all collected information into a CSV file (`leads.csv`).
- Sends a follow-up message if a lead does not respond within 10 seconds, simulating a 24-hour delay.

## Project Structure

```
sales-agent/
├── adk-env/                  # Virtual environment
├── agent.py                  # SalesAgent class logic
├── utils.py                  # Helper function to update leads.csv
├── simulate_leads.py          # Script to automatically simulate lead interaction
├── interactive_test.py        # Script to manually interact with the agent
├── leads.csv                  # Output file where leads are saved
├── README.md                  # Project documentation
```

## Setup Instructions

1. Clone or download the project files.
2. Create a virtual environment:
   ```
   python -m venv adk-env
   ```
3. Activate the virtual environment:
   ```
   adk-env\Scripts\activate
   ```
4. Install required dependencies:
   ```
   pip install google-adk
   pip install aioconsole
   ```

## How It Works

- External Trigger:  
  The agent is activated when a lead sends a message, simulating a form submission.

- Conversational Flow:  
  1. The agent greets the user and asks for consent.
  2. If the user agrees, the agent collects information step-by-step.
  3. The collected data is saved in the `leads.csv` file.

- Multi-Session Handling:  
  Each conversation session is handled independently using a unique session ID.

- Follow-Up Handling:  
  If the user does not respond within 10 seconds after a question, the agent sends an automatic follow-up reminder.

## How to Test

### Simulate Leads Automatically
Run the simulation script:
```
python simulate_leads.py
```
This script automatically interacts with the agent to simulate lead form filling.

### Manually Interact with the Agent
Run the manual testing script:
```
python interactive_test.py
```
Type your responses manually. If you do not respond to a question within 10 seconds, the agent will automatically send a follow-up message.

## Leads Data Example

After the interaction, the `leads.csv` file will store lead data in the following format:

| lead_id | age | country | interest | status |
|---------|-----|---------|----------|--------|
| manual_lead | 25 | Pakistan | Nike Shoes | secured |

## Requirements Fulfilled

| Task Requirement | Status |
|-------------------|--------|
| Use Google ADK in Python | Completed |
| Handle multiple lead interactions concurrently | Completed |
| Collect specific information step-by-step | Completed |
| Activate agent through an external trigger | Completed |
| Save collected information into a CSV file | Completed |
| Follow up with leads who do not respond | Completed |
| Manual and simulation-based testing | Completed |

## Conclusion

This project successfully implements a fully functional conversational sales agent that interacts with leads, collects necessary information, saves the data securely, and manages follow-up messaging in case of inactivity, all built using Google's Agent Development Kit in Python.
