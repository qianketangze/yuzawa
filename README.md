# RSS Summarizer with Gemini

This project is a Python application that fetches the latest articles from various tech news RSS feeds and uses the Google Gemini API to generate concise summaries.

## Features

- Fetches articles from Google Research Blog, TechCrunch, and OpenAI News.
- Extracts the main content from the RSS feed entries.
- Uses the Gemini API to summarize the article text.
- Displays the article title, link, and its summary in the console.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    - Rename the `.env.example` file to `.env`.
    - Open the `.env` file and replace `"YOUR_API_KEY_HERE"` with your actual Google Gemini API key.
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## Usage

To run the application, execute the `main.py` script from the project's root directory:

```bash
python src/main.py
```

The application will then fetch the latest articles from the specified RSS feeds, summarize them, and print the results to your console.
