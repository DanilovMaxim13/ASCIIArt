import unittest
import os.path

from Main import main

correct_ansiArt = "[41m[31m&[0m[41m[31m&[0m[41m[31m&[0m" \
                  "[41m[31m&[0m[41m[31m&[0m[41m[31m&[0m" \
                  "[41m[31m&[0m[41m[31m&[0m[41m[31m&[0m" \
                  "[41m[31m&[0m[41m[31m&[0m[41m[31m&[0m" \
                  "[41m[31m&[0m[41m[31m&[0m[41m[31m&[0m" \
                  "[41m[31m$[0m[41m[31m$[0m[41m[31m$[0m" \
                  "[41m[31m$[0m[41m[31m$[0m[41m[31m$[0m" \
                  "[41m[31m$[0m[41m[31m$[0m[41m[31m$[0m" \
                  "[41m[31m$[0m[41m[31m$[0m[41m[31m$[0m" \
                  "[41m[31m$[0m[41m[31m$[0m[43m[33m![0m" \
                  "[43m[33m:[0m[43m[33m:[0m[43m[33m:[0m" \
                  "[43m[33m:[0m[43m[33m:[0m[43m[33m:[0m" \
                  "[43m[33m:[0m[43m[33m:[0m[43m[33m:[0m" \
                  "[43m[33m:[0m[43m[33m:[0m[43m[33m:[0m" \
                  "[43m[33m:[0m[43m[33m:[0m[42m[32m&[0m" \
                  "[42m[32m&[0m[42m[32m&[0m[42m[32m&[0m" \
                  "[42m[32m&[0m[42m[32m&[0m[42m[32m&[0m" \
                  "[42m[32m&[0m[42m[32m&[0m[42m[32m&[0m" \
                  "[42m[32m&[0m[42m[32m&[0m[42m[32m&[0m" \
                  "[42m[32m&[0m[42m[32m&[0m[46m[36m%[0m" \
                  "[46m[36m%[0m[46m[36m%[0m[46m[36m%[0m" \
                  "[46m[36m%[0m[46m[36m%[0m[46m[36m%[0m" \
                  "[46m[36m%[0m[46m[36m%[0m[46m[36m%[0m" \
                  "[46m[36m%[0m[46m[36m%[0m[46m[36m%[0m" \
                  "[46m[36m%[0m[46m[36m%[0m[44m[34m#[0m" \
                  "[44m[34m#[0m[44m[34m#[0m[44m[34m#[0m" \
                  "[44m[34m#[0m[44m[34m#[0m[44m[34m#[0m" \
                  "[44m[34m#[0m[44m[34m#[0m[44m[34m#[0m" \
                  "[44m[34m#[0m[44m[34m#[0m[44m[34m#[0m" \
                  "[44m[34m#[0m[45m[35m&[0m[45m[35m&[0m" \
                  "[45m[35m&[0m[45m[35m&[0m[45m[35m&[0m" \
                  "[45m[35m&[0m[45m[35m&[0m[45m[35m&[0m" \
                  "[45m[35m&[0m[45m[35m&[0m[45m[35m&[0m[47m[37m:[0m"


class TestAllMethods(unittest.TestCase):
    def test_ascii(self):
        main("test_ascii.jpg", 100, 1)
        correct_asciiArt = "BBBBBBBBBBBBBBBBBBBBBBBSSSSSSS#######&&&&&&" \
                           "@@@@@@$$$$$$%%%%%%*******!!!!!!!:::::::::::" \
                           ".............."
        f = open("ascii_img.txt", 'r')
        self.assertEqual(correct_asciiArt, f.read())

    def test_ansi(self):
        main("raduga.jpg", 100, 2)
        f = open("ascii_img.txt", 'r')
        self.assertEqual(correct_ansiArt, f.read())

    def test_asciirefact(self):
        main("raduga.jpg", 100, 3)
        self.assertTrue(os.path.exists("content.png"))

    def test_unexect_type(self):
        main("raduga.jpg", 100, 4)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
