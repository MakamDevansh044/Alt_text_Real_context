from textblob import TextBlob

class SentimentService:
    def analyze_sentiment(self, text: str) -> dict:
        try:
            # Use TextBlob for sentiment analysis
            analysis = TextBlob(text)
            
            # Get polarity (-1 to 1) and subjectivity (0 to 1)
            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity
            
            # Determine sentiment label
            if polarity > 0:
                sentiment = "positive"
            elif polarity < 0:
                sentiment = "negative"
            else:
                sentiment = "neutral"
                
            # Extract emotional elements (keywords)
            words = text.lower().split()
            emotional_elements = [word for word in words if len(word) > 3][:5]
            
            return {
                "polarity": polarity,
                "subjectivity": subjectivity,
                "sentiment": sentiment,
                "emotional_elements": emotional_elements
            }
            
        except Exception as e:
            print(f"Sentiment analysis error: {str(e)}")
            raise Exception(f"Sentiment analysis failed: {str(e)}")