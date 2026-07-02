from enum import Enum
from objects.phones import Phone

vowel_list = ["A", "E", "I", "O", "U"]

class Vowel(Phone):
    def __init__(self, arpa: str, is_stressed):
         super().__init__(arpa)
         self.is_stressed = is_stressed
         self.lexical_set = ""