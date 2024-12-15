import onnxruntime as ort
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the model path to your ONNX model file
MODEL_PATH = os.getenv("MODEL_PATH", "model.onnx")

#OS
if not os.path.isfile(MODEL_PATH):
    print(f"Error: Model file '{MODEL_PATH}' does not exist.")
    exit(1)


# Function to load the model using onnxruntime
def load_model(model_path):
    try:
        # Create a session to run the model
        session = ort.InferenceSession(model_path)
        return session
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")

# Function to interpret the query using the loaded model
def interpret_query(query):
    """ Use the ONNX model to interpret user queries. """
    try:
        # Load the ONNX model (this is done once and cached for performance)
        session = load_model(MODEL_PATH)
        
        # Prepare input data (assuming the model expects a text input in a certain format)
        input_data = {"input_text": query}  # Modify this according to your model's input format
        
        # Prepare input name and data for the model (adjust for your model's input names and types)
        input_name = session.get_inputs()[0].name
        input_array = np.array([input_data["input_text"]], dtype=np.str_)  # Adjust input format if needed
        
        # Run the model
        outputs = session.run(None, {input_name: input_array})
        
        # Process and return the output (assuming it's a text-based output)
        output_text = outputs[0][0]
        return output_text
    except Exception as e:
        return f"Error: {e}"
