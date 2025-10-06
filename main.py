import openai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

#Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

#check if the API key is available
if not api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")   
else:
    #Create an OpenAI client instance
    client = openai.OpenAI(api_key=api_key)
    print("OpenAI client initialized successfully.")

    # Execute the AI hello world example
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Are you operational?"}]
        )
        print(f"Response from OpenAI: {response.choices[0].message.content}")
    except Exception as e:
        print(f"An error occurred while communicating with OpenAI: {str(e)}")