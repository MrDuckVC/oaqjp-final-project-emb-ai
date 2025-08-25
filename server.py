"""
Flask server for Emotion Detection web application.
This module provides a web interface for analyzing emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render the main index page of the Emotion Detection application.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze emotions in the provided text and return the results.

    Returns:
        str: Formatted response with emotion analysis results or error message.
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    # Analyze the emotion
    result = emotion_detector(text_to_analyze)

    # Check if analysis was successful
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
