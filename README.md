# Sentiment Analysis Web Application

This is a simple web application built with Flask for performing sentiment analysis on text reviews. Users can input their text reviews, and the application predicts whether the sentiment of the review is positive or negative.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AbhishekT-2002/sentiment_analysis_flask_app
    ```

2. Navigate to the project directory:

    ```bash
    cd sentiment-analysis-flask-app
    ```

3. Install the dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

3. Enter your text review in the input field and click the "Submit" button.

4. The application will display the predicted sentiment of the review.

## Project Structure

- `app.py`: Contains the Flask application code including routes and model loading.
- `model.joblib`: Pre-trained pipeline model for sentiment analysis.
- `requirements.txt`: File containing the list of Python dependencies required for the project.
- `templates/`: Directory containing HTML templates for the web application.

## Dependencies

The project relies on the following Python libraries:

- Flask
- nltk
- scikit-learn
- emoji
- BeautifulSoup

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
