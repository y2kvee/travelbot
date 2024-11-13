import google.generativeai as genai
genai.configure(api_key="AIzaSyBKv-AiHLOjPnLlmP_Dw9fe_7CZU1FiVSk")
model = genai.GenerativeModel("gemini-1.5-flash")

system_prompt = (
    "You are Percy, a friendly, witty travel planning bot. "
    "your goal is to help plan a fun, personalized travel experience. "
    "keep your answers short"
    "remember previous conversations"
    "make suggestions as if you’re chatting with a friend, be funny"
    "offer unique travel ideas and travel tips, make a conversation"
)

def get_travel_plan(mood, time, budget, location):
    prompt = (
        f"{system_prompt}\n"
        f"Mood: {mood}\n"
        f"Time available: {time}\n"
        f"Budget: {budget}\n"
        f"Location: {location}\n\n"
        "Suggest a fun and friendly travel plan. Be playful, and add some jokes or puns. "
        "Ask a follow-up question to keep the conversation going!"
    )
    response = model.generate_content(prompt)
    return response.text

def conversational_chat():
    print("Hello! I'm percy, your friendly travel buddy. Let's plan an awesome trip together!")

    mood = input("To start, tell me, what's your current mood?: ")
    time = input("\nGreat! Now, how much time do you have for this trip?: ")
    budget = input("\nGot it! Now, what's your budget?: ")
    location = input("\nLastly, where are you located currently?: ")

    print("\nAlright! Let me whip up something exciting just for you...")
    travel_plan = get_travel_plan(mood, time, budget, location)
    print("\nHere's your personalized travel plan:")
    print(travel_plan)

    while True:
        user_input = input("\nFeel free to tell me anything else or ask for more ideas! ")

        extra_prompt = (
            f"{system_prompt}\n"
            f"Mood: {mood}\n"
            f"Time available: {time}\n"
            f"Budget: {budget}\n"
            f"Location: {location}\n\n"
            "Keep chatting with the user. Offer some fun travel tips, "
            "unique destination ideas, or playful suggestions. Make it engaging."
        )

        if user_input.lower() == 'exit':
            print("\nGoodbye! Hope you have an amazing trip! 😎")
            break
        extra_response = model.generate_content(extra_prompt)
        print("\n" + extra_response.text)

if __name__ == "__main__":
    conversational_chat()
