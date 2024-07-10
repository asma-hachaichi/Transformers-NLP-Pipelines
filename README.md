# Transformers NLP Pipelines Demo

This Streamlit-based web application demonstrates the use of various NLP pipelines using the Hugging Face Transformers library. The application includes the following features:

- **Sentiment Analysis**: Classify the sentiment of the given text as positive or negative.
- **Question Answering**: Provide an answer to a question based on the given context.
- **Summarization**: Generate a concise summary of the provided text.
- **Named Entity Recognition (NER)**: Identify and categorize entities (like names of people, organizations, locations) within the input text.

Each feature is accessible through a user-friendly interface with dedicated pages for each NLP task.

## File Structure

- `app.py`: The main application file containing the menu and navigation logic.
- `sentiment_analysis.py`: Interface and logic for the Sentiment Analysis pipeline.
- `question_answering.py`: Interface and logic for the Question Answering pipeline.
- `summarization.py`: Interface and logic for the Summarization pipeline.
- `ner.py`: Interface and logic for the Named Entity Recognition pipeline.

## How to Run

1. **Install the required packages**:

   ```sh
   pip install streamlit transformers torch
   ```

2. **Run the main application**:
   ```sh
   streamlit run app.py
   ```

## Requirements

- Python 3.6 or higher
- Streamlit
- Transformers
- Tensorflow

## Getting Started

1. Clone the repository:

   ```sh
   git clone https://github.com/asma-hachaichi/Transformers-NLP-Pipelines.git
   cd Transformers-NLP-Pipelines
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   streamlit run app.py
   ```

## App Pages

1. **Home Page**:
   - Welcome message and navigation buttons for each NLP task.
2. **Sentiment Analysis**:
   - Text input area and sentiment analysis results.
3. **Question Answering**:

   - Context and question input areas, with the generated answer displayed.

4. **Summarization**:
   - Text input area and the generated summary.
5. **Named Entity Recognition**:
   - Text input area and identified entities displayed.

## Contributing

Feel free to fork this repository, make enhancements, and submit pull requests. Any contributions to improve the application are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
