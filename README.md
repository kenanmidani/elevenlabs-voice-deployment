# ElevenLabs Voice Deployment

Exploring the ElevenLabs API for enterprise voice and agent deployment use cases,
with a focus on GCC industry verticals including energy, utilities, and government services.

## Scripts

### `speech_generation.py`
Calls the ElevenLabs TTS API to generate human-like voice output from text.
Applicable to automated customer communications, IVR systems, and multilingual support workflows.

### `voice_agent_demo.py`
Demonstrates creation and configuration of a conversational AI agent via the ElevenAgents API.
Covers agent setup, system prompt design, and deployment readiness validation —
mirroring the workflow for deploying voice agents in enterprise customer-facing operations.

## Setup

```bash
pip install requests
export ELEVENLABS_API_KEY=your_api_key_here
python speech_generation.py
python voice_agent_demo.py
```

## Context
Built as part of exploring enterprise AI deployment patterns in the Middle East market,
where voice-enabled agent workflows are increasingly relevant for energy, telecom,
and public sector digital transformation initiatives.
