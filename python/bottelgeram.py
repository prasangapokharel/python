import openai
import os

# Set your OpenAI GPT-3 API key
openai.api_key = os.getenv("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")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def chat():
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    conversation_history = ""

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            break

        conversation_history += f"You: {user_input}\n"
        response = generate_response(conversation_history)
        conversation_history += f"ChatGPT: {response}\n"

        print(f"ChatGPT: {response}")

if __name__ == "__main__":
    chat()

