import streamlit as st
import sentiment_analysis
import question_answering
import summarization
import ner

def main():
    # Get query parameters to handle navigation
    page = st.query_params["page"] if "page" in st.query_params else "home"

    if page == "home":
        st.title("NLP Pipelines Demo")
        st.write("Welcome to the Transformers' NLP Pipelines Demo!")
        st.write("Please choose one of the following pipelines to proceed.")
        
        if st.button("Sentiment Analysis"):
            st.query_params.page="sentiment_analysis"
            st.experimental_rerun()

        if st.button("Question Answering"):
            st.query_params.page="question_answering"
            st.experimental_rerun()

        if st.button("Summarization"):
            st.query_params.page="summarization"
            st.experimental_rerun()

        if st.button("Named Entity Recognition"):
            st.query_params.page="ner"
            st.experimental_rerun()
    
    elif page == "sentiment_analysis":
        sentiment_analysis.run()

    elif page == "question_answering":
        question_answering.run()

    elif page == "summarization":
        summarization.run()

    elif page == "ner":
        ner.run()

if __name__ == '__main__':
    main()
