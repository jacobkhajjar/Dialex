from enum import Enum
from objects.phones import Phone
from config.fx import *

class Action(Enum):
    STOP = "stop-plosive"
    FRICATIVE = "fricative"
    NASAL = "nasal"
    AFFRICATE = "affricate"
    LIQUID = "liquid approximant"
    SEMIVOWEL = "semivowel approximant"

unvoiced = ["CH", "F", "HH", "K", "P", "S", "SH", "T", "TH"]

stops = ["B", "D", "G", "K", "P", "T"]
fricatives = ["DH", "F", "HH", "S", "SH", "TH", "V", "Z", "ZH"]
nasals = ["M", "N", "NG"]
affricates = ["CH", "JH"]
liquids = ["L", "R"]
semivowels = ["W", "Y"]

class Consonant(Phone):
    def __init__(self, arpa: str, fx: str, is_voiced: bool, action: Action):
        super().__init__(arpa, fx)
        self.is_voiced = is_voiced
        self.action = action