from enum import Enum

class EncodingMode(Enum):
    NUMERIC = 0b0001
    ALPHANUMERIC = 0b0010
    BINARY = 0b0100
    KANJI = 0b1000
    ECI = 0b0111