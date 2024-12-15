import groqflow
import os
from dotenv import load_dotenv

load_dotenv()

# Assuming the model has been compiled and is stored locally as `calculator_model.groq`
MODEL_PATH = "path_to_your_groq_optimized_model.groq"

# Groq model runner initialization
model_runner = groqflow.ONNXRunner(MODEL_PATH)

def interpret_query(query):
    """ Use Groq-powered AI to interpret user queries. """
    try:
        input_data = {"input_text": query}  # Prepare the input for the Groq-optimized model
        response = model_runner(input_data)  # Run the model on Groq hardware
        return response["output_text"]      # Process and return the result
    except Exception as e:
        return f"Error: {e}"
