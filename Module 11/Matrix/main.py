class Matrix:
    def __init__(self, rows, column):
        self.rows = rows
        self.columns = column
        self.data = []

    def __repr__(self):
        lines = []
        for row in self.data:
            line = ' '.join(str(x) for x in row)
            lines.append(line)
        return '\n'.join(lines) + '\n'

    def print_matrix(self, other):
        lines = []
        for row in other:
            line = ' '.join(str(x) for x in row)
            lines.append(line)
        return '\n'.join(lines) + '\n'

    def add(self, other):
        name = 'Сложение матриц'
        sum_matrix = []
        for i_list in range(len(self.data)):
            temp = []
            for i_num in range(self.columns):
                temp.append(self.data[i_list][i_num] + other.data[i_list][i_num])
            sum_matrix.append(temp)
        return name + '\n' + self.print_matrix(sum_matrix)

    def subtract(self, other):
        name = 'Вычитание матриц'
        sub_matrix = []
        for i_list in range(len(self.data)):
            temp = []
            for i_num in range(self.columns):
                temp.append(self.data[i_list][i_num] - other.data[i_list][i_num])
            sub_matrix.append(temp)
        return name + '\n' + self.print_matrix(sub_matrix)

    def multiply(self, other):
        name = 'Умножение матриц'
        if self.columns == other.rows and self.rows == other.columns:
            rows_A, columns_A = self.rows, self.columns
            rows_B, columns_B = other.rows, other.columns
            result = [[0 for _ in range(columns_B)] for _ in range(rows_A)]
            for i_rows_a in range(rows_A):
                for j_cols_b in range(columns_B):
                    for k_cols_a in range(columns_A):
                        result[i_rows_a][j_cols_b] += self.data[i_rows_a][k_cols_a] * other.data[k_cols_a][j_cols_b]
            return name + '\n' + self.print_matrix(result)

        else:
            raise ValueError('Умножение двух этих матриц не возможно')

    def transpose(self):
        name = 'Транспорация матрицы'
        result = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
        for i_val in range(self.rows):
            for j_val in range(self.columns):
                result[j_val][i_val] = self.data[i_val][j_val]
        return name + '\n' + self.print_matrix(result)


a = Matrix(2, 3)
a.data = [[1, 2, 3], [4, 5, 6]]

b = Matrix(2, 3)
b.data = [[7, 8, 9], [10, 11, 12]]

c = Matrix(3, 2)
c.data = [[1, 2], [3, 4], [5, 6]]

print(a)

print(b)

print(a.add(b))

print(a.subtract(b))

print(a.multiply(c))

print(a.transpose())
