import os
import pandas as pd
import re
import time
from datetime import datetime

class programz:
    def __init__(self):
        self.introMessage = "---------Welcome to program A of phase II. This program is for validating patterns in file names and checks the validity of file contents. ---------\n"
        #data strucutre "L per assignment document"
        self.listOfDirectoryFiles = []
        self.fileName = "ValidityChecks.txt"
        self.fileCreated = False
        self.fileCheck = pd.DataFrame()
        self.currentFile = ""
        self.currentLine = 3
    
        self.classDriver()    
    def timeCheck(self, t1, t2):
        #This only checks it for the HH:MM:SS format and assume military time
        format = "%H:%M"
        print(datetime.strptime(t2, format).minute)

        if( datetime.strptime(t2, format).hour < datetime.strptime(t1, format).hour ):
            return 1
        else:
            return 0
    # def overTimeCheck(self, t1, t2):
    #     #This function assumes t2 > t1, so it is called chronologically after timeCheck which makes sure that t2 > t1
    #     format = "%H:%M"
    #     t11 = datetime.strptime(t1,format)
    #     t22 = datetime.strptime(t2, format)
    #     print(t22-t11)
    #     # print((datetime.strptime(t2, format).hour +((datetime.strptime(t2, format).minute)/60)))
    #     # if(  (datetime.strptime(t2, format).hour  - datetime.strptime(t1, format).hour)+((datetime.strptime(t1, format).minute)) >4  ):
    #     #     return 11
    #     # else:
    #     #     return 10
    #     # if(  (datetime.strptime(t2, format).hour +((datetime.strptime(t2, format).minute)/60)) - (datetime.strptime(t1, format).hour+((datetime.strptime(t1, format).minute)/60)) >4  ):
    #     #     return 11
    #     # else:
    #     #     return 10
    def overTimeCheck(self, t1, t2):
        #This function assumes t2 > t1, so it is called chronologically after timeCheck which makes sure that t2 > t1
        #if(  (datetime.strptime(t2, format).hour +((datetime.strptime(t2, format).minute)/60)) - (datetime.strptime(t1, format).hour+((datetime.strptime(t1, format).minute)/60)) >4  ):
        format = "%H:%M"
        format2 = "%H:%M:%S"
        #delta = datetime.strptime((datetime.strptime(t2, format) - datetime.strptime(t1, format)), format)
        delta = datetime.strptime((str(datetime.strptime(t2, format) - datetime.strptime(t1, format))), format2)
        print(delta)
        if( delta.hour > 4  ):
            return 1
        elif (delta.hour == 4 and delta.minute > 0 ):
            return 1
        else:
            return 0
    def bs(self):
        a = 1
    def classDriver(self):
        # print("hi")
        # print(self.bs())
        print(self.overTimeCheck("12:21", "19:31"))
        print(self.overTimeCheck("12:21", "16:20"))
        print(self.overTimeCheck("12:21", "16:21"))
        print(self.overTimeCheck("12:21", "16:22"))
        print(self.overTimeCheck("12:21", "13:21"))
        print(self.overTimeCheck("12:21", "11:21"))

if __name__ == "__main__":
    programz()