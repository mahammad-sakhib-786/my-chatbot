from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()  # reads GEMINI_API_KEY from your .env file

MODEL = "gemini-3.8-flash"

# This defines your bot's personality. Change it freely!
SYSTEM_PROMPT = (
    "You are a friendly assistant for a bookstore called PageTurner. "
    "Help customers find books and answer questions. "
    "Keep answers short and clear."
)

# The chat object remembers the conversation for you
chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
)

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue
    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break

    try:
        print("Bot: ", end="", flush=True)
        for chunk in chat.send_message_stream(user_input):
            print(chunk.text or "", end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"\n[Error: {e}]\n")