import unittest
from ciphertext import *


class ciphertextTest(unittest.TestCase):
    """Tests for ciphertext.py"""
    def test1(self):
	self.assertEqual(repr(ciphertext("Hello!")), "HELLO")


    def test2(self):
	self.assertEqual(ciphertext("Hello!").occurences(), {'A': 0, 'C': 0, 'B': 0, 'E': 1, 'D': 0, 'G': 0, 'F': 0, 'I': 0, 'H': 1, 'K': 0, 'J': 0, 'M': 0, 'L': 2, 'O': 1, 'N': 0, 'Q': 0, 'P': 0, 'S': 0, 'R': 0, 'U': 0, 'T': 0, 'W': 0, 'V': 0, 'Y': 0, 'X': 0, 'Z': 0})

    def test3(self):
	self.assertEqual(ciphertext("Hello!").nocc(2), {'EL': 1, 'LL': 1, 'LO': 1, 'HE': 1})

    def test4(self):
	self.assertEqual(ciphertext("Hello!").frequency(), {'W': 0.0, 'E': 0.2, 'Z': 0.0, 'L': 0.4, 'J': 0.0, 'Y': 0.0, 'A': 0.0, 'U': 0.0, 'P': 0.0, 'T': 0.0, 'Q': 0.0, 'I': 0.0, 'S': 0.0, 'N': 0.0, 'K': 0.0, 'R': 0.0, 'G': 0.0, 'H': 0.2, 'D': 0.0, 'V': 0.0, 'X': 0.0, 'M': 0.0, 'O': 0.2, 'C': 0.0, 'F': 0.0, 'B': 0.0}
)
if __name__ == '__main__':
    unittest.main()

