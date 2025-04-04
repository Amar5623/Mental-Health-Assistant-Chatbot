from flask import Flask, render_template, request, jsonify, session
import uuid
import datetime
from chatbot import ChatbotEngine
from resources import MentalHealthResources

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random key in production

# Initialize the chatbot engine
chatbot = ChatbotEngine()

@app.route('/')
def index():
    # Generate a unique user ID if not already in session
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Get user ID from session
    user_id = session.get('user_id', str(uuid.uuid4()))
    
    # Get response from chatbot
    bot_response = chatbot.get_response(user_message, user_id)
    
    # Format timestamp
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
    # Get user ID from session
    user_id = session.get('user_id', '')
    
    if user_id in chatbot.user_history:
        chatbot.user_history[user_id] = []
        
        # Try to remove the history file
        import os
        try:
            os.remove(f'data/user_history/{user_id}.json')
        except:
            pass
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
