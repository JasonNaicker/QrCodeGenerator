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

    def _encode_data() -> BitStream:
        pass

    def _error_correction() -> BitStream:
        pass

    def _place_modules() -> QrMatrix:
        pass

    def _apply_mask() -> QrMatrix:
        pass
    
    def encode(self) -> QrMatrix:
        pass