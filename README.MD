# Caesar Cipher Cryptanalysis

This repository contains Python scripts for encrypting and decrypting text using the Caesar cipher. It includes brute-force decryption using English word frequency analysis.

## Files Overview

### 1. `encipher.py`
This script encrypts a given text using the Caesar cipher by shifting letters forward.

**Functions:**
- `shift(key: int, letter: str)`: Shifts a single letter by a given key.
- `shift_word(key: int, word: str)`: Encrypts a full text string by shifting each letter.

**Usage:**
```
python encipher.py
```
This script reads plaintext from `text.txt`, encrypts it using a shift of 9, and saves the result to `cipher.txt`.

---

### 2. `cryptanalysis.py`
Contains functions for decrypting text encrypted using the Caesar cipher.

**Functions:**
- `unshift_word(key: int, word: str)`: Decrypts a given text by shifting letters backward.

---

### 3. `brute_caesar.py`
Performs a brute-force attack on Caesar cipher text by trying all possible shifts and checking which results in the most English words.

**Functions:**
- `count_english_words(text: str)`: Counts the number of valid English words in a given text.
- `unshift_word(key: int, word: str)`: Decrypts text with a given shift key.

**Process:**
- Reads encrypted text from `cipher.txt`.
- Attempts all 25 possible shifts.
- Determines the best decryption by counting English words.
- Prints the most likely key and decrypted text.

**Usage:**
```
python brute_caesar.py
```

---

## Dependencies
- `nltk` (Natural Language Toolkit)
  - Install using `pip install nltk`
  - Run the following inside Python to download the word corpus:
    ```python
    import nltk
    nltk.download('words')
    ```

## How It Works
1. `encipher.py` encrypts plaintext using the Caesar cipher.
2. `brute_caesar.py` decrypts the text using brute force.
3. The best decryption is determined by counting English words.

## Example
If `text.txt` contains:
```
hello world
```
Encrypting with shift 9 produces:
```
qnuux fxlnu
```
Brute-force decryption will recover:
```
hello world (Key: 9)
```

---

## Author
This repository was created for learning and demonstrating cryptanalysis techniques on simple substitution ciphers.

