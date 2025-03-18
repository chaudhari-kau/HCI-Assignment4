import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Hugging Face API token from the environment variable
hf_token = os.getenv('HF_TOKEN')
if hf_token is None:
    raise ValueError("Hugging Face API token not found. Please set HF_TOKEN in your .env file.")

# Define the Hugging Face Inference API endpoint for the GPT-2 model.
API_URL = "https://api-inference.huggingface.co/models/gpt2"

# Set up the headers using the API token
headers = {
    "Authorization": f"Bearer {hf_token}"
}

def query(payload):
    """
    Sends a POST request to the Hugging Face API with the given payload.
    
    Args:
        payload (dict): Data to be sent in the request body.
        
    Returns:
        dict or list: The JSON response from the API.
    """
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def main():
    # Create a creative "Hello World" prompt.
    prompt = "Hello World! Today is a fantastic day to explore the wonders of AI. Let the creativity begin: "
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 50, "temperature": 0.7},
        "options": {"wait_for_model": True}
    }
    
    # Query the API and get the generated text.
    result = query(payload)
    
    # Check if the response is in the expected format.
    if isinstance(result, list) and result and "generated_text" in result[0]:
        generated_text = result[0]["generated_text"]
        print("Generated 'Hello World' message:")
        print(generated_text)
    else:
        print("Unexpected response format:")
        print(result)

if __name__ == "__main__":
    main()
