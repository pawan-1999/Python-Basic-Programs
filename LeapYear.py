'''
@Author: Pawan Gupta
@Date: 2021-08-17 11:35:00
@Title : Checking the entered year is a leap year or not
'''
#function to check leap year or not
def CheckLeap(Year):
        """"Checking if the given year is leap year"""""

        if len(str(year))==4 : #condtion that year must be of 4 digits
            if ((Year % 400 == 0) or
                    (Year % 100 != 0) and
                    (Year % 4 == 0)):
                print("Given Year is a leap Year")
            else:
                print("Given Year is not a leap Year")
        else:
            print("Enter the valid year it should contain 4 digits")

if __name__ == '__main__':
    flag = True
    while(flag == True):
        #Exception Try Block
        try :
            year = int(input("Enter the year to check it is leap year or not :"))
            CheckLeap(year) #function Calling
            flag =False

        #Exception catch Block
        except Exception as e:
            print(e)
            flag =True