import requests
import os

# ElevenLabs Text-to-Speech API Demo
# Demonstrates basic API integration for enterprise voice generation

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Default: Rachel

def generate_speech(text: str, output_file: str = "output.mp3") -> None:
    """
    Generate speech from text using ElevenLabs TTS API.
    Use case: automated voice responses for customer-facing workflows.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Audio saved to {output_file}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    sample_text = (
        "Welcome to our customer support line. "
        "How can I assist you today?"
    )
    generate_speech(sample_text)
