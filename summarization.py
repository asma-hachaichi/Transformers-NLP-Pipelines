import streamlit as st
from transformers import pipeline

def run():
    st.title("Summarization")

    summarization_pipeline = pipeline("summarization")

    text = st.text_area("Enter text to summarize:", height=200)
    
    if st.button("Summarize"):
        if text:
            result = summarization_pipeline(text)
            st.write("Summary:", result[0]['summary_text'])
        else:
            st.write("Please enter text to summarize.")

if __name__ == '__main__':
    run()
