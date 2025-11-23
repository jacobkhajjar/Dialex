from enum import Enum
from objects.phones import Phone
from config.fx import *

vowel_list = ["A", "E", "I", "O", "U"]

class Vowel(Phone):
    def __init__(self, arpa: str, fx: str, is_stressed):
         super().__init__(arpa, fx)
         self.is_stressed = is_stressed

    # prints unstressed vowels in lowercase
    def __repr__(self):
        if not self.is_stressed:
            return self.fx.lower()
        return self.fx