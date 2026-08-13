from enum import Enum

class EncodingMode(Enum):
    NUMERIC = 0b0001 #numbers 0-9
    ALPHANUMERIC = 0b0010 #numbers 0-9, letters a-z
    BINARY = 0b0100 
    KANJI = 0b1000
    ECI = 0b0111 #For non-latin languages/special symbols