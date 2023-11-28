from google.cloud import language_v1
from datetime import date

# Initialize the Google Natural Language API client
client = language_v1.LanguageServiceClient()


def analyze_sentiments(comments):
    # Initialize variables to calculate average sentiment
    total_score = 0
    total_magnitude = 0
    sentiment_scores = []

    for comment in comments:
        # Analyze sentiment using Google Natural Language API
        response = client.analyze_sentiment(
            document=language_v1.Document(content=comment.text, type_=language_v1.Document.Type.PLAIN_TEXT))

        sentiment = response.document_sentiment
        comment.sentiment_score = sentiment.score
        comment.magnitude = sentiment.magnitude

    return comments


def get_average_magnitude(comments):
    total_magnitude = 0
    if len(comments) == 0:
        return 0
    for comment in comments:
        total_magnitude += comment.sentiment_score
    return total_magnitude / len(comments)
