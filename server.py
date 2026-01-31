"""
Flask server for Emotion Detection application.
Provides routes to analyze text emotions using Watson NLP.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotion of the input text provided as a query parameter.
    Returns formatted emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotion_scores = {
        key: val
        for key, val in response.items()
        if key != 'dominant_emotion'
    }

    return (
        "For the given statement, the system response is "
        + ", ".join(f"'{k}': {v}" for k, v in emotion_scores.items())
        + f". The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
