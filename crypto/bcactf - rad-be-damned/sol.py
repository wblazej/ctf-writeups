def find_leftmost_set_bit(plaintext):
    pos = 0
    while plaintext > 0:
        plaintext = plaintext >> 1
        pos += 1
    return pos

def decrypt_segment(segment):
    cp = int("10011", 2)
    cp_length = cp.bit_length()

    for possible_bit in range(12):
        mask = 1 << possible_bit
        candidate = segment ^ mask
        bin_letter = candidate >> (cp_length - 1)
        rem = candidate & ((1 << (cp_length - 1)) - 1)

        if validate_rem(bin_letter, rem, cp, cp_length):
            return chr(bin_letter)

def validate_rem(bin_letter, rem, cp, cp_length):
    recalculated_rem = bin_letter * 2 ** (cp_length - 1)
    while recalculated_rem.bit_length() >= cp_length:
        first_pos = find_leftmost_set_bit(recalculated_rem)
        recalculated_rem = recalculated_rem ^ (cp << (first_pos - cp_length))
    return recalculated_rem == rem

def decrypt_corrupted_text(corrupted_text):
    plaintext = ""
    for i in range(0, len(corrupted_text), 12):
        segment = int(corrupted_text[i:i+12], 2)
        decrypted_char = decrypt_segment(segment)
        plaintext += decrypted_char
    return plaintext

corrupted_text = "011000001011010000111000011000111110011000111100011101001100001001100111011111110110011110010100011100010111011011111001010011011011010100011010001010011110010110010000001110111010001000011100011100011100010011111101010101101011110000110010001101100011011010100011001001010010001011011111011110000010001101100110010000110011011101110101010010111000011100011001010100011001001000111000001101010001011000100111010011000001011100011111111101010111010001001000001101000000001101011100010101101010101011011110011010100010010010010011010101010101010000010000001011011100011000011010010000111110001110011111011100011101010110001010010100100111001110011100011010101000011000101010001000101001001100011101111101100010010011100000010101111010011101101000011100100101001001000001010001111111010001001101111110100101011111001100"  # Example encrypted text
print(decrypt_corrupted_text(corrupted_text))
