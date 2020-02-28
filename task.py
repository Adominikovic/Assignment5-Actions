import math
import datetime


def firstrun():
    return "success"


def circlearea(r):
    return math.pi*(r**2)


def firstandlast(some_list):
    return [some_list[0], some_list[-1]]


def numdays(date1, date2):
    return (date1-date2).days
