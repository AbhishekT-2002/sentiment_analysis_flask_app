from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize
import string
import re
import emoji
from bs4 import BeautifulSoup
from sklearn.pipeline import Pipeline
from joblib import load

# Initialize Flask app
app = Flask(__name__)

# Load trained pipeline model
model_path = 'model.joblib'
pipeline = load(model_path)

# html tags removal ( if prestnt) 
def remove_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'', text)

# Emoji Handling
def convert_emojis_to_text(text):
    text_with_emojis_converted = emoji.demojize(text)
    return text_with_emojis_converted

def preprocess_text(text):
    text = text.lower()  
    text = remove_tags(text)   
    text = convert_emojis_to_text(text) 
    text = ' '.join([word for word in word_tokenize(text) if word not in nltk.corpus.stopwords.words('english')])  # Remove stopwords and tokenize
    return text

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review_text = request.form['review']
        processed_text = preprocess_text(review_text)
        
        # Check if the processed text has at least 50 words
        if len(processed_text.split()) < 50:
            return render_template('index.html', error_message="Please enter a review with at least 50 words.")
        
        prediction = pipeline.predict([processed_text])[0]
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
