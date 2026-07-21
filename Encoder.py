from typing import Optional, Final, TypeAlias, Generic

QrInput : TypeAlias = str

class QrEncoder():
    __slots__ = ("input")
    def __init__(self, input : QrInput) -> None:
        self.input = input
    
    def encode(self) -> str:
        pass
    
    