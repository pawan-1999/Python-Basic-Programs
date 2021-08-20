'''
@Author: Pawan Gupta
@Date: 2021-08-20 16:23:00
@Title : To get the elapsed time from where user started the stop watch and ended it
'''

from time import time

class SimulateStopwatch:
    startTime = 0
    stopTime = 0
    elapsTime = 0

    def inputStartTime(self):
        self.startTime = int(time() * 1000)               # input start time in millisecond
    def inputStopTime(self):
        self.stopTime = int(time() * 1000)                # input stop time in millisecond
    def elapsedTime(self):
        self.elapsTime = self.stopTime - self.startTime   # calculate elapsed time
        print("Elapsed Time : ",int(self.elapsTime) / 1000, "sec")          # print elapsed time in second

if __name__ == '__main__':                                # main method

    obj = SimulateStopwatch()                          # creating object of the class

    while True:

        try:

            startInput = int(input("Enter 1 for start: "))
            if startInput != 1:
               raise ValueError
               continue
            obj.inputStartTime()                       # inputStartTime method call

            stopInput = int(input("Enter 2 for stop: "))
            if stopInput != 2:
                raise OverflowError
                continue
            obj.inputStopTime()                        # inputStopTime Method call

            obj.elapsedTime()                          # elapsedTime Method call
            break

        except ValueError:
            print("Wrong input !! Enter 1 only")

        except OverflowError:
            print("Wrong input !! Enter 2 only")