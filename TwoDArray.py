'''
@Author: Pawan Gupta
@Date: 2021-08-19 23:36:00
@Title : To create a 2d array with user input
'''

class Matrix:

    @staticmethod
    def inputMatrix(Rows,Col):

        matrix = []
        print("Enter the entries in row wise:")

        for M in range(Rows):
            array = []
            for N in range(Col):
                array.append(int(input())) #for input in array
            matrix.append(array)

        print("The 2D array is given below:")

        for M in range(Rows):
            for N in range(Col):
                print(matrix[M][N], end=" ") #printing array
            print()

while True:

    try:
        Rows = int(input("Enter the number of rows:"))
        Col = int(input("Enter the number of columns:"))
        Matrix.inputMatrix(Rows,Col)
        break

    except Exception as e:
        print(e)
        continue
