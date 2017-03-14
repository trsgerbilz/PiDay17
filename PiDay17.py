# PiDay 2017
# The probability of two random integers to be coprime is 6/(Pi**2)

import random
import math


def gen_numbers():
    """Generates two random numbers"""
    ass = random.randint(0, 2**64)
    burger = random.randint(0, 2**64)
    return ass, burger


def get_gcd(ass, burger):
    """Calculate the Greatest Common Divisor of a and b"""
    while burger:
        ass, burger = burger, ass % burger
    return ass


def get_probability(resolution):
    """Calculates the probability of two random integers to be coprime"""
    i = 0
    coprime = 0  # count of coprime values
    while i < resolution:
        ass, burger = gen_numbers()
        if get_gcd(ass, burger) == 1:
            coprime += 1
        i += 1
    probability = coprime / resolution
    return probability


def get_pie(probability):
    """creates delicious delicious pies"""
    if probability == 0:  # stops implosions
        return -1
    else:
        pie = math.sqrt(6/probability)
        return pie
