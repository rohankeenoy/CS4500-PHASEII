import os

class programA:
    def __init__(self):
        self.introMessage = "---------Welcome to program A of phase II. This program is for validating patterns in file names and checks the validity of file contents. ---------\n"
        
        
        
        
        self.classDriver()
    
    def classDriver(self):
        print(self.introMessage)
        input("Press any key to continue....")
            

if __name__ == "__main__":
    programA()