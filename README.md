# NLP - Emotion Detection Web Application

This project is a fully functional web application designed to analyze text and detect the underlying emotions.

It was developed and submitted as the Capstone Project for the **IBM AI Developer** Professional Certificate.

## 📝 About the Project

The application provides a user-friendly interface where users can input any text. Clicking the button triggers an asynchronous call to the server, which in turn queries the powerful **IBM Watson NLP (Emotion Predict)** cloud model.

The system evaluates the text across five basic emotions:

* 😡 Anger
* 🤢 Disgust
* 😨 Fear
* 😄 Joy
* 😢 Sadness

After the analysis, the application automatically determines and displays the **dominant emotion**, dynamically updating the page without reloading.

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **API Integration:** `requests` library for HTTP calls
* **AI Model:** IBM Watson NLP
* **Frontend:** HTML5, Vanilla JavaScript (AJAX / XMLHttpRequest), Bootstrap 4.3.1 CSS framework
* **Quality Assurance:** `unittest` library for unit testing
* **Web Server:** Built-in Flask development server

## 📁 Repository Structure

* `server.py` — The main application file containing Flask routing logic (`/` and `/emotionDetector`).
* `EmotionDetection/` — A Python package containing the core business logic:
  * `emotion_detection.py` — Script for integrating with the Watson NLP API, parsing the JSON response, and handling errors.
* `templates/index.html` — The frontend user interface.
* `static/mywebscript.js` — Client-side script for handling button clicks and asynchronous DOM updates.
* `test_emotion_detection.py` — A suite of unit tests to verify the accuracy of the emotion analyzer.

## 🚀 How to Run Locally

1. **Clone the repository:**

    ```bash
    git clone <your_repository_link>
    cd oaqjp-final-project-emb-ai
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # For Linux/macOS
    # or
    .venv\Scripts\activate     # For Windows
    ```

3. **Install dependencies:**
    *(Make sure you have Flask and requests installed)*

    ```bash
    pip install flask requests
    ```

4. **Start the server:**

    ```bash
    python server.py
    ```

5. **Open the application:**
    Navigate to `http://localhost:5000` in your web browser.

## 🧪 Running Tests

To verify the correctness of the emotion detection algorithm, run the following command in the root directory of the project:

```bash
python test_emotion_detection.py
````

## 🎓 About the Author

**Author:** Valentin Cunev
I am a student, and I successfully completed this project and the 10-course IBM Skills Network specialization while juggling my university studies and preparing for my exam tomorrow\!

## 📄 License

This project is licensed under the [Apache License 2.0](https://www.google.com/search?q=LICENSE). Copyright 2020 IBM Developer Skills Network.
