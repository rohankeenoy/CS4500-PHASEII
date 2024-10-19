import os
import pandas as pd
import re
import time
class programA:
    def __init__(self):
        self.introMessage = "---------Welcome to program A of phase II. This program is for validating patterns in file names and checks the validity of file contents. ---------\n"
        #data strucutre "L per assignment document"
        self.listOfDirectoryFiles = []
        self.fileName = "ValidityChecks.txt"
        self.fileCreated = False
        
        
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
            
    #base check for fromat
    def openFilesAndCheck(self):
        for file in range(len(self.listOfDirectoryFiles)):
            try:
                fileCheck = pd.read_csv(f"{file}")
            except:
                print("Could not open a supposedly valid csv: {file}, continuing")
            if(fileCheck):
                #creates the validity check file 
                self.createFile()
                
                  
    #checks directory
    def fileChecks(self):
        #modified my old regex from phase A, tested on regex101.com. 
        #posted the image for doc in server
        regPat = r"^[A-Za-z]+[lL][oO][gG]\.[cC][sS][vV]$"
        for file in os.listdir():
            if re.match(regPat,file):
                count +=1
                self.listOfDirectoryFiles.append(file)
        if len(self.listOfDirectoryFiles) < 1:
            print("There are no valid files matching pattern: X (any capital letter) + [lL][oO][gG]\.[cC][sS][vV] \n EXITING.......")
            #had to put this in so when an executable is generated it doesn't quit extremely fast
            time.sleep(2)
            exit(1)
        print(f"Total valid file names found {count}\n With more than one file found, opening a new file called ValidityChecks.txt")
        if len(self.listOfDirectoryFiles > 1):
            self.openFilesAndCheck()
        #sorta redundant, meh
        else: 
            print("There are no valid files matching pattern: X (any capital letter) + [lL][oO][gG]\.[cC][sS][vV] \n EXITING.......")
            #had to put this in so when an executable is generated it doesn't quit extremely fast
            time.sleep(2)
            exit(1)
        
    
    def classDriver(self):
        print(self.introMessage)
        input("Press any key to continue....")
        self.fileChecks()
            

if __name__ == "__main__":
    programA()