import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    res = {
        'anger': formatted_response["emotionPredictions"][0]["emotion"]["anger"],
        'disgust': formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
        'fear': formatted_response["emotionPredictions"][0]["emotion"]["fear"],
        'joy': formatted_response["emotionPredictions"][0]["emotion"]["joy"],
        'sadness': formatted_response["emotionPredictions"][0]["emotion"]["sadness"],
        'dominant_emotion': '',
    }
    dominant = ''
    dominant_score = -1
    for attr, value in formatted_response["emotionPredictions"][0]["emotion"].items():
        if value > dominant_score:
            dominant = attr
            dominant_score = value
    res["dominant_emotion"] = dominant
    return res

    # '{"emotionPredictions":[{"emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."}, "emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'