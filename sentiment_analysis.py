import streamlit as st
from transformers import pipeline

def run():
    st.title("Sentiment Analysis")

    sentiment_pipeline = pipeline("sentiment-analysis")

    text = st.text_area("Enter text for sentiment analysis:", height=200)
    
    if st.button("Analyze"):
        if text:
            result = sentiment_pipeline(text)
            st.write("Result:", result)
        else:
            st.write("Please enter text to analyze.")

if __name__ == '__main__':
    run()
