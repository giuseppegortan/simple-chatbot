import openai
import os
from dotenv import load_dotenv

class SimpleChatbot:
    def __init__(self):
        # Load environment variables from a .env file
        load_dotenv()

        #Get the OpenAI API key from environment variables
        api_key = os.getenv("OPENAI_API_KEY")

        #check if the API key is available
        if not api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")   
        else:
            #Create an OpenAI client instance
            self.client = openai.OpenAI(api_key=api_key)
            #Initialize the OpenAI client with system message
            self.conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]

    def talk(self, user_input: str) -> str:
        """Send user input to the OpenAI API and get a response."""
        #Add user input to the conversation history
        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            #Send the conversation history to the OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.conversation_history
            )

            #Extract the assistant's reply from the response
            assistant_reply = response.choices[0].message['content']

            #Add the assistant's reply to the conversation history
            self.conversation_history.append({"role": "assistant", "content": assistant_reply})

            return assistant_reply
        except Exception as e:
            return f"An error occurred: {e}"
        
    def init(self):
        """Start the interactive chat loop."""
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("Goodbye!")
                    break
                response = self.talk(user_input)
                print(f"Bot: {response}")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
if __name__ == "__main__":
    try:
        chatbot = SimpleChatbot()
        chatbot.init()
    except ValueError as ve:
        print(f"Initialization error: {ve}")