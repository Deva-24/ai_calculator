import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def interpret_query(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Interpret this query for a calculator: {query}",
        max_tokens=100
    )
    return response.choices[0].text.strip()
