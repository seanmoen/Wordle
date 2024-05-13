#Sean Moen
#May 19, 2023
#Test cases for wordlesolver

#https://www.dataquest.io/blog/unit-tests-python/

#Run with command:
#python3 -m unittest -v

import unittest
from wordle_solver import evaluate_word

class TestClass(unittest.TestCase):
    def test_green_singular(self):
        word_list = ["chale", "trees", "tests", "waste", "plans"]
        word = "prays"
        colors = ["Gray", "Gray", "Green", "Gray", "Gray"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["chale"])

    def test_yellow_singular(self):
        word_list = ["chale", "trees", "tests", "waste", "plans"]
        word = "watch"
        colors = ["Gray", "Yellow", "Gray", "Gray", "Gray"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["plans"])

    def test_gray_singular(self):
        word_list = ["chale", "trees", "tests", "waste", "plans", "plant"]
        word = "plans"
        colors = ["Green", "Green", "Green", "Green", "Gray"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["plant"])

    def test_green_multiple(self):
        word_list = ["chale", "trees", "tests", "waste", "plans", "watch"]
        word = "watch"
        colors = ["Green", "Green", "Green", "Green", "Green"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["watch"])

    def test_yellow_multiple(self):
        word_list = ["chale", "trees", "tests", "waste", "plans", "watch", "haste"]
        word = "shaet"
        colors = ["Yellow", "Yellow", "Yellow", "Yellow", "Yellow"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["haste"])

    def test_gray_multiple(self):
        word_list = ["chale", "trees", "tests", "waste", "plans", "watch", "haste"]
        word = "quick"
        colors = ["Gray", "Gray", "Gray", "Gray", "Gray"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["trees", "tests", "waste", "plans", "haste"])

    def test_green_and_gray(self):
        word_list = [ "haste", "cacao", "cream"]
        word = "cacao"
        colors = ["Green", "Gray", "Gray", "Green", "Gray"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["cream"])

    def test_yellow_and_gray(self):
        word_list = ["haste", "cacao", "cream", "echla"]
        word = "cacao"
        colors = ["Yellow", "Gray", "Gray", "Yellow", "Gray"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["echla"])

    def test_green_yellow_gray(self):
        word_list = ["haste", "cacao", "cream", "echla", "laece"]
        word = "eerie"
        colors = ["Yellow", "Gray", "Gray", "Gray", "Green"]
        evaluate_word(word, colors, word_list)
        self.assertEqual(word_list, ["laece"])

        

if __name__ == '__main__':
    unittest.main()