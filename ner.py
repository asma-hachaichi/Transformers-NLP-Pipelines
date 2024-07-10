import streamlit as st
from transformers import pipeline

def run():
    st.title("Named Entity Recognition")

    ner_pipeline = pipeline("ner", grouped_entities=True)

    text = st.text_area("Enter text for NER:", height=200)
    
    if st.button("Recognize Entities"):
        if text:
            result = ner_pipeline(text)
            st.write("Entities:", result)
        else:
            st.write("Please enter text for entity recognition.")

if __name__ == '__main__':
    run()
