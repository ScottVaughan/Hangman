'''
Created on Oct 2, 2014

@author: Scott Vaughan
'''
class Employee:
    '''
    classdocs
    '''
    def __init__(self, name, title, pay):
        self.employeeName = name
        self.employeeTitle = title 
        self.employeePay = pay
     
    def Hire(self,fileIn,hireEmployee,hireJobTitle,hirePay):
        with open("employees.txt", "a") as fileIn:
            fileIn.write("\n\n"+hireEmployee)
            fileIn.write("\n"+hireJobTitle)
            fileIn.write("\n"+hirePay)
            fileIn.close()
        
    def Fire(self,fileIn,fireEmployee):
        with open("employees.txt") as fileIn, open("employeesUpdated.txt", "w") as output_file:
            for line in fileIn:
                if fireEmployee not in line: 
                    output_file.write(line)
                else:
                    next(fileIn)
                    next(fileIn)
                    next(fileIn)
        print(fireEmployee+" Has been terminated")
                
    def printEmployee(self): 
        print("employee name: " + self.employeeName)
        print("job title: " + self.employeeTitle)
        print("hourly pay: " + self.employeePay)