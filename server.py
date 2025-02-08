''' Emotion detector that receives text and responds with the detected emotion
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def em_detector():
    '''Receives text to analyze and responds with a score for various emotions and
    identifies the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    output = "For the given statement, the system response is 'anger': "
    output += str(result['anger']) + ", 'disgust': " + str(result['disgust'])
    output += ", 'fear': " + str(result['fear']) + ", 'joy': "
    output += str(result['joy']) + " and 'sadness': " + str(result['sadness'])
    output += ". The dominant emotion is " + result['dominant_emotion'] + "."
    return output

@app.route('/')
def render_index_page():
    '''Renders the main index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
