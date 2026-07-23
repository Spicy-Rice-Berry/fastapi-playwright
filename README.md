# FastAPI Playwright Project

This project demonstrates how to use FastAPI and Playwright together. The Playwright script launches a browser, navigates to Google, searches for "strawberry", and saves a screenshot of the search results.

## Requirements

- Python 3.10+
- Git
- Playwright
- FastAPI
- Uvicorn

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Spicy-Rice-Berry/fastapi-playwright.git
cd fastapi-playwright
```

### 2. Checkout the Developer Branch

```bash
git checkout developer
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Playwright Browsers

```bash
playwright install
```

## Running the FastAPI Application

Start the FastAPI development server:

```bash
uvicorn app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

### API Documentation

FastAPI automatically generates API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Running the Playwright Script

Execute:

```bash
python3 playwright_script.py
```

## Playwright Example

The Playwright script:

1. Opens Google in Chromium.
2. Searches for "strawberry".
3. Waits for the search results page to load.
4. Saves a screenshot to the `output/` directory.

## Output

Generated screenshots are saved to:

```text
output/
```

Example:

```text
output/strawberry_results.png
```

## Project Structure

```text
fastapi-playwright/
├── app.py
├── playwright_script.py
├── requirements.txt
├── README.md
├── .gitignore
├── output/
└── venv/
```

## Ignored Files

The following directories are excluded from source control:

- `venv/` (Python virtual environment)
- `output/` (generated screenshots and test artifacts)
- `__pycache__/`

## Git Workflow

Check status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Describe your changes"
```

Push changes:

```bash
git push origin developer
```

## Notes

- The `venv/` directory should not be committed to GitHub.
- The `output/` directory contains generated files and is ignored through `.gitignore`.
- Playwright requires browser binaries installed through `playwright install`.
