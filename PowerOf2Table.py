'''
@Author: Pawan Gupta
@Date: 2021-08-17 11:44:00
@Title : Table of Base 2 with power wgich is given by user
'''

#constant
BASE = 2

#variable
i=0
flag = True

#function
def powerOfBase(power):
    """"" Finding power in the function """""
    table = BASE ** power
    print(BASE,"^",power," = ",table)

while(flag == True):
    #Exception Try
    try:
        N = int(input("Enter the power for 2 :"))
        while(i<=N):
            powerOfBase(i)
            i += 1
        flag = False
    #Exception Catch
    except Exception as e:
        print(e)
        flag = True
