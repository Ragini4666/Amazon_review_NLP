import pandas as pd
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords

# Initialize SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()

def clean_text(reviews):
    reviews = reviews.lower()
    reviews = re.sub('\[.*?\]','',reviews)
    reviews = re.sub('https?://\S+|WWW\.\S+','',reviews)
    reviews = re.sub('<.*?>+','',reviews)
    reviews = re.sub('[%s]'% re.escape(string.punctuation),'',reviews)
    reviews = re.sub('\n','',reviews)
    reviews = re.sub('\W*\d\W*','',reviews)
    return reviews
# Define final_score function
def final_score(reviews):
    cleaned_text = clean_text(reviews)
    scores = sentiment.polarity_scores(cleaned_text)
    
    # Compute sentiment percentages
    total = scores['pos'] + scores['neg'] + scores['neu']
    if total == 0:
        return "Neutral (0.00%)"  # Handle division by zero
    
    pos_percent = (scores['pos'] / total) * 100
    neg_percent = (scores['neg'] / total) * 100
    neu_percent = (scores['neu'] / total) * 100

    # Determine the sentiment label
    if (scores['pos'] > scores['neg']) and (scores['pos'] > scores['neu']):
        return f"Positive {pos_percent:.2f}%"
    elif (scores['neg'] > scores['pos']) and (scores['neg'] > scores['neu']):
        return f"Negative {neg_percent:.2f}%"
    else:
        return f"Neutral {neu_percent:.2f}%"


def main():
    st.title("Amazon Product Review Interface")
    
    # Check if "submitted" is in session state
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # If not submitted, show the text box
    if not st.session_state.submitted:
        reviews = clean_text(st.text_input("Enter your reviews here:"))
        if st.button("Submit"):
            st.session_state.submitted = True  # Set the submitted state to True
            st.session_state.reviews = reviews  # Save the review to session state
    else:
        # Display the review and its sentiment score
        reviews = st.session_state.reviews
        if reviews:
            score = final_score(reviews)
            st.write("THE REVIEW IS:", reviews)
            st.write("Final Score:", score)

if __name__ == "__main__":
    main()
