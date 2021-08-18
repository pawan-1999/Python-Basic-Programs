'''
@Author: Pawan Gupta
@Date: 2021-08-17 15:43:00
@Title : finding prime factors of given number
'''

import math

#variable
flag = True

#Below function will print the all prime factor of given number
def prime_factors(num):
    """"" Using the while loop, we will print the number of two's that divide n """""
    while num % 2 == 0:
        print(2,)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):

        # while i divides n , print i and divide n
        while num % i == 0:
            print(i,)
            num = num / i
    if num > 2:
        print(num)
while(flag == True):
    #Exception try Block
    try :
        # calling function
        num = int(input("Enter the number to get its prime factor :"))
        prime_factors(num)
        flag =False

    #Exception Catch block
    except Exception as e:
        print(e)
        flag =True

