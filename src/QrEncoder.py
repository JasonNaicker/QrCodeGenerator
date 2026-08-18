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
        "matrix_builder", 
        "data_codeword_size",
        "character_count_bits",
        "encoded_data")

    def __init__(
        self,
        input_data: QrInput,
        encoding_mode: EncodingMode | None = None,
        error_correction_mode: ErrorCorrectionMode = ErrorCorrectionMode.HIGH,
        version: int | None = None) -> None:

        if not isinstance(input_data, str):
            raise TypeError("Input data is not a string")

        if version is not None and not 1 <= version <= 40:
            raise ValueError("Version must be between 1-40")
        
        self.input_data = input_data
        self.error_correction_mode = self.error_correction_mode
        self.encoding_mode = (self._detect_encoding_mode() if encoding_mode is None else encoding_mode)
        self.encoded_data : EncodedData = self._encode_data()
        self.version = (self._calculate_version() if version is None else version)

        self.data_codeword_size : int = self._get_data_codewords() * 8
        self.character_count_bits  : int = self._get_character_count_bits(self.version)

        self.reed_solomon = ReedSolomon(self.error_correction_mode)
        self.matrix_builder = QrMatrixBuilder(self.version)
        
    def _get_character_count_bits(self, version : int) -> int:
        if version <= 9:
            table = {
                EncodingMode.NUMERIC: 10,
                EncodingMode.ALPHANUMERIC: 9,
                EncodingMode.BINARY: 8,
                EncodingMode.KANJI: 8,
            }
        elif version <= 26:
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

    def _get_version_info(self, version : int) -> VersionInfo:
        return QR_VERSION_INFO[version][self.error_correction_mode]

    def _get_data_codewords(self) -> int:
        version_info : VersionInfo = self._get_version_info(self.version)
        return version_info.data_codewords

    def _calculate_version(self) -> int:
        for version in range(1, 41):
            character_count_bits = self._get_character_count_bits(version)

            required_bits = (4 + character_count_bits + len(self.encoded_data.bits))

            capacity_bits = (self._get_version_info(version).data_codewords * 8)

            if required_bits <= capacity_bits:
                return version

        raise ValueError("Input data is too big for QR Code")
    
    def _encode_byte_data(self) -> EncodedData:
        encoded_bytes = self.input_data.encode("utf-8")

        bits: BitStream = []
        for byte in encoded_bytes:
            bits.extend(int(bit) for bit in f"{byte:08b}")
        return EncodedData(bits=bits, character_count=len(encoded_bytes))

    def _encode_numeric_data(self) -> EncodedData:
        bits: BitStream = []

        for i in range(0, len(self.input_data), 3):
            group = self.input_data[i:i + 3]

            if len(group) == 3:
                bit_count = 10
            elif len(group) == 2:
                bit_count = 7
            else:
                bit_count = 4

            value = int(group)
            bits.extend(int(b) for b in f"{value:0{bit_count}b}")

        return EncodedData(
            bits=bits,
            character_count=len(self.input_data))

    @staticmethod
    def _alphanumeric_value(c: str) -> int:
        ALPHANUMERIC_CHARS : str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
        value = ALPHANUMERIC_CHARS.find(c)

        if value == -1:
            raise ValueError(f"Invalid alphanumeric character: {c!r}")

        return value
            
    def _encode_alphanumeric_data(self) -> EncodedData:

            bits: BitStream = []
        
            for i in range(0, len(self.input_data), 2):
                group = self.input_data[i : i + 2]

                if len(group) == 2:
                    value = int((self._alphanumeric_value(group[0]) * 45) + self._alphanumeric_value(group[1]))
                    bit_count = 11
                else:
                    value = int((self._alphanumeric_value(group[0])))
                    bit_count = 6

                bits.extend(int(b) for b in f"{value:0{bit_count}b}")

            return EncodedData(
                bits=bits,
                character_count=len(self.input_data))

    def _can_encode_as_kanji(self) -> bool:
        for c in self.input_data:
            try:
                encoded = c.encode("shift-jis")
            except UnicodeEncodeError:
                return False

            if len(encoded) != 2:
                return False

            value = (encoded[0] << 8) | encoded[1]

            if not (0x8140 <= value <= 0x9FFC or 0xE040 <= value <= 0xEBBF):
                return False

        return True

    def _encode_kanji_data(self) -> EncodedData:
        bits: BitStream = []
        for c in self.input_data:
            encoded = c.encode("shift-jis") 

            if len(encoded) != 2: 
                raise ValueError(f"Character {c!r} cannot be encoded using QR Kanji mode")
            
            value = (encoded[0] << 8) | encoded[1]
            if 0x8140 <= value <= 0x9FFC:
                value -= 0x8140
            elif 0xE040 <= value <= 0xEBBF:
                value -= 0xC140
            else:
                raise ValueError(f"Character {c!r} cannot encode data using kanji mode")

            high = value >> 8
            low = value & 0xFF

            encoded_value = (high * 0xC0) + low
            bits.extend(int(b) for b in f"{encoded_value:013b}")

        return EncodedData(bits=bits, character_count=len(self.input_data))
    
    def _detect_encoding_mode(self) -> EncodingMode:
        if self.input_data == "":
            return EncodingMode.BINARY
        
        if self.input_data.isdigit():
            return EncodingMode.NUMERIC

        if all(self._alphanumeric_value(c) != -1 for c in self.input_data):
            return EncodingMode.ALPHANUMERIC

        if self._can_encode_as_kanji():
            return EncodingMode.KANJI

        return EncodingMode.BINARY

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
        result: BitStream = []

        result.extend(int(b) for b in f"{self.encoding_mode.value:04b}") #Encoding Mode Bits
        result.extend(int(b) for b in f"{encoded.character_count:0{self.character_count_bits}b}") #Character count Bits
        result.extend(encoded.bits) #Data Bits

        return result

    def _add_terminator(self, data: BitStream) -> BitStream:
        remaining = self.data_codeword_size - len(data)
        terminator_size = min(remaining, 4)

        data.extend([0] * terminator_size)

        return data

    def _pad_data(self, data: BitStream) -> BitStream:
        remainder : int = len(data) % 8

        if remainder:
            data.extend([0] * (8 - remainder))

        return data

    def _add_pad_codewords(self, data: BitStream) -> BitStream:
        remaining : int = self.data_codeword_size - len(data)

        pad_codwards = (0xEC, 0x11)

        for i in range(0, remaining, 8):
            value = pad_codwards[(i // 8) % 2]
            data.extend(int(b) for b in f"{value:08b}")

        return data

    def encode(self) -> QrMatrix:
        bits = self._add_metadata(self._encoded_data)
        bits = self._add_terminator(bits)
        bits = self._pad_data(bits)
        bits = self._add_pad_codewords(bits)
        assert len(bits) == self.data_codeword_size
        bits = self.reed_solomon.generate(bits)
        print(bits)
        matrix = self.matrix_builder.place_modules(bits)
        return matrix