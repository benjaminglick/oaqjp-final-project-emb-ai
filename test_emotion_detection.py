from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test emotion: joy
        result1 = emotion_detector('I am glad this happened')
        self.assertEqual(result1['dominant_emotion'],'joy')

        # Test emotion: anger
        result1 = emotion_detector('I am really mad about this')
        self.assertEqual(result1['dominant_emotion'],'anger')

        # Test emotion: disgust
        result1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result1['dominant_emotion'],'disgust')

        # Test emotion: sadness
        result1 = emotion_detector('I am so sad about this')
        self.assertEqual(result1['dominant_emotion'],'sadness')

        # Test emotion: fear
        result1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result1['dominant_emotion'],'fear')

unittest.main()
