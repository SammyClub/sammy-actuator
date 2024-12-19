# SAMMY Actuator API

SAMMY is an AI-powered automation platform that guides users like a human would, helping teams focus on what really matters. This is the FastAPI-based actuator service enables intelligent GUI automation and screen capture for Supabase, automating tasks that might be difficult or impossible via traditional methods.

🎥 [Watch the Quick Start Guide](https://www.loom.com/share/237a4e57a01c4eb2a175b6cef81763d6?sid=621d29ca-777e-411c-b8f8-d44e51e02460)

## Prerequisites

- Python 3.12
- Poetry (Python package manager)
- Chrome/Arc browser for extension support
- A Google account (for OAuth login)
- Access to Supabase

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/SammyClub/sammy-actuator
   cd sammy-actuator
   ```

2. **Install Poetry** (if not already installed)

   ```bash
   # On Unix/macOS/WSL
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies**
   ```bash
   poetry env use 3.12
   poetry install
   ```

## macOS Permissions Setup

⚠️ Important: On macOS, you must enable several permissions for the extension to work properly. If permissions aren't granted, actions will silently fail.

### 1. Input Monitoring

Enable under: Settings → Privacy & Security → Input Monitoring → Allow [Your IDE/Terminal]

![Enabling input monitoring](./assets/image-3.png)

### 2. Screen Recording

Enable under: Settings → Privacy & Security → Screen Recording → Allow [Your IDE/Terminal]

![Enabling screen recording](./assets/image-2.png)

### 3. Accessibility Access

Enable under: Settings → Privacy & Security → Accessibility → Allow [Your IDE/Terminal]

![Enabling replay of actions](./assets/image.png)

## Starting the API Server

1. **Development Mode**

   ```bash
   poetry run uvicorn actuator.app:app --port 8001 --reload
   ```

2. **Production Mode**
   ```bash
   poetry run gunicorn actuator.app:app -c gunicorn.conf.py
   ```

## Browser Extension Setup

1. Open your browser's extensions page:

   - Chrome: Navigate to `chrome://extensions`
   - Arc: Navigate to `arc://extensions`

2. Enable "Developer mode" (toggle in the top-right corner)

3. Click "Load unpacked"

4. Navigate to and select the `supabase-extension` folder in this repository

## Using SAMMY with Supabase

0. Log into the SAMMY extension

1. After installing the extension, navigate to [Supabase Dashboard](https://supabase.com/dashboard/)

2. Look for the SAMMY AI icon in the top-right corner

3. Click the icon and log in with Google OAuth

4. You'll see:
   - The SAMMY AI logo in the header
   - "My Macros" in the top right
   - "Top Community Macros"
   - A search bar for finding macros

## Features

- **Search Macros**: Use the search bar to find macros using similarity search
- **Create Macros**: Create new automation macros that will be processed in the background
- **Community Macros**: Access and use macros created by the community
- **Feedback System**: Provide feedback on macro execution for continuous improvement
