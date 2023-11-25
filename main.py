import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or specify the appropriate engine
        prompt=prompt,
        max_tokens=150  # adjust as needed
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
