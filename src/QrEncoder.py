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

    def _get_character_count(self) -> int:
        if self.encoding_mode == EncodingMode.BINARY:
            return len(self.input_data.encode("utf-8"))

        elif self.encoding_mode == EncodingMode.NUMERIC:
            return len(self.input_data)

        elif self.encoding_mode == EncodingMode.ALPHANUMERIC:
            return len(self.input_data)

        elif self.encoding_mode == EncodingMode.KANJI:
            return len(self.input_data)

        raise ValueError("Unsupported encoding mode")

    def _get_character_count_bits(self) -> int:
        if self.version <= 9:
            table = {
                EncodingMode.NUMERIC: 10,
                EncodingMode.ALPHANUMERIC: 9,
                EncodingMode.BINARY: 8,
                EncodingMode.KANJI: 8,
            }
        elif self.version <= 26:
            table = {
                EncodingMode.NUMERIC: 12,
                EncodingMode.ALPHANUMERIC: 11,
                EncodingMode.BINARY: 16,
                EncodingMode.KANJI: 10,
            }
        else:
            table = {
                EncodingMode.NUMERIC: 14,
                EncodingMode.ALPHANUMERIC: 13,
                EncodingMode.BINARY: 16,
                EncodingMode.KANJI: 12,
            }
        return table[self.encoding_mode]

    def _encode_byte_data(self) -> BitStream:
        """
        Convert UTF-8 bytes into bits
        """

        encoded: BitStream = []
        for byte in self.input_data.encode("utf-8"):
            encoded.extend(int(bit) for bit in f"{byte:08b}")
        return encoded

    def _encode_numeric_data(self) -> BitStream:
        pass

    def _encode_alphanumeric_data(self) -> BitStream:
        pass
    
    def _encode_kanji_data(self) -> BitStream:
        pass

    def _encode_data(self) -> BitStream:
        if self.encoding_mode == EncodingMode.BINARY:
                return self._encode_byte_data()
        elif self.encoding_mode == EncodingMode.NUMERIC:
                return self._encode_numeric_data()
        elif self.encoding_mode == EncodingMode.ALPHANUMERIC:
            return self._encode_alphanumeric_data()
        elif self.encoding_mode == EncodingMode.KANJI:
            return self._encode_kanji_data()

        raise ValueError("Unsupported Encoding")

    def _add_metadata(self, data: BitStream) -> BitStream:
        """
        Add:
        - mode indicator
        - character count
        """

        # TODO:
        # Add encoding mode bits
        # Add character count bits
        encoded: BitStream = []

        count = self._get_character_count_bits()
        count_bits = self._get_character_count_bits()

        encoded.extend(int(b) for b in f"{self.encoding_mode.value:04b}")
        encoded.extend(int(b) for b in f"{count:0{count_bits}b}")
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