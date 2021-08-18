'''
@Author: Pawan Gupta
@Date: 2021-08-17 12:19:00
@Title : Table of Base 2 with power wgich is given by user
'''

#variable
i = 1
harmonicValue = 0
flag = True

while(flag == True):
    #Exception Try block
    try :
        N = int(input("Enter the Nth harmonic number : "))

        if N > 0 :
            while (i<=N) :
                harmonicValue += 1/i
                i += 1
            print("Harmonic Value = ",harmonicValue)
            flag = False
        else :
            print("Enter the valid Nth value it cannot be 0 or less than that")
            flag = True

    #Exception catch Block
    except Exception as e :
        print(e)
        flag = True