class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        [print(i) for i in self.list]
        return str()

    def __add__(self, other):
        result = [self.list[i][j] + other.list[i][j] for i in range(len(self.list)) for j in range(len(self.list[0]))]
        return Matrix([result[k:k + len(self.list[0])] for k in range(0, len(result), len(self.list[0]))])


my_matrix = Matrix([[1, 2, 3], [3, 4, 3], [5, 6, 3]])
print(my_matrix)

print(Matrix([[2, 3, 3], [4, 5, 3], [6, 7, 3]]))
my_matrix2 = Matrix([[2, 3, 3], [4, 5, 3], [6, 7, 3]])

print(my_matrix + my_matrix2 + my_matrix)
