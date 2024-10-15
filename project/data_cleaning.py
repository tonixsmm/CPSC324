import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from textblob import TextBlob
import re

# Download NLTK stopwords
import nltk
nltk.download('stopwords')


def clean_data(df):
    # Handle quoting inconsistencies
    df.replace(to_replace=["'", '"'], value=["''", '""'], regex=True, inplace=True)

    # Replace newlines and other problematic characters in all string columns
    df = df.applymap(lambda x: x.replace('\n', ' ').replace('\r', ' ') if isinstance(x, str) else x)
    return df

def load_file(file_path):
    df = pd.read_csv(file_path, on_bad_lines = 'warn', lineterminator='\n')
    return df

def save_file(df, file_path):
    df.to_csv(file_path, index=False)

def clean_text(text):
    """Clean raw tweet text for analysis."""
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    # Remove user mentions
    text = re.sub(r'@\w+', '', text)
    # Remove hashtags 
    # text = re.sub(r'#', '', text)
    # Remove punctuations and numbers
    text = re.sub(r'[^\w\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def preprocess_data(file_path):
    """Load and preprocess data."""
    # Load data
    df = pd.read_csv(file_path)
    df = clean_data(df)
    
    # Clean text data
    df['cleaned_tweet'] = df['tweet'].apply(clean_text)
    # df.drop(columns=['tweet'], inplace=True)
    df = df[['cleaned_tweet']]
    
    # Handle missing values
    df.fillna('', inplace=True)

    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=999)
    tfidf_matrix = vectorizer.fit_transform(df['cleaned_tweet'])

    return df, tfidf_matrix


if __name__ == '__main__':
    file_path = 'biden_cleaned.csv'
    processed_data, features = preprocess_data(file_path)
    
    processed_data.to_csv('processed_tweets_biden.csv', index=False)

    features_df = pd.DataFrame(features.toarray())
    features_df['sentiment_label'] = processed_data['cleaned_tweet'].apply(lambda text: 'positive' if TextBlob(text).sentiment.polarity > 0 else 'negative' if TextBlob(text).sentiment.polarity < 0 else 'neutral')
    features_df.to_csv('processed_tweets_features_biden.csv', index=False)
