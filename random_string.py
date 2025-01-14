import string
import random

class RandomName:
    def randomStringGenerator():
        res = ''.join(random.choices(string.ascii_letters,k=7))
        return res
