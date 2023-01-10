class Matrix:
    def __init__(self, matrix_string:str):
        mat = matrix_string.split("\n")
        self.matrix = [line.split(" ") for line in mat]
        print(self.matrix)



    def row(self, index):
        return [int(x) for x in self.matrix[index-1]]

    def column(self, index):
        col = []
        for i in range(len(self.matrix)):
            col.append(int(self.matrix[i][index-1]))
        return col
