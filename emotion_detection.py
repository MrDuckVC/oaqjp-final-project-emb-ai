import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze the emotion of the given text using Watson NLP Emotion Predict service
    and return formatted output with dominant emotion
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # URL and headers for the Watson NLP service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Input data format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Send POST request to the Watson NLP service
        response = requests.post(url, headers=headers, json=input_json)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            
            # Extract emotion scores from the response
            emotions = result['emotionPredictions'][0]['emotion']
            
            # Format the output as required
            formatted_output = {
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness']
            }
            
            # Find the dominant emotion (emotion with highest score)
            dominant_emotion = max(formatted_output.items(), key=lambda x: x[1])[0]
            formatted_output['dominant_emotion'] = dominant_emotion
            
            return formatted_output
            
        else:
            # Return error information if request failed
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
    except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError, IndexError) as e:
        # Return None values for all emotions in case of any error
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
