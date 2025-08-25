import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for the emotion_detector function
    """
    
    def test_emotion_detector_joy(self):
        """
        Test that the function correctly identifies 'joy' as dominant emotion
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_anger(self):
        """
        Test that the function correctly identifies 'anger' as dominant emotion
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_disgust(self):
        """
        Test that the function correctly identifies 'disgust' as dominant emotion
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_sadness(self):
        """
        Test that the function correctly identifies 'sadness' as dominant emotion
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_fear(self):
        """
        Test that the function correctly identifies 'fear' as dominant emotion
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()