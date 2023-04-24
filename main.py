#follow me on github for more challeging projects: www.github.com/gamer-snave
import openai
import tkinter as tk

# Set up OpenAI API credentials
openai.api_key = ""

"""You can also use dotenv to hide your api keys.
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
Save your api key in a file called .env 
and add .env to your .gitignore file."""


# Initialize the GPT-3 language model
model_engine = "text-davinci-002"
prompt = "Hi, how can I help you today?"
temperature = 0.7
max_tokens = 60

# Define a function to generate a response from the GPT-3 model
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

# Define a function to send a message and generate a response
def send_message():
    user_message = input_box.get()
    input_box.delete(0, tk.END)
    chat_history.insert(tk.END, "You: " + user_message + "\n")
    prompt = "User: " + user_message + "\nBot:"
    response = generate_response(prompt)
    chat_history.insert(tk.END, response + "\n")
    chat_history.see(tk.END)

# Set up the GUI
root = tk.Tk()
root.title("OpenAI Chatbot-Kashipara")

# Create a chat history display box
chat_history = tk.Text(root, height=20, width=60, font=("Helvetica", 12))
chat_history.grid(row=0, column=0, padx=10, pady=10)

# Create an input box for the user's messages
input_box = tk.Entry(root, width=60, font=("Helvetica", 12))
input_box.grid(row=1, column=0, padx=10, pady=10)

# Create a "Send" button to send messages
send_button = tk.Button(root, text="Send", font=("Helvetica", 12), command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()

