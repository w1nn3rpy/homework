from typing import List
from functools import reduce


sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic",
             "because his mother was a Catholic", "or had been"]

def was_count(count, sentence):
    words = sentence.split()
    for word in words:
        if word == 'was':
            count += 1
            print(f'Количество "was": {count}')
    return count

print(f'Итоговое кол-во "was": {reduce(was_count, sentences, 0)}')
