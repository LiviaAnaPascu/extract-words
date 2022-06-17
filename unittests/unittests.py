import os
import unittest

from python import formatWhatsappTexts as format
from collections import Counter

testDir = os.path.join(os.getcwd(), "unittests", "conversations")
testUser = "Gita Pressley"
testOutput = "testOutput.csv"

class TestFormatTexts(unittest.TestCase):

#make sure it finds dir
#make sure it finds file from dir
#make sure it finds multiple files
#make sure it gets correct username
#make sure is more than one word
#make sure it gets count of each word
#make sure it doesn't include symbols/emojis/links/names
#make sure it csv file gets created corectly

    def testEmptyDir(self):
        with self.assertWarns(UserWarning):
            format.getChatFiles("")
    
    def testWrongDir(self):
        cwd = os.getcwd()
        with self.assertWarns(UserWarning):
            format.getChatFiles(cwd)
        
    def testCorrectDir(self):
        files = format.getChatFiles(testDir)
        self.assertIsNotNone(files)
        self.assertEqual(2, len(files))

    def testEmptyUser(self):
        with self.assertWarns(UserWarning):
            format.extract(testDir, "")
            
    def testExtractWords(self):
        words = format.extract(testDir, testUser)
        self.assertIsNot(0, len(words))

    def testCorrectCount(self):
        words = format.extract(testDir, testUser)
        wordCount = Counter(words)
        self.assertEquals(0, wordCount['cake'])
        self.assertEquals(1, wordCount['park'])
        self.assertEquals(2, wordCount['he'])

    def testEmojisAndCo(self):
        words = format.extract(testDir, testUser)
        self.assertTrue("🐵" not in words)
        self.assertTrue(":O" not in words)
        self.assertTrue("400" not in words)

    def testFormat(self):
        out = os.path.join(os.getcwd(), testOutput)
        format.writeCSV(testDir, testOutput, testUser)
        self.assertTrue(os.path.exists(out))
