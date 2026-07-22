from src.Enums.ErrorCorrection import ErrorCorrectionMode

BitStream = list[int]

class ReedSolomon:

    __slots__ = ("error_correction_mode",)

    def __init__(self, error_correction_mode: ErrorCorrectionMode) -> None:
        self.error_correction_mode = error_correction_mode

    def generate(self, data: BitStream) -> BitStream:
        """
        Generate Reed-Solomon error correction bytes
        """

        # TODO:
        # Actual Reed-Solomon implementation

        return data