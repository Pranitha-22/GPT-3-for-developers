import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt, model="gpt-3.5-turbo", temperature=0.5, max_tokens=1000):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print("GPT API Error:\n")
        print(e)
        return "Error calling GPT."


