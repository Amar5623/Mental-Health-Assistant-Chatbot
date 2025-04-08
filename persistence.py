import os
import json

# Directory to store chat logs
CHAT_DIR = "data/chats"

# Ensure the directory exists
os.makedirs(CHAT_DIR, exist_ok=True)

def save_message(user_id, sender, message):
    chat_file = os.path.join(CHAT_DIR, f"{user_id}.json")
    if os.path.exists(chat_file):
        with open(chat_file, 'r') as f:
            chat_history = json.load(f)
    else:
        chat_history = []

    chat_history.append({'sender': sender, 'message': message})

    with open(chat_file, 'w') as f:
        json.dump(chat_history, f, indent=4)

def load_chat_history(user_id):
    chat_file = os.path.join(CHAT_DIR, f"{user_id}.json")
    if os.path.exists(chat_file):
        with open(chat_file, 'r') as f:
            return json.load(f)
    return []
