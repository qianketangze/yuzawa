import os
import google.generativeai as genai
from dotenv import load_dotenv

def summarize_text(text):
    """
    Summarizes the given text using the Gemini API.

    Args:
        text: The text to be summarized.

    Returns:
        The summarized text, or an error message if summarization fails.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY not found in .env file."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        # Prepare the prompt for summarization
        prompt = f"以下の記事を日本語で3文程度に要約してください:\n\n{text}"

        response = model.generate_content(prompt)

        return response.text
    except Exception as e:
        return f"Error during summarization: {e}"
