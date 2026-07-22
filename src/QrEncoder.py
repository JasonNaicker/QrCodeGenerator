from typing import Optional, Final, TypeAlias, Generic
from src.Enums.ErrorCorrection import ErrorCorrection

QrInput : TypeAlias = str
QrMatrix : TypeAlias = list[list[int]]
BitStream : TypeAlias = list[int]

class QrEncoder():
    __slots__ = ("data", "error_correction", "version")
    def __init__(self, data : QrInput, error_correction : ErrorCorrection, version : int = 1) -> None:
        self.data = data
        self.error_correction = error_correction
        self.version = version

        if not isinstance(self.data, str):
            raise TypeError("Input data is not a string")

    def _encode_data(self) -> BitStream:
        encoded : BitStream = [0] * len(self.data)
        for c in self.data:
            encoded.append[format(c, "b")]

    def _error_correction(self) -> BitStream:
        pass

    def _place_modules(self) -> QrMatrix:
        pass

    def _apply_mask(self) -> QrMatrix:
        pass
    
    def encode(self) -> QrMatrix:
        pass