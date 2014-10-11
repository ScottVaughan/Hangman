'''
Created on Oct 2, 2014

@author: Scott Vaughan
'''
from Employee import Employee

def Hire():
    hireEmployee = input("Enter employees full name to hire: ")
    hireJobTitle = input("Enter employees job title: ")
    hirePay = input("hourly pay: ")
    info.Hire(fileIn, hireEmployee, hireJobTitle, hirePay)
    return
  
def Fire():  
    fireEmployee = input("Enter employees full name to terminate: ")
    info.Fire(fileIn, fireEmployee)
    return

try:
    fileIn = open('employees.txt','r')
    
    for line in fileIn:
        employeeName = fileIn.readline()
        employeeTitle = fileIn.readline()
        employeePay = fileIn.readline()
    
        info = Employee(employeeName, employeeTitle, employeePay)
        info.printEmployee()
    fileIn.close()

except IOError:
    print("An error has occured while reading in the file")
 
    
while True:
    print("\n Press 'H' - Hire employee")
    print("\n Press 'F' - Fire employee")
    print("\n Press 'E' - Exit")
    userInput = input("Please enter a valid value: ")
    
    if userInput == 'H':
        Hire()
    elif userInput == 'F': #This is appending not removing
        Fire()
    elif userInput == 'E':
        break
    
print("program exited")
    
              
    
        
        


        
        
        
        
        