from zipfile import ZipFile

with ZipFile('voina-i-mir.zip', 'r') as myzip:
    myzip.extractall()

text = open('voina-i-mir.txt', 'r')


def counting(file):
    chars_dict = dict()
    for line in file:
        for char in line:
            if char.isalpha():
                if char in chars_dict.keys():
                    chars_dict[char] += 1
                else:
                    chars_dict[char] = 1

    sym_sort_count = dict()

    for i in chars_dict:
        if chars_dict[i] not in sym_sort_count:
            sym_sort_count[chars_dict[i]] = list(i)
        else:
            sym_sort_count[chars_dict[i]].append(i)

    return sym_sort_count


def analysis_file(some_dict):
    for sym_cnt in sorted(some_dict.keys(), reverse=True):
        for sym in sorted(some_dict[sym_cnt]):
            print(f'{str(sym)} {str(sym_cnt)}')


analysis_file(counting(text))
