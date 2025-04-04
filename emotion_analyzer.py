from textblob import TextBlob
import re

class EmotionAnalyzer:
    def __init__(self):
        # Define emotion keywords for better detection
        self.emotion_keywords = {
            'joy': ['happy', 'joy', 'delighted', 'glad', 'pleased', 'excited', 'thrilled', 'content'],
            'sadness': ['sad', 'unhappy', 'depressed', 'down', 'miserable', 'heartbroken', 'gloomy', 'disappointed'],
            'anger': ['angry', 'mad', 'furious', 'irritated', 'annoyed', 'frustrated', 'outraged'],
            'fear': ['afraid', 'scared', 'frightened', 'terrified', 'anxious', 'worried', 'nervous', 'panic'],
            'surprise': ['surprised', 'shocked', 'amazed', 'astonished', 'stunned'],
            'disgust': ['disgusted', 'revolted', 'repulsed', 'sickened'],
            'gratitude': ['grateful', 'thankful', 'appreciative', 'thanks', 'thank you'],
            'confusion': ['confused', 'puzzled', 'perplexed', 'unsure', 'uncertain', 'don\'t understand']
        }
        
        # Compile regex patterns for each emotion
        self.emotion_patterns = {}
        for emotion, keywords in self.emotion_keywords.items():
            pattern = r'\b(' + '|'.join(keywords) + r')\b'
            self.emotion_patterns[emotion] = re.compile(pattern, re.IGNORECASE)
    
    def analyze(self, text):
        """
        Analyze text for emotional content and return the detected emotions
        and overall sentiment polarity.
        """
        # Detect specific emotions based on keywords
        detected_emotions = []
        for emotion, pattern in self.emotion_patterns.items():
            if pattern.search(text):
                detected_emotions.append(emotion)
        
        # Get sentiment polarity using TextBlob
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        # Determine overall sentiment category
        if polarity > 0.3:
            sentiment = "positive"
        elif polarity < -0.3:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        # If no specific emotions were detected, use the sentiment
        if not detected_emotions:
            if sentiment == "positive":
                detected_emotions = ["joy"]
            elif sentiment == "negative":
                # Try to differentiate between common negative emotions
                if any(word in text.lower() for word in ['worry', 'anxious', 'nervous', 'scared']):
                    detected_emotions = ["fear"]
                elif any(word in text.lower() for word in ['angry', 'mad', 'annoyed']):
                    detected_emotions = ["anger"]
                else:
                    detected_emotions = ["sadness"]
        
        return {
            'emotions': detected_emotions,
            'sentiment': sentiment,
            'polarity': polarity
        }
