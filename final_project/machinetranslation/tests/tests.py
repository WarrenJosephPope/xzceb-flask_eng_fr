"""
This module tests the translation of text from English to French
and vice versa
"""
import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    This class tests the translation
    of English text to French
    """
    def test1(self):
        """
        This method checks if the French translation
        of the English text is correct or not
        """
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """
    This class tests the translation
    of French text to English
    """
    def test1(self):
        """
        This method checks if the English translation
        of the French text is correct or not
        """
        self.assertEqual(french_to_english(' '), ' ')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
