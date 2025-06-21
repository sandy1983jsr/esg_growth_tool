import pandas as pd

def prepare_heatmap_data(signal_df, sentiment_df):
    sentiment_df['sentiment_score'] = sentiment_df['label'].map({'POSITIVE': 1, 'NEGATIVE': -1, 'NEUTRAL': 0}).fillna(0)
    keywords = pd.Series([kw for signals in signal_df['signals'] for kw in eval(str(signals))]).unique()
    heatmap_data = pd.DataFrame({
        'keyword': keywords,
        'demand_signal': [signal_df['signals'].apply(lambda x: kw in eval(str(x))).sum() for kw in keywords],
        'sentiment': [sentiment_df[sentiment_df['text'].str.contains(kw, case=False)]['sentiment_score'].mean() for kw in keywords]
    })
    return heatmap_data
