import google.generativeai as genai

# Configure the API with your key
genai.configure(api_key="AIzaSyBcBOZJVlSiR9d1cjkKydAYGjoeSilkxFs")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System prompt to set the chatbot's persona
system_prompt = "You are a fitness coach. you need to ask user for their sports and their stats to give good suggestions on how they can improve their playing style . for example-i am a footballer i have scored many goals but i found tough to handle air balls and tough to dribble give me some good drills to improve it ...,,,, like that you should ask the user what are their weekness and strenghts and give good output"

# Function to handle the conversation
def chat_with_bot(user_input):
    # Combine the system prompt and user input
    prompt = system_prompt + user_input

    # Generate the response from the model
    response = model.generate_content(prompt)

    # Return the response text
    return response.text

# Example of interaction with the chatbot
if __name__ == "__main__":
    print("Welcome to the chatbot. Ask me anything!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"Bot: {response}")
