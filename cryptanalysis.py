from string import ascii_lowercase, ascii_uppercase


def shift(key: int, letter: str):
    if letter in ascii_lowercase:
        new_letter_index = (ascii_lowercase.index(letter) + key) % 26
        return ascii_lowercase[new_letter_index]
    elif letter in ascii_uppercase:
        new_letter_index = (ascii_uppercase.index(letter) + key) % 26
        return ascii_uppercase[new_letter_index]
    else:
        return letter

def shift_word(key: int, word: str):
    new_word = []
    for letter in word:
        if letter != " ":
            new_word.append(shift(key, letter))
        else:
            new_word.append(" ")
    return "".join(new_word)

def unshift_word(key: int, word: str):
    return shift_word(-key, word)



    
