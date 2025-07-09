# AI Desktop Assistant Alpha 

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Technical Details](#technical-details)
7. [Limitations](#limitations)
8. [Future Improvements](#future-improvements)

---

## Overview
AI Desktop Assistant Alpha is a voice-controlled personal assistant that can perform various tasks including web searches, media control, application launching, and general conversation using AI. It features wake word detection and combines offline and online speech recognition with OpenAI's GPT-3.5 for intelligent responses.

## Features

### Core Capabilities
- **Wake Word Detection**: Listens continuously for "Alpha" to activate
- Voice-controlled interaction
- Dual speech recognition (Google and offline Vosk model)
- AI-powered conversation (OpenAI GPT-3.5)
- Text-to-speech feedback

### Command Functions
- **Web Browsing**:
  - Open websites ("open facebook")
  - Google searches ("search for python tutorials")
- **Media Control**:
  - YouTube video playback ("play Bohemian Rhapsody on youtube")
  - Playback control (pause/resume/mute/volume/skip)
  - Playback speed adjustment
- **System Control**:
  - Launch applications ("open spotify")
- **Conversation**:
  - General knowledge questions
  - Casual conversation
- **Control**:
  - Pause/resume listening ("stop"/"listen")
  - Exit program ("exit")

## Installation

### Prerequisites
- Python 3.8+
- Chrome browser (for YouTube functionality)
- Porcupine wake word engine

### Steps
1. Clone the repository or download the script
2. Install required packages:
   ```bash
   pip install pyttsx3 speechrecognition vosk selenium openai pvporcupine pyaudio
   ```
3. Download Vosk model:
   - Download `vosk-model-small-en-us-0.15` from [Vosk models](https://alphacephei.com/vosk/models)
   - Extract to `./models/vosk-model-small-en-us-0.15` in the project directory
4. Set up OpenAI API:
   - Get an API key from [OpenAI](https://platform.openai.com/)
   - Replace the placeholder in the script with your actual key
5. Set up wake word detection:
   - Get a Porcupine access key from [Picovoice Console](https://console.picovoice.ai/)
   - Place the wake word model file (`wake_up_alpha.ppn`) in the project directory

## Usage

### Starting the Assistant
1. Run the wake word listener:
   ```bash
   python wakeup_listener.py
   ```
2. Say "Alpha" to activate the assistant
3. The main assistant will launch and greet you

### During Operation
1. Speak commands naturally after the "Listening..." prompt appears
2. Use "stop" to pause listening and "listen" to resume
3. Use "exit" to quit the program

### Example Commands
- "Alpha" (wake word)
- "Open youtube"
- "Search for best python frameworks"
- "Play Hotel California on youtube"
- "Pause video"
- "Volume to 50"
- "Skip 30 seconds"
- "Speed to 1.5x"
- "What's the weather today?"
- "Tell me a joke"
- "Stop" (pauses listening)
- "Exit" (quits program)

## Configuration

### Key Configuration Points
1. **OpenAI API Key**:
   - Replace `"sk-proj-..."` with your actual OpenAI API key
   - Consider using environment variables for security

2. **Porcupine Access Key**:
   - Replace the access key in `wakeup_listener.py`

3. **Application Paths**:
   - Modify the Spotify path if needed in `main.py`
   - Update `ASSISTANT_COMMAND` in `wakeup_listener.py` to point to your installation

4. **Wake Word Model**:
   - Ensure `wake_up_alpha.ppn` is in the correct location

## Technical Details

### Architecture
1. **Wake Word Detection**:
   - Porcupine engine continuously listens for "Alpha"
   - Launches main assistant when detected
2. **Voice Input**:
   - Primary: Google Speech Recognition (online)
   - Fallback: Vosk (offline)
3. **Command Processing**:
   - Pattern matching for specific commands
   - OpenAI GPT-3.5 for general conversation
4. **Output**:
   - pyttsx3 for text-to-speech
   - Console logging for debugging

### Key Components
- `wakeup_listener.py`: Handles wake word detection
- `speak()`: Handles text-to-speech output
- `take_command()`: Manages voice input
- `get_chat_response()`: Interfaces with OpenAI API
- Selenium WebDriver: Controls YouTube playback

## Limitations
1. Requires internet connection for Google recognition and OpenAI
2. YouTube controls require Chrome browser
3. Limited to English language
4. Spotify path is hardcoded for Windows
5. Basic error handling
6. Requires Porcupine access key for wake word functionality

## Future Improvements
1. Add more application integrations
2. Implement custom wake word training
3. Add system monitoring capabilities
4. Improve error handling and robustness
5. Add configuration file support
6. Implement plugin architecture for extensibility
7. Add multi-language support
8. Implement proper API key management
9. Add background process management

---

# Updated README.md

```markdown
# AI Desktop Assistant Alpha

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A voice-controlled personal assistant with wake word detection, web browsing, media control, and AI conversation capabilities.

## Features

- Wake word detection ("Alpha")
- Voice commands for web browsing and media control
- YouTube video playback with full control (play/pause/volume/skip)
- OpenAI-powered conversations
- Both online (Google) and offline (Vosk) speech recognition
- Text-to-speech feedback

## Quick Start

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Download and set up:
   - Vosk model in `./models/vosk-model-small-en-us-0.15`
   - Porcupine wake word model (`wake_up_alpha.ppn`)
   - Add your OpenAI and Porcupine API keys

3. Run the wake word listener:
   ```bash
   python wakeup_listener.py
   ```

4. Say "Alpha" to activate the assistant

## Basic Commands

| Command | Action |
|---------|--------|
| "Alpha" | Wake word to activate assistant |
| "Open [website]" | Opens the specified website |
| "Search for [query]" | Performs a Google search |
| "Play [song] on youtube" | Plays YouTube video |
| "Pause video" / "Resume video" | Controls playback |
| "Volume to 50" | Adjusts volume |
| "Skip 30 seconds" | Seeks in video |
| "Speed to 1.5x" | Changes playback speed |
| "Stop" / "Listen" | Pauses/resumes listening |
| "Exit" | Quits the program |

## Requirements

- Python 3.8+
- Chrome browser
- Microphone
- OpenAI API key
- Porcupine access key
