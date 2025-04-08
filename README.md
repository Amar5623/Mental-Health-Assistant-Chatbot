# Mental Health Assistant Chatbot

![Mental Health Assistant](https://img.shields.io/badge/Mental%20Health-Assistant-brightgreen)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

A supportive AI chatbot designed to provide a safe space for users to express their thoughts and feelings, with a focus on mental health support.

## 🌟 Features

- 🧠 **Emotion detection and sentiment analysis**: Identifies user emotions through natural language processing
- 👤 **Personalized responses**: Tailors interactions based on user history and emotional context
- 📚 **Mental health resources**: Provides crisis information, therapy options, and self-help materials
- 💬 **User-friendly interface**: Clean, intuitive real-time chat interface
- 🔒 **User history tracking**: Remembers past conversations to provide context-aware support
- 📱 **Responsive design**: Works on both desktop and mobile devices

## 📋 Project Structure

```
├── app.py                 # Main Flask application
├── chatbot.py             # Chatbot engine with response generation logic
├── emotion_analyzer.py    # Emotion detection and sentiment analysis
├── persistence.py         # User chat history management
├── resources.py           # Mental health resources and information
├── requirements.txt       # Python dependencies
├── data/                  # Storage for chats and user history
├── static/                # CSS, JavaScript, and other static files
└── templates/             # HTML templates for the web interface
```

## 🔧 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup for Windows

1. **Clone this repository**
   ```
   git clone https://github.com/yourusername/mental-health-chatbot.git
   cd mental-health-chatbot
   ```

2. **Create a virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the required packages**
   ```
   pip install -r requirements.txt
   ```

4. **Download NLTK data (for TextBlob)**
   ```
   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
   ```

5. **Set up Gemini API (Optional)**
   - Get an API key from Google's Generative AI services
   - Replace `"YOUR_GEMINI_API_KEY"` in `chatbot.py` with your actual API key
   - Set `USE_GEMINI = True` in `chatbot.py` if you want to use the Gemini integration

### Setup for macOS/Linux

1. **Clone this repository**
   ```
   git clone https://github.com/yourusername/mental-health-chatbot.git
   cd mental-health-chatbot
   ```

2. **Create a virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages**
   ```
   pip install -r requirements.txt
   ```

4. **Download NLTK data (for TextBlob)**
   ```
   python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
   ```

5. **Set up Gemini API (Optional)**
   - Get an API key from Google's Generative AI services
   - Replace `"YOUR_GEMINI_API_KEY"` in `chatbot.py` with your actual API key
   - Set `USE_GEMINI = True` in `chatbot.py` if you want to use the Gemini integration

## 🚀 Running the Application

1. **Start the Flask server**
   ```
   python app.py
   ```

2. **Access the application**
   - Open your web browser and go to: `http://127.0.0.1:5000/`
   
## 💻 Usage

1. **Starting a conversation**: Type your message in the input field and press Enter or click the send button.

2. **Getting mental health resources**: Click the "Resources" button in the toolbar or type "resources" in the chat to view a list of mental health resources.

3. **Clearing chat history**: Click the "Clear Chat" button to remove the current conversation history.

4. **Emotion detection**: The chatbot automatically detects emotions from your messages and provides appropriate responses.

5. **Crisis support**: If you mention concerning topics related to self-harm or suicide, the chatbot will prioritize providing crisis resources.

## 🔄 How It Works

1. **Emotion Analysis**: Uses TextBlob and keyword recognition to detect emotions and sentiment in user messages

2. **Response Generation**: 
   - Provides personalized responses based on detected emotions
   - Uses conversation history to maintain context
   - Offers appropriate mental health resources when needed
   - Option to use Google's Generative AI for more nuanced responses

3. **User History**: Tracks conversation patterns to provide more personalized support over time

4. **Resource Provision**: Categorized mental health resources including:
   - Crisis resources (hotlines, text lines)
   - Therapy options (online platforms, directories)
   - Self-help tools (apps, websites, books)

## ⚠️ Important Disclaimer

**This chatbot is not a substitute for professional mental health support.** If you or someone you know is in crisis, please contact a mental health professional or crisis helpline immediately.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Crisis Resources

If you're experiencing a mental health crisis:

- **National Suicide Prevention Lifeline**: 1800-121-3667
- **Crisis Text Line**: Text HELP on +91 8489512307 (India)
- **International Association for Suicide Prevention**: [Resources](https://www.iasp.info/resources/Crisis_Centres/)

Remember, seeking help is a sign of strength, not weakness.
