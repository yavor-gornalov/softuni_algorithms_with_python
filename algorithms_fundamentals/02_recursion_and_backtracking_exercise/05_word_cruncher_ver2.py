# https://judge.softuni.org/Contests/Practice/Index/3460#4
import re


def find_all_solutions(target, idx, words_idx, used_words):
    if idx == len(target_string):
        print(*used_words, sep=" ")
        return

    for current_word, word_data in words_idx.items():
        if word_data["count"] < 1:
            continue
        if idx in word_data["indexes"]:
            current_word_idx = word_data["indexes"].index(idx)
            word_data["indexes"].pop(current_word_idx)
            word_data["count"] -= 1
            used_words.append(current_word)
            idx += len(current_word)

            find_all_solutions(target, idx, words_idx, used_words)  # call recursion

            idx -= len(current_word)
            used_words.pop()
            word_data["count"] += 1
            word_data["indexes"].insert(current_word_idx, idx)


substrings = input().split(", ")
target_string = input()

words_indexes = {}
for word in substrings:
    if word not in words_indexes:
        words_indexes[word] = {"count": 0,
                               "indexes": [match.start() for match in re.finditer(f'{word}', target_string)]}
    words_indexes[word]["count"] += 1

find_all_solutions(target_string, 0, words_indexes, [])
