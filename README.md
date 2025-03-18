# Hello World Generative AI Application 🚀✨

## Overview
This project demonstrates a basic integration with the [Hugging Face Inference API](https://huggingface.co/inference-api) to generate a creative **"Hello World"** message using the GPT-2 model. The application sends a prompt to the API and displays the generated text output, showcasing a simple yet effective use of a generative AI API. This serves as an introduction to working with AI APIs and handling environment variables securely.

## Objectives 🎯
- **Gain Familiarity with APIs:** Learn how to integrate and interact with external APIs, understand request/response patterns, and handle API authentication.
- **Application Development:** Develop a Python application that calls a generative AI API, process the responses, and implement proper error handling.
- **Creative Output:** Generate a creative "Hello World" message using state-of-the-art language models.
- **Security Best Practices:** Learn how to securely manage API tokens and sensitive credentials.
- **Documentation & Reflection:** Document the process and reflect on the learning experience.

## API Selection 🔍
For this project, we selected the [Hugging Face Inference API](https://huggingface.co/inference-api) with the GPT-2 model for several reasons:
- **Accessibility:** Provides straightforward access to powerful language models
- **Ease of Use:** Simple API structure with comprehensive documentation
- **Capabilities:** Generates creative and contextually relevant text completions
- **Free Tier:** Offers a generous free tier for learning and experimentation

An API token is required to access the service. In this demo, the token is securely loaded from a `.env` file, which is excluded from version control to maintain security.

## Setup and Installation ⚙️

### Prerequisites
- **Python 3.6+:** Ensure you have Python 3.6 or newer installed.
- **Required Packages:**
  - `requests` (v2.25.0+) for handling HTTP requests.
  - `python-dotenv` (v0.15.0+) for loading environment variables from a `.env` file.
- **Hugging Face Account:** You'll need to [create a Hugging Face account](https://huggingface.co/join) to obtain an API token.

### Installation Steps
1. **Clone or Download the Project:**
   ```bash
   git clone https://github.com/chaudhari-kau/HCI-Assignment4.git
   cd HCI-Assignment4
   ```

2. **Install Dependencies:**
   - Open your terminal, navigate to the project directory, and run:
     ```bash
     pip install requests python-dotenv
     ```
   - Alternatively, if you have a `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

3. **Create a `.env` File:**
   - In the project root directory, create a file named `.env` and add your Hugging Face API token in the following format:
     ```bash
     HF_TOKEN="YOUR_API_TOKEN_HERE"
     ```
   > **Important Security Notes:** 
   > - Replace the placeholder with your actual Hugging Face API token
   > - Keep this file secure and NEVER commit it to version control
   > - The `.gitignore` file is configured to exclude `.env` files
   > - Rotate your API tokens regularly as a security best practice

4. **Get a Hugging Face API Token:**
   - Visit the [Hugging Face website](https://huggingface.co/settings/tokens)
   - Sign in or create an account
   - Navigate to your profile settings -> Access Tokens
   - Create a new token with "read" permissions
   - Copy the generated token to your `.env` file

## Project Structure 📁
```
HCI-Assignment4/
├── .env                  # Environment variables file (not tracked by Git)
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── main.py               # Main application code
```

## Running the Application 🏃‍♂️💨
1. Ensure you've completed all installation steps above
2. Open a terminal and navigate to the project directory
3. Run the application using:
   ```bash
   python main.py
   ```
4. The application will:
   - Load your API token from the `.env` file
   - Send a creative prompt to the Hugging Face API
   - Display the generated "Hello World" message in the terminal

## Example Output 📝
```
Generated 'Hello World' message:
Hello World! Today is a fantastic day to explore the wonders of AI. Let the creativity begin: with a new language model, we can generate text that resembles human writing. This technology can help us understand how language works and how we might improve communication between humans and machines.
```
*Note: Actual output will vary due to the nature of generative AI.*

## How It Works 🔧
1. **Environment Setup**: The application loads the API token from a `.env` file using `python-dotenv`
2. **API Request Preparation**: It constructs a payload with:
   - A prompt ("Hello World!" followed by a creative context)
   - Parameters to control generation (max length, temperature)
   - Options for API behavior (waiting for model loading)
3. **API Call**: It sends a POST request to the Hugging Face Inference API
4. **Response Processing**: It parses the JSON response and extracts the generated text
5. **Output Display**: It prints the creative "Hello World" message to the console

## Troubleshooting 🔍
- **API Token Issues**: Ensure your token is correctly formatted in the `.env` file
- **Connection Errors**: Check your internet connection and firewall settings
- **Rate Limiting**: Hugging Face has usage limits; if exceeded, wait before trying again
- **Response Format Issues**: Verify that the API response structure matches what's expected in the code



## Learning Resources 📚
- [Hugging Face Documentation](https://huggingface.co/docs)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [Environment Variables in Python](https://pypi.org/project/python-dotenv/)
- [API Security Best Practices](https://owasp.org/www-project-api-security/)

## License 📄
This project is released under the MIT License. See the LICENSE file for details.

## Acknowledgments 👏
- Hugging Face for providing access to powerful language models
- The open-source community for developing the tools and libraries used in this project