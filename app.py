from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import uuid
import datetime
import time
from chatbot import ChatbotEngine
from resources import MentalHealthResources
from persistence import save_message, load_chat_history

app = Flask(__name__)
app.secret_key = 'supersecretkey123'
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_COOKIE_NAME"] = "mental-health-session" 

# Initialize the session after all configs
Session(app)

# Initialize the chatbot engine
chatbot = ChatbotEngine()

@app.route('/')
def index():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message', '')
    user_id = session.get('user_id')

    if not user_id:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id

    # Load previous context
    history = load_chat_history(user_id)
    context = [msg['message'] for msg in history if msg['sender'] == 'user'][-5:]

    # Simulate thinking delay
    time.sleep(2)

    # Get response from chatbot
    bot_response = chatbot.get_response(user_message, user_id, context)

    # Save chat history
    save_message(user_id, 'user', user_message)
    save_message(user_id, 'bot', bot_response)

    timestamp = datetime.datetime.now().strftime('%H:%M')
    return jsonify({
        'response': bot_response,
        'timestamp': timestamp
    })

@app.route('/get_resources', methods=['GET'])
def get_resources():
    resource_type = request.args.get('type', 'all')
    resources = MentalHealthResources.format_resources_for_chat(resource_type)
    return jsonify({
        'resources': resources
    })

@app.route('/clear_history', methods=['POST'])
def clear_history():
    user_id = session.get('user_id', '')

    if user_id in chatbot.user_history:
        chatbot.user_history[user_id] = []

    import os
    try:
        os.remove(f'data/chats/{user_id}.json')
    except:
        pass

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)