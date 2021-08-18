'''
@Author: Pawan Gupta
@Date: 2021-08-16 19:32:00
@Title : To get the user name in the given string 
'''
#variable
flag = True

while(flag == True):
    #Exception Try
    try:
        userName=input("Enter User Name : ")
        if userName.isalpha(): #condtion to check the entered input is alphabetic or not
            if len(userName)>=3: #condition to check user name with atleast 3 chars
                print("Hello",userName, "How are you?")
                flag = False
            else:
                print("User Name should contain atleast 3 characters")
                flag = True
        else:
            print("Invalid input please enter alphabates")
            flag = True

    #Exception Catch
    except Exception as e:
        print(e)
        flag = True
