import streamlit as st
from transformers import pipeline

def run():
    st.title("Question Answering")

    qa_pipeline = pipeline("question-answering")

    context = st.text_area("Context", height=200)
    question = st.text_input("Question")
    
    if st.button("Ask"):
        if context and question:
            result = qa_pipeline(question=question, context=context)
            st.write("Answer:", result['answer'])
        else:
            st.write("Please provide both context and question.")

if __name__ == '__main__':
    run()
