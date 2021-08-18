'''
@Author: Pawan Gupta
@Date: 2021-08-17 11:30:00
@Title : To get the result of flip coin which is fliped number of times 
'''

#Module importing to use random func
import random

lst = ("HEAD","TAIL")

#variable
noHead=0
noTail=0
i=0
flag = True

while (flag == True) :
    #Exception try block
    try :
        print("Enter the number of times you want to flip the coin :")
        num = int(input())
        if num>0 :
            while(i<=num):
                outcome = random.choice(lst)
                if(outcome=="HEAD"):
                    noHead = noHead + 1
                elif(outcome=="TAIL"):
                    noTail = noTail + 1
                i = i+1

        perOfTail = str((noTail/num) * 100)
        perOfHead = str((noHead/num) * 100)

        print("Head :"+perOfHead,"VS Tail:"+perOfTail)

        if perOfHead>perOfTail:
            print("Head Wins with percent : "+perOfHead)
            flag = False
        elif perOfHead ==perOfTail:
            print("Both Percentages are equal")
            flag = True
        else:
            print("Tail Wins with percent : "+perOfTail)
            glag = False

    #Exception Catch Block
    except Exception as e:
        print(e)
        flag = True
