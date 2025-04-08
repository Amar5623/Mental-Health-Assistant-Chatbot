import json
import os
import random
import time
from datetime import datetime
from emotion_analyzer import EmotionAnalyzer
import difflib
from resources import MentalHealthResources
from collections import defaultdict
import google.generativeai as genai  # Gemini integration

# Configure Gemini API (replace with your actual API key)
genai.configure(api_key="AIzaSyCegmzgSkEX0SKQTdU1Dl5swf5dZYBqr3U")

USE_GEMINI = True
GEMINI_MODEL_NAME = "gemini-1.5-flash"

class ChatbotEngine:
    def __init__(self):
        self.user_history = {}
        self.emotion_analyzer = EmotionAnalyzer()
        self.resources = MentalHealthResources()
        self.load_responses()
        self.user_concerns = defaultdict(set)

    def load_responses(self):
        try:
            with open('data/responses.json', 'r') as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            self.responses = {
                "greetings": [
                    "Hello! I'm here to listen. How are you feeling today?",
                    "Hi there! I'm your mental health assistant. How can I support you today?",
                    "Welcome! I'm here to chat whenever you need someone to talk to."
                ],
                "joy": [
                    "I'm glad to hear you're feeling positive! What's contributing to that feeling?",
                    "That's wonderful to hear! It's important to acknowledge these good moments.",
                    "I'm happy that you're in a good place right now. Would you like to share more about it?"
                ],
                "sadness": [
                    "I'm sorry to hear you're feeling sad. Would you like to talk more about what's troubling you?",
                    "It's okay to feel sad sometimes. I'm here to listen if you want to share more.",
                    "I appreciate you sharing your feelings with me. Is there anything specific that's making you feel this way?"
                ],
                "anger": [
                    "I can understand why you might feel angry. Would you like to talk about what's frustrating you?",
                    "It sounds like you're dealing with some difficult emotions. I'm here to listen without judgment.",
                    "Anger is a natural response to certain situations. Would it help to explore what triggered these feelings?"
                ],
                "fear": [
                    "It sounds like you're feeling anxious. Remember that it's okay to take things one step at a time.",
                    "I understand that feeling worried can be overwhelming. Would you like to talk about what's causing this anxiety?",
                    "When we're afraid, it can help to break things down into smaller, manageable parts. What's on your mind right now?"
                ],
                "surprise": [
                    "That does sound surprising! How are you processing this unexpected situation?",
                    "Unexpected events can certainly catch us off guard. How are you feeling about this surprise?",
                    "I can understand why you'd be surprised. Would you like to talk more about how this is affecting you?"
                ],
                "disgust": [
                    "That sounds like a difficult situation to deal with. How are you coping with these feelings?",
                    "I understand that some things can be really off-putting. Would you like to talk more about this?",
                    "It's natural to have strong reactions to certain things. How is this affecting you?"
                ],
                "gratitude": [
                    "You're very welcome. I'm here anytime you need to talk.",
                    "I'm glad I could be here for you. Is there anything else on your mind?",
                    "It's my pleasure to be here with you. How else can I support you today?"
                ],
                "confusion": [
                    "It sounds like you're trying to make sense of things. Would it help to explore this together?",
                    "Feeling confused is completely normal, especially when dealing with complex emotions. Let's take it step by step.",
                    "I understand that uncertainty can be challenging. Would you like to talk through what's confusing you?"
                ],
                "neutral": [
                    "How has your day been so far?",
                    "Is there anything specific on your mind today?",
                    "I'm here to chat about whatever you'd like. What's on your mind?"
                ],
                "farewell": [
                    "Take care of yourself. I'll be here when you want to chat again.",
                    "Goodbye for now. Remember to be kind to yourself.",
                    "I'll be here whenever you need to talk. Have a peaceful day."
                ],
                "fallback": [
                    "I'm here to listen. Would you like to tell me more?",
                    "I appreciate you sharing that. How does that make you feel?",
                    "Thank you for expressing that. Would you like to explore this further?"
                ],
                "encouragement": [
                    "Remember that it's okay to have difficult days. You're doing the best you can.",
                    "I believe in your ability to navigate through these challenges. Take it one step at a time.",
                    "Your feelings are valid, and it's brave of you to express them. That's an important step."
                ],
                "resources": [
                    "If you're feeling overwhelmed, remember that professional help is available. Would you like me to provide some resources?",
                    "Sometimes talking to a mental health professional can be really beneficial. Would you like information about finding support?",
                    "There are many resources available to support mental health. Would it be helpful if I shared some with you?"
                ]
            }  # Keep existing response dictionary content
            os.makedirs('data', exist_ok=True)
            with open('data/responses.json', 'w') as f:
                json.dump(self.responses, f, indent=4)

    def simulate_thinking(self):
        print("[thinking...]")
        time.sleep(random.uniform(1.5, 2.5))

    def similarity(self, text1, text2):
        return difflib.SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

    def extract_concerns(self, message):
        text = message.lower()
        topics = {
            "stress": ["stress", "pressure", "overwhelmed", "tension"],
            "anxiety": ["anxiety", "nervous", "panic", "worried"],
            "depression": ["depressed", "sad", "hopeless", "empty", "worthless"],
            "relationship": ["relationship", "partner", "breakup", "heartbreak"],
            "self-esteem": ["self-esteem", "confidence", "insecure", "worthless"],
            "academic": ["exam", "study", "grades", "assignment", "deadline"],
            "work": ["job", "work", "career", "boss", "burnout"],
            "loneliness": ["alone", "lonely", "isolated", "nobody"],
            "grief": ["loss", "grief", "died", "passed away", "funeral"],
        }
        concerns = set()
        for topic, keywords in topics.items():
            if any(word in text for word in keywords):
                concerns.add(topic)
        return concerns

    def detect_intent(self, text):
        text_lower = text.lower()
        if any(word in text_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return "greetings"
        elif any(word in text_lower for word in ['thank', 'thanks', 'appreciate']):
            return "gratitude"
        elif any(word in text_lower for word in ['bye', 'goodbye', 'see you', 'farewell']):
            return "farewell"
        elif any(word in text_lower for word in ['help', 'resource', 'support', 'therapist', 'counselor']):
            return "resources"
        elif any(word in text_lower for word in ['crisis', 'emergency', 'suicidal', 'suicide', 'kill myself']):
            return "crisis"
        elif any(word in text_lower for word in ['therapy', 'therapist', 'counseling', 'professional help']):
            return "therapy"
        elif any(word in text_lower for word in ['self-help', 'app', 'book', 'meditation', 'mindfulness']):
            return "self_help"
        else:
            emotion_result = self.emotion_analyzer.analyze(text)
            if emotion_result['emotions']:
                return emotion_result['emotions'][0]
            elif emotion_result['sentiment'] == 'positive':
                return 'joy'
            elif emotion_result['sentiment'] == 'negative':
                return 'sadness'
            else:
                return 'neutral'

    def save_interaction(self, user_id, message, response):
        if user_id not in self.user_history:
            self.user_history[user_id] = []

        concerns = list(self.extract_concerns(message))
        for concern in concerns:
            self.user_concerns[user_id].add(concern)

        self.user_history[user_id].append({
            'user_message': message,
            'bot_response': response,
            'concerns': concerns,
            'timestamp': datetime.now().isoformat()
        })

        try:
            os.makedirs('data/user_history', exist_ok=True)
            with open(f'data/user_history/{user_id}.json', 'w') as f:
                json.dump(self.user_history[user_id], f, indent=4)
        except Exception as e:
            print(f"Error saving user history: {e}")

    def load_user_history(self, user_id):
        try:
            with open(f'data/user_history/{user_id}.json', 'r') as f:
                self.user_history[user_id] = json.load(f)
        except FileNotFoundError:
            self.user_history[user_id] = []
        except Exception as e:
            print(f"Error loading user history: {e}")
            self.user_history[user_id] = []

    def get_top_concerns(self, user_id, top_n=3):
        concern_count = defaultdict(int)
        for interaction in self.user_history.get(user_id, []):
            for concern in interaction.get('concerns', []):
                concern_count[concern] += 1
        sorted_concerns = sorted(concern_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_concerns[:top_n]

    def get_personalized_response(self, intent, user_id, message):
        if user_id not in self.user_history or len(self.user_history[user_id]) < 3:
            return random.choice(self.responses.get(intent, self.responses["fallback"]))

        recent_messages = [item['user_message'] for item in self.user_history[user_id][-5:]]
        negative_count = sum(1 for msg in recent_messages if self.emotion_analyzer.analyze(msg)['sentiment'] == 'negative')

        if negative_count >= 3 and intent in ['sadness', 'fear', 'anger']:
            return ("I've noticed you've been feeling down for a while. " +
                    "Remember that it's okay to seek help when needed. " +
                    "Would talking to a mental health professional be something you'd consider?")

        if len(recent_messages) >= 2 and any(
            self.similarity(recent_messages[-1], msg) > 0.7 for msg in recent_messages[:-1]
        ):
            return ("I notice this seems to be a recurring concern for you. " +
                    "Sometimes talking through the same issue from different angles can help. " +
                    "Would it help to explore what might be keeping this on your mind?")

        if len(recent_messages) >= 4 and all('?' not in msg for msg in recent_messages):
            return ("Thank you for sharing so openly with me. " +
                    "I'm wondering if there's anything specific you'd like my perspective on, " +
                    "or if it's helpful just to express your thoughts?")

        crisis_keywords = ['kill myself', 'suicide', 'end my life', 'harm myself', 'hurt myself']
        if any(keyword in message.lower() for keyword in crisis_keywords):
            return ("I'm really concerned about what you're sharing. If you're having thoughts of harming yourself, " +
                    "please reach out to a crisis helpline immediately. In the US, you can text HOME to 741741 to reach the Crisis Text Line, " +
                    "or call the National Suicide Prevention Lifeline at 1-800-273-8255. These services are confidential and available 24/7. " +
                    "Would you like me to provide more resources?")

        return random.choice(self.responses.get(intent, self.responses["fallback"]))

    def generate_gemini_response(self, message, user_id):
        recent_history = self.user_history.get(user_id, [])[-5:]
        context = "\n".join(f"User: {item['user_message']}\nBot: {item['bot_response']}" for item in recent_history)
        prompt = (
            "You are a compassionate and thoughtful mental health support assistant. "
            "Speak in a gentle, friendly, and non-judgmental tone. Be empathetic, supportive, and validating. "
            f"Use this past conversation to maintain context:\n{context}\nUser: {message}\nBot:"
        )

        try:
            model = genai.GenerativeModel(GEMINI_MODEL_NAME)
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Gemini error: {e}")
            return None

    def get_response(self, message, user_id, context=None):
        self.simulate_thinking()
        if user_id not in self.user_history:
            self.load_user_history(user_id)

        intent = self.detect_intent(message)

        if intent == "resources":
            return self.resources.format_resources_for_chat("all")
        elif intent == "crisis":
            return self.resources.format_resources_for_chat("crisis")
        elif intent == "therapy":
            return self.resources.format_resources_for_chat("therapy")
        elif intent == "self_help":
            return self.resources.format_resources_for_chat("self_help")

        crisis_keywords = ['kill myself', 'suicide', 'end my life', 'harm myself', 'hurt myself']
        if any(keyword in message.lower() for keyword in crisis_keywords):
            crisis_response = ("I'm really concerned about what you're sharing. If you're having thoughts of harming yourself, " +
                               "please reach out to a crisis helpline immediately. " +
                               "Here are some resources that can help:\n\n")
            return crisis_response + self.resources.format_resources_for_chat("crisis")

        response = self.get_personalized_response(intent, user_id, message)

        if USE_GEMINI:
            gemini_response = self.generate_gemini_response(message, user_id)
            if gemini_response:
                response = gemini_response

        self.save_interaction(user_id, message, response)

        trend_score = self.get_emotion_trend(user_id)
        if trend_score >= 2:
            response += " I'm really glad to see you feeling a bit better lately. Keep it going!"
        elif trend_score <= -2:
            response += " I’ve noticed you’ve been feeling down for a while. Would you like to talk more about what’s been going on?"

        return response

    def get_emotion_trend(self, user_id, window=5):
        history = self.user_history.get(user_id, [])[-window:]
        sentiments = [self.emotion_analyzer.analyze(h['user_message'])['sentiment'] for h in history]
        score = sentiments.count('positive') - sentiments.count('negative')
        return score
