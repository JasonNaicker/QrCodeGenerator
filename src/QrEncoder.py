from typing import TypeAlias
from dataclasses import dataclass
from src.Enums.ErrorCorrection import ErrorCorrectionMode
from src.Enums.EncodingMode import EncodingMode
from src.ReedSolomon import ReedSolomon
from src.Matrix import QrMatrix, QrMatrixBuilder
from src.QrVersionInfo import QR_VERSION_INFO, VersionInfo

QrInput: TypeAlias = str
BitStream: TypeAlias = list[int]

@dataclass(slots=True)
class EncodedData():
    bits: BitStream
    character_count : int
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
        self.data_codward_size : int = self._get_data_codewards() * 8
        self.character_count_bits  : int = self._get_character_count_bits()

        if not isinstance(self.input_data, str):
            raise TypeError("Input data is not a string")

        if self.version < 1 or self.version > 40:
            raise ValueError("Version must be between 1-40")
        
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

    def _get_version_info(self) -> VersionInfo:
        return QR_VERSION_INFO[self.version][self.error_correction_mode]

    def _get_data_codewards(self) -> int:
        versionInfo : VersionInfo = self._get_version_info()
        return versionInfo.data_codewords

    def _encode_byte_data(self) -> EncodedData:
        encoded_bytes = self.input_data.encode("utf-8")

        bits: BitStream = []
        for byte in encoded_bytes:
            bits.extend(int(bit) for bit in f"{byte:08b}")
        return EncodedData(bits=bits, character_count=len(encoded_bytes))

    def _encode_numeric_data(self) -> EncodedData:
        pass

    def _encode_alphanumeric_data(self) -> EncodedData:
        pass
    
    def _encode_kanji_data(self) -> EncodedData:
        encoded_bytes = self.input_data.encode("shift-jis")
    
        bits: BitStream = []
        for byte in encoded_bytes:
            bits.extend(int(bit) for bit in f"{byte:08b}")
        return EncodedData(bits=bits, character_count=len(encoded_bytes))

    def _encode_data(self) -> EncodedData:
        if self.encoding_mode == EncodingMode.BINARY:
                return self._encode_byte_data()
        elif self.encoding_mode == EncodingMode.NUMERIC:
                return self._encode_numeric_data()
        elif self.encoding_mode == EncodingMode.ALPHANUMERIC:
            return self._encode_alphanumeric_data()
        elif self.encoding_mode == EncodingMode.KANJI:
            return self._encode_kanji_data()

        raise ValueError("Unsupported Encoding")

    def _add_metadata(self, encoded: EncodedData) -> BitStream:
        """
        Add:
        - mode indicator
        - character count
        """

        # TODO:
        # Add encoding mode bits
        # Add character count bits
        result: BitStream = []

        result.extend(int(b) for b in f"{self.encoding_mode.value:04b}") #Encoding Mode Bits
        result.extend(int(b) for b in f"{encoded.character_count:0{self.character_count_bits}b}") #Character count Bits
        result.extend(encoded.bits) #Data Bits

        return result

    def _add_terminator(self, data: BitStream) -> BitStream:
        for i in range(max((len(data) - self.data_codward_size), 4)):
            data.extend(int(0)) #Terminator Bits

    def _pad_data(self, data: BitStream) -> BitStream:
        remainder = len(data) % 8

        if remainder:
            data.extend([0] * (8 - remainder))

        return data

    def _add_mask(self, data: BitStream) -> BitStream:
        current_size : int = len(data)
        remaining_codeward_space : int = (self.data_codward_size - current_size) // 8

        first_mask = format(236, '08b')
        second_mask = format(17, '08b')

        for i in range(remaining_codeward_space):
            match (i % 2):
                case 0:
                    data.extend(int(b) for b in first_mask)
                case 1:
                    data.extend(int(b) for b in second_mask)

        return data

    def encode(self) -> QrMatrix:
        bits = self._encode_data()
        bits = self._add_metadata(bits)
        bits = self._add_terminator(bits)
        bits = self._pad_data(bits)
        bits = self._add_mask(bits)
        bits = self.reed_solomon.generate(bits)
        matrix = self.matrix_builder.place_modules(bits)
        return matrix