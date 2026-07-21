from typing import Optional, Final, TypeAlias, Generic

QrInput : TypeAlias = str
QrMatrix : TypeAlias = list[list[int]]
class QrEncoder():
    __slots__ = ("data")
    def __init__(self, data : QrInput) -> None:
        self.data = data

    def _encode_data() -> None:
        pass

    def _error_correction() -> None:
        pass

    def _place_modules() -> None:
        pass

    def _apply_mask() -> None:
        pass
    
    def encode(self) -> QrMatrix:
        pass