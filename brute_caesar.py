from nltk.corpus import words
from cryptanalysis import unshift_word

english_words = set(words.words())

def count_english_words(text: str):
    # words_found = [word.lower() for word in text.split() if word.lower() in english_words]
    text_list = text.split()
    words_found = []
    for word in text_list:
        if word.lower() in english_words:
            words_found.append(word)
    
    return len(words_found)

best_fit = 0
likely_key = None
best_text = None
with open("cipher.txt", "r") as cipher_file:
    cipher_text = cipher_file.read()
for key in range(1, 26):
    outcome = unshift_word(key, cipher_text)
    english_word_count = count_english_words(outcome)
    if int(english_word_count) > int(best_fit):
        best_fit = english_word_count
        likely_key = key
        best_text = outcome
    print(f"Key: {key}, Outcome: {outcome[:35]}, English word count: {english_word_count}")

print("\n ----- Best Decryption Candidate -----")
print(f"Most likely key is {likely_key}")
print(f"Best text: {best_text[:40]}...")