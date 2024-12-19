# SAMMY Actuator API

A FastAPI-based actuator service that enables SAMMY extension automation and screen capture.

## Prerequisites

- Python 3.12
- Poetry (Python package manager)
- Chrome/Arc browser for extension support

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
   poetry install
   ```

## Running the API

### Development Mode

```bash
poetry run uvicorn actuator.app:app --port 8001 --reload
```

### Production Mode

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
