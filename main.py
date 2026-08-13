from src.QrEncoder import QrEncoder

if __name__ == "__main__":
    encoder = QrEncoder(input_data="HELLO WORLD")
    result = encoder.encode()
    print(f'Qr Result: \n {result}')