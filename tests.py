import unittest
import task
import random
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        r = random.randint(1, 100)
        area = math.pi*(r*r)
        self.assertEqual(area, task.circlearea(r))


if __name__ == '__main__':
    unittest.main()
