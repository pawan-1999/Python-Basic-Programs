'''
@Author: Pawan Gupta
@Date: 2021-08-20 01:20:00
@Title : To find the triplets with sum zero from given input
'''

class Triplets:

    def find_triples(Self,arr, n):

        #local variable
        found = True
        count = 0

        for i in range(0, n - 2):

            for j in range(i + 1, n - 1):

                for k in range(j + 1, n):

                    if arr[i] + arr[j] + arr[k] == 0:
                        print(arr[i], arr[j], arr[k])
                        found = True
                        count = count + 1

        print("The number of triples are: ", count)

        if not found:
            print(" not exist ")

#object
obj = Triplets()

while True:
    try:
        array = []
        length = int(input("Enter length of array: "))
        for i in range(length):
            temp = int(input("Enter numbers: "))
            array.append(temp)
        obj.find_triples(array, length)
        break

    except ValueError:
        print("Check the input")
        continue