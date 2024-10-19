import os
import pandas as pd
import re
import time
from datetime import datetime
class programA:
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
    #write to that file
    def writeToValidityFile(self, toWrite):
        if self.fileCreated == True:
            with open(self.filename, "w") as validCheck:
                validCheck.write(f"{toWrite} . \n")
    #create a file
    def createFile(self):
        if self.fileCreated == False:
            with open(self.fileName, "w") as  validCheck:
                self.fileCreated = True
                
    def initialFormatCheck(self):
        if self.fileCheck.empty:
            self.writeToValidityFile(f"FILE {self.currentFile}: CSV is empty.")
            return 1
        elif self.fileCheck.shape[0] < 2 or self.fileCheck.shape[1] < 2:
            self.writeToValidityFile(f"FILE {self.currentFile}: Initial check for shape failed on line 0 or 1")
            return 1
        #A CHECK FOR THE FIRST LAST NAME
        elif pd.isna(self.fileCheck.iloc[0,0]) or pd.isna(self.fileCheck.iloc[0,1]) or  (self.fileCheck.iloc[0, 0] == False or self.fileCheck.iloc[0, 1] == False) :
            self.writeToValidityFile(f"FILE {self.currentFile}: Initial check for name failed on line 1")
            return 1
        #acheck for CLASS NAME
        elif pd.isna(self.fileCheck.iloc[1,0]) or self.fileCheck.iloc[1,0] != "CS 4500" :
            self.writeToValidityFile(f"FILE {self.currentFile}: Initial check for CLASS name failed on line 2")
            return 1
        
        else:
            return 0
    def checkForAdditionalLines(self):
        if self.fileCheck.shape[0] > 2:
            return 1
        return 0
    #https://www.geeksforgeeks.org/python-validate-string-date-format/
    def dateCheck(self, date):
        #format reference https://pynative.com/python-datetime-format-strftime/
        format = "%m/%d/%Y"
        isDateValid = True
        try:
            isDateValid = bool(datetime.strptime(date,format))
        except:
            isDateValid = False
            
        if isDateValid == False:
            return 1
        else:
            return 0
                 
    #base check for fromat
    def openFilesAndCheck(self):
        #main loop for checking
        for file in self.listOfDirectoryFiles:
            checkedFailed = 0
            self.currentFile = file
            self.fileCheck = pd.read_csv(f"{file}",header = None, na_filter=False)
            print(self.fileCheck)
            self.createFile()
            #self.initialFormatCheck(fileCheck)
            #check initial format
            checkedFailed = self.initialFormatCheck()
            if checkedFailed == 1:
                continue
            #check if there are additional lines, if return 0 then it is just the header and is empty
            if (self.checkForAdditionalLines() < 1):
                # we are done checking so
                self.writeToValidityFile(f"FILE {self.currentFile}: Initial check for CLASS name failed line 2")
                continue
            #we can now iterate through the rows of the dataframe checking each column, it is assumed if we make it here that the file starts at row 3.
            checkedFailed = self.dateCheck()
            for index, row in self.fileCheck.iloc[2:].iterrows():
                self.currentLine = index
                #date check
                date = row[0]
                print(f"Type of Date {type(date)}")
                checkedFailed = self.dateCheck(self, date)
                if checkedFailed == 1:
                    self.writeToValidityFile(f"FILE {self.currentFile}: check for date failed on line {self.currentLine}")
                    break
                
            if checkedFailed == 1:
                continue
  
                
                  
    #checks directory
    def fileChecks(self):
        #modified my old regex from phase A, tested on regex101.com. 
        #posted the image for doc in server
        count = 0
        regPat = r"^[A-Za-z]+[lL][oO][gG]\.[cC][sS][vV]$"
        for file in os.listdir():
            if re.match(regPat,file):
                count +=1
                self.listOfDirectoryFiles.append(file)
        print(f"LENGTH {len(self.listOfDirectoryFiles)}")
        if len(self.listOfDirectoryFiles) <= 0:
            print("There are no valid files matching pattern: X (any capital letter) + [lL][oO][gG]\.[cC][sS][vV] \n EXITING.......")
            #had to put this in so when an executable is generated it doesn't quit extremely fast
            time.sleep(2)
            exit(1)
        print(f"Total valid file names found {count}\n With more than one file found, opening a new file called ValidityChecks.txt")
        if len(self.listOfDirectoryFiles)> 0:
            self.openFilesAndCheck()
        #sorta redundant, meh
       
        
    
    def classDriver(self):
        
        print(self.introMessage)
        input("Press any key to continue....")
        self.fileChecks()
            

if __name__ == "__main__":
    programA()