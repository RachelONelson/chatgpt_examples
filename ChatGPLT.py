import openai
import configparser

# Set your OpenAI API key
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openapi']['api']

openai.api_key = get_api_key()

def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        try:
            # Send the input to the OpenAI GPT model
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Choose the model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )

            # Extract and print the model's response
            reply = response['choices'][0]['message']['content']
            print(f"Chatbot: {reply}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chatbot()