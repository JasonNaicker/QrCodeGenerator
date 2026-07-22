from typing import TypeAlias

QrMatrix: TypeAlias = list[list[int]]
BitStream: TypeAlias = list[int]

class QrMatrixBuilder:

    __slots__ = ("version","size")

    def __init__(self, version: int) -> None:
        self.version = version
        self.size = 21 + (version - 1) * 4

    def create_empty(self) -> QrMatrix:

        return [[0] * self.size for _ in range(self.size)]

    def place_modules(self,data: BitStream) -> QrMatrix:
        matrix = self.create_empty()

        # TODO:
        # add finder patterns
        # add timing patterns
        # zig-zag place data

        return matrix