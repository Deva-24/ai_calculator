import openai

def interpret_query(query):
    response = openai.chat.Completion.create(
        model="gpt-4",  # or another model like "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": query}
        ]
    )
    return response['choices'][0]['message']['content']
