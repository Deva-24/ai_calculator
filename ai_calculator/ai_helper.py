# ai_helper.py

import spacy

# Load the spaCy model for English language processing
nlp = spacy.load("en_core_web_sm")

# Define the function to interpret the query
def interpret_query(query):
    # Process the user query
    doc = nlp(query.lower())
    
    # Extract numbers and operations from the query
    numbers = [float(token.text) for token in doc if token.pos_ == 'NUM']
    
    # If less than two numbers are found, return an error
    if len(numbers) < 2:
        return "Error: Could not find two numbers for operation."

    # Perform operations based on the user's query
    if "add" in query:
        return numbers[0] + numbers[1]
    elif "subtract" in query:
        return numbers[0] - numbers[1]
    elif "multiply" in query:
        return numbers[0] * numbers[1]
    elif "divide" in query:
        if numbers[1] == 0:
            return "Error: Division by zero."
        return numbers[0] / numbers[1]
    elif "power" in query:
        return numbers[0] ** numbers[1]
    elif "root" in query:
        if numbers[0] < 0:
            return "Error: Cannot compute the root of a negative number."
        return numbers[0] ** (1/numbers[1])
    else:
        return "Error: Unknown operation."
