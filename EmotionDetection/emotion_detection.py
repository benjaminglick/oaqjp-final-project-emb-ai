import requests
import json
def emotion_detector(text_to_analyze):
    # URL for Emotion API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # JSON payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)
    # Parse the JSON response into dict
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        # Get Emotion Scores
        emotion_predictions = formatted_response['emotionPredictions'][0]
        anger_score = emotion_predictions['emotion']['anger']
        disgust_score = emotion_predictions['emotion']['disgust']
        fear_score = emotion_predictions['emotion']['fear']
        joy_score = emotion_predictions['emotion']['joy']
        sadness_score = emotion_predictions['emotion']['sadness']
        # Structure Response
        emotion_obj =  {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        }
        # Determine dominant emotion    
        highest_score = 0
        dominant_emotion = ''
        for key in emotion_obj.keys():
            if emotion_obj[key] > highest_score:
                dominant_emotion = key
                highest_score = emotion_obj[key]
        emotion_obj['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
       emotion_obj =  {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        } 
    return emotion_obj
