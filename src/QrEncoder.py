from typing import TypeAlias

from src.Enums.ErrorCorrection import ErrorCorrectionMode
from src.Enums.EncodingMode import EncodingMode
from src.ReedSolomon import ReedSolomon
from src.Matrix import QrMatrix, QrMatrixBuilder

QrInput: TypeAlias = str
BitStream: TypeAlias = list[int]

class QrEncoder:

    __slots__ = (
        "input_data",
        "encoding_mode",
        "error_correction_mode",
        "version",
        "reed_solomon",
        "matrix_builder")

    def __init__(
        self,
        input_data: QrInput,
        encoding_mode: EncodingMode = EncodingMode.BINARY,
        error_correction_mode: ErrorCorrectionMode = ErrorCorrectionMode.HIGH,
        version: int = 1) -> None:

        self.input_data = input_data
        self.encoding_mode = encoding_mode
        self.error_correction_mode = error_correction_mode
        self.version = version

        self.reed_solomon = ReedSolomon(error_correction_mode)

        self.matrix_builder = QrMatrixBuilder(version)

        if not isinstance(self.input_data, str):
            raise TypeError("Input data is not a string")

        if self.version < 1 or self.version > 40:
            raise ValueError("Version must be between 1-40")

    def _encode_data(self) -> BitStream:
        """
        Convert UTF-8 bytes into bits
        """

        encoded: BitStream = []
        for byte in self.input_data.encode("utf-8"):
            encoded.extend(int(bit) for bit in f"{byte:08b}")
        return encoded

    def _add_metadata(self, data: BitStream) -> BitStream:
        """
        Add:
        - mode indicator
        - character count
        """

        encoded: BitStream = []

        # TODO:
        # Add encoding mode bits
        # Add character count bits

        encoded.extend(data)

        return encoded

    def _pad_data(self, data: BitStream) -> BitStream:
        """
        Align bits to byte boundary
        """

        remainder = len(data) % 8

        if remainder:
            data.extend([0] * (8 - remainder))

        return data

    def encode(self) -> QrMatrix:
        bits = self._encode_data()
        bits = self._add_metadata(bits)
        bits = self._pad_data(bits)
        bits = self.reed_solomon.generate(bits)
        matrix = self.matrix_builder.place_modules(bits)
        return matrix

    def generateQrCode(self) -> None:
        _matrix = self.encode()

        #TODO, display/render qr code