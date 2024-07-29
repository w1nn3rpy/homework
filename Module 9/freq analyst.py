file = open('text.txt', 'r')
analystis = open('analystis.txt', 'w')


def all_sym(text):
    count = 0
    dct_sym = dict()

    for i_line in text:
        for sym in i_line.lower():
            if sym.isalpha():
                count += 1
                if sym in dct_sym.keys():
                    dct_sym[sym] += 1
                else:
                    dct_sym[sym] = 1

    for i in dct_sym:
        dct_sym[i] = round(dct_sym[i] / count, 3)

    sym_sort_count = dict()
    for i in dct_sym:
        if dct_sym[i] not in sym_sort_count:
            sym_sort_count[dct_sym[i]] = list(i)
        else:
            sym_sort_count[dct_sym[i]].append(i)

    return sym_sort_count


def analysis_file(some_dict, file):
    for sym_cnt in sorted(some_dict.keys(), reverse=True):
        for sym in sorted(some_dict[sym_cnt]):
            file.write(f'{str(sym)} {str(sym_cnt)}' + '\n')


analysis_file(all_sym(file), analystis)

