from src.QrEncoder import QrEncoder
from src.Enums.ErrorCorrection import ErrorCorrection

if __name__ == "__main__":
    encoder = QrEncoder(data="Hello", error_correction=ErrorCorrection.MEDIUM)
    result = encoder.encode()
    print(f'Qr Result: \n {result}')