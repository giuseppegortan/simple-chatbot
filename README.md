# simple-chatbot
Simple chatbot based on OpenAI API



# simple-chatbot
Simple chatbot based on the OpenAI API

## Installation

1. Clone the repository or download the files.
2. Make sure you have Python 3.8+ installed.
3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Set the `OPENAI_API_KEY` environment variable or create a `.env` file in the same folder with the following content:

```
OPENAI_API_KEY=sk-...
```

## Usage

Run the application from the folder where `main.py` is located:

```
python main.py
```

## Interactive Test

Example session:

```
You: Hi, who are you?
Bot: Hello! I am a virtual assistant powered by OpenAI. How can I help you today?

You: Tell me a joke.
Bot: Sure! Why did the computer go to the doctor? Because it had a virus!

You: exit
Goodbye!
```

The chatbot maintains the conversation and responds naturally thanks to the OpenAI API.
