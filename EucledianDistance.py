'''
@Author: Pawan Gupta
@Date: 2021-08-19 18:36:00
@Title : To find the Euclidean distance from point (x,y) from origin
'''

#module
import math

#class
class Calculator:
    #class method
    def distance(Self,X,Y):
        powerOfX = math.pow(X,2)
        powerOfY = math.pow(Y,2)
        dist = math.sqrt(powerOfX + powerOfY)
        return dist

#Object
obj = Calculator()

#variable
flag = True

while (flag == True):
    try:
        x = float(input("Enter the value of X : "))
        y = float(input("Enter the value of Y : "))
        print("Distance =",obj.distance(x,y),"Units")
        flag = False

    except Exception as e:
        print(e)
        flag = True