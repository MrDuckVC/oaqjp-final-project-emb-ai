import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze the emotion of the given text using Watson NLP Emotion Predict service
    """
    if not text_to_analyze.strip():
        return None
    
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
            # Parse the JSON response and return the text attribute
            result = response.json()
            return result
        else:
            # Return error information if request failed
            return {
                'error': f'Request failed with status code {response.status_code}',
                'status_code': response.status_code
            }
            
    except requests.exceptions.RequestException as e:
        return {'error': f'Request exception: {str(e)}'}
    except json.JSONDecodeError as e:
        return {'error': f'JSON decode error: {str(e)}'}
