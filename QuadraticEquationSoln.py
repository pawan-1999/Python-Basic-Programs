'''
@Author: Pawan Gupta
@Date: 2021-08-19 18:40:00
@Title : To find the solution of a quadratic equation
'''

import math

class QuadraticEquation():

    def solution(self,a,b,c):
        delta = (math.pow(b,2)) - 4 * a * c

        sol1 = (- b + (math.sqrt(delta)) )/ (2*a)
        sol2 = (- b - (math.sqrt(delta)) )/ (2*a)

        if (delta > 0):
            print("Two real and distinct roots")
        elif (delta == 0):
            print("Two equal and real roots")
        else:
            print("Has no real roots")

        print()
        print("Root 1 of x = ",sol1)
        print("Root 2 of x = ",sol2)

#variable
flag = True

#object
obj = QuadraticEquation()

while (flag == True):
    try:

        print("To find the solution for quadratic equation ax^2+bx+c : ")
        a = int(input("Enter the value of a : "))
        if (a==0):
            raise ValueError
        b = int(input("Enter the value of b : "))
        c = int(input("Enter the value of c : "))
        print(f"{a}x^2 + {b}x + {c}")
        print()
        obj.solution(a,b,c)
        flag = False

    except ValueError:
        print("##Invalid Input## \n Enter the value greter value than 0")
        flag =True

    except Exception as e:
        print(e)
        flag = True