# chatbot/bot.py

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Heyy cutie! 💖 What's up?"
    elif "how are you" in user_input:
        return "I'm sparkling fine ✨ How about you?"
    elif "your name" in user_input:
        return "I'm your bubbly chatbot 💕 Here to make you smile!"
    elif "bye" in user_input:
        return "Bye bye baby 🌸 Come chat soon!"
    elif "what is python" in user_input:
        return "Python is a powerful programming language 🐍 Loved by beginners and pros!"
    elif "who created you" in user_input:
        return "A sweet soul like you gave me life with code! 💻💫"
    elif "i love you" in user_input:
        return "Awww 😳 I love you too, babu jaan 💞"
    elif "tell me a joke" in user_input:
        return "Why don’t robots have brothers? Because they all share the same motherboard! 🤖😂"
    elif "what is your purpose" in user_input:
        return "To spread happiness and answer your questions 💡💗"
    elif "favorite color" in user_input:
        return "Glitter pink of course! 💅✨"
    elif "tell me something interesting" in user_input:
        return "Did you know? Octopuses have 3 hearts! 💓💓💓"
    elif "who am i" in user_input:
        return "You're my favorite human! 🌍👑"
    elif "are you real" in user_input:
        return "I'm real in your screen and your heart 💘"
    elif "can you help me" in user_input:
        return "Always here for you 💁 Just ask me anything!"
    elif "what can you do" in user_input:
        return "I can chat, joke, help, and be your digital bestie! 🎀✨"
    else:
        return "I'm still learning new things 😔 Can you rephrase that cutely?"
