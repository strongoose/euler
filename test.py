import unittest
import os
import glob

import p001, p002, p003, p004, p005, p006, p007, p008, p009, p010
import p011, p012

ANSWERS = {'001': 233168,
           '002': 4613732,
           '003': 6857,
           '004': 906609,
           '005': 232792560,
           '006': 25164150,
           '007': 104743,
           '008': 23514624000,
           '009': 31875000,
           '010': 142913828922,
           '011': 70600674,
           '012': 76576500,
          }

class AnswerTests(unittest.TestCase):

    def test_001(self):
        self.assertEqual(p001.solve(), ANSWERS['001'])

    def test_002(self):
        self.assertEqual(p002.solve(), ANSWERS['002'])

    def test_003(self):
        self.assertEqual(p003.solve(), ANSWERS['003'])

    def test_004(self):
        self.assertEqual(p004.solve(), ANSWERS['004'])

    def test_005(self):
        self.assertEqual(p005.solve(), ANSWERS['005'])

    def test_006(self):
        self.assertEqual(p006.solve(), ANSWERS['006'])

    def test_007(self):
        self.assertEqual(p007.solve(), ANSWERS['007'])

    def test_008(self):
        self.assertEqual(p008.solve(), ANSWERS['008'])

    def test_009(self):
        self.assertEqual(p009.solve(), ANSWERS['009'])

    def test_010(self):
        self.assertEqual(p010.solve(), ANSWERS['010'])

    def test_011(self):
        self.assertEqual(p011.solve(), ANSWERS['011'])

    def test_012(self):
        self.assertEqual(p012.solve(), ANSWERS['012'])
