from cryptanalysis import shift_word

with open("text.txt", "r") as text_file:
    with open("cipher.txt", "w") as cipher_text:
        cipher_text.write(shift_word(9, text_file.read()))