# My Streamlit App

A simple Mood Detector app built with Streamlit and TextBlob NLTK.

## Features

- **Sentiment Analysis**: Detect positive/negative sentiment in text
- **Mood Detection**: Classify text into different mood categories
- **Real-time Processing**: Instant analysis as you type
- **User-friendly Interface**: Clean and intuitive design

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation & Running

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

**Create a Virtual Environment (Optional)**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

2. **Install the requirements**
    pip install -r requirements.txt

**Install TextBlob if first time using it**
    python -m textblob.download_corpora

3. **Run the app**
    streamlit run main.py

4.**Open your browser AT**
    http://localhost:8501