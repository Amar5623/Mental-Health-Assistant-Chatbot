# Mental Health Chatbot Assistant

A supportive AI chatbot designed to provide a safe space for users to express their thoughts and feelings, with a focus on mental health support.

## Features

- Emotion detection and sentiment analysis
- Personalized responses based on user history
- Mental health resources and crisis information
- User-friendly interface with real-time chat

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/mental-health-chatbot.git
   cd mental-health-chatbot
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Download NLTK data (for TextBlob):
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
   ```

## Running the Application

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

- `app.py`: Main Flask application
- `chatbot.py`: Chatbot engine with response generation logic
- `emotion_analyzer.py`: Emotion detection and sentiment analysis
- `resources.py`: Mental health resources and information
- `templates/`: HTML templates
- `static/`: CSS, JavaScript, and other static files
- `data/`: JSON files for responses and user history

## Disclaimer

This chatbot is not a substitute for professional mental health support. If you or someone you know is in crisis, please contact a mental health professional or crisis helpline immediately.

## License

MIT
