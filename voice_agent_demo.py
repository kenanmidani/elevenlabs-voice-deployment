import requests
import os

# ElevenLabs Conversational Agent Demo
# Demonstrates ElevenAgents API setup for enterprise customer workflows

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def create_agent(agent_name: str, system_prompt: str) -> dict:
    """
    Create a conversational voice agent via ElevenLabs API.
    Use case: deploying AI agents for customer-facing operations
    in enterprise environments (e.g. banking, telecoms, utilities).
    """
    url = "https://api.elevenlabs.io/v1/convai/agents/create"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "name": agent_name,
        "conversation_config": {
            "agent": {
                "prompt": {
                    "prompt": system_prompt
                },
                "first_message": "Hello, how can I help you today?",
                "language": "en"
            },
            "tts": {
                "voice_id": "21m00Tcm4TlvDq8ikWAM"
            }
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        agent = response.json()
        print(f"Agent created: {agent['agent_id']}")
        return agent
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return {}


def get_agent_details(agent_id: str) -> dict:
    """
    Retrieve configuration and status of a deployed agent.
    Use case: monitoring and validating agent deployment readiness.
    """
    url = f"https://api.elevenlabs.io/v1/convai/agents/{agent_id}"

    headers = {"xi-api-key": ELEVENLABS_API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return {}


if __name__ == "__main__":
    system_prompt = (
        "You are a helpful customer support agent for an energy company. "
        "You assist customers with billing inquiries, outage reports, "
        "and service requests. Be concise and professional."
    )

    agent = create_agent(
        agent_name="Energy-Customer-Support-Demo",
        system_prompt=system_prompt
    )

    if agent:
        details = get_agent_details(agent["agent_id"])
        print(f"Agent status: {details}")
