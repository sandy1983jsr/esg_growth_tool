import pandas as pd
from transformers import pipeline

# Use Hugging Face Transformers sentiment pipeline (distilbert)
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(texts):
    results = sentiment_pipeline(texts)
    sentiments = []
    for i, res in enumerate(results):
        sentiments.append({
            'text': texts[i][:100],
            'label': res['label'],
            'score': res['score']
        })
    return pd.DataFrame(sentiments)

# Example usage
if __name__ == "__main__":
    example_feedback = [
        "The company's move to 100% renewable energy is impressive.",
        "There is still a lack of diversity in management positions.",
        "Net zero pledge seems like greenwashing."
    ]
    sentiment_df = analyze_sentiment(example_feedback)
    print(sentiment_df)
