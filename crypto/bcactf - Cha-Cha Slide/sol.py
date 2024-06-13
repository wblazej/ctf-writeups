plain_text = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
en = bytes.fromhex("d80067af38da70666f5a04d8fedcb2d5987dd00c35a72a26b4c890be49d138a4")

stream = [a ^ b for a, b in zip(plain_text.encode(), en)]

secret = bytes.fromhex("ff75478b48ab0312162b72fdd9ffc2a1bb0ff77d4d870e02c0bcb29e39a040d2")
print(bytes([a ^ b for a, b in zip(stream, secret)]))