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

    def test4(self):
        r = random.randint(2, 100)
        random_list = random.sample(range(0, 100), r)
        first_last = [random_list[0], random_list[-1]]
        self.assertEqual(first_last, task.firstandlast(random_list))


if __name__ == '__main__':
    unittest.main()
