import unittest
import task
import random
import math
import datetime


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

    def test5(self):
        day1 = random.randint(1, 28)
        day2 = random.randint(1, 28)
        month1 = random.randint(1, 12)
        month2 = random.randint(1, 12)
        year1 = random.randint(1900, 2019)
        year2 = random.randint(1900, 2019)
        date1 = datetime.datetime(year1, month1, day1)
        date2 = datetime.datetime(year2, month2, day2)
        days = (date1 - date2).days
        self.assertEqual(days, task.numdays(date1, date2))


if __name__ == '__main__':
    unittest.main()
