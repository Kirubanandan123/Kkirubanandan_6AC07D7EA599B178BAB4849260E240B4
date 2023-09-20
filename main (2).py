[15/09, 2:28 pm] Madhan BCA: # Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
[15/09, 3:15 pm] Madhan BCA: # Python3 program to calculate the CGPA
# and CGPA percentage of a student
def CgpaCalc(marks, n):
 
    # Variable to store the grades in
    # every subject
    grade = [0] * n
   
    # Variables to store CGPA and the
    # sum of all the grades
    Sum = 0
   
    # Computing the grades
    for i in range(n):
       grade[i] = (marks[i] / 10)
   
    # Computing the sum of grades
    for i in range(n):
       Sum += grade[i]
   
    # Computing the CGPA
    cgpa = Sum / n
   
    return cgpa
   
# Driver code
n = 5
marks = [ 90, 80, 70, 80, 90 ]
 
cgpa = CgpaCalc(marks, n)
       
print("CGPA = ", '%.1f' % cgpa)
print("CGPA Percentage = ", '%.2f' % (cgpa * 9.5))
 
# This code is contributed by divyeshrabadiya07
[15/09, 3:15 pm] Madhan BCA: # Python3 code to linearly search x in arr[].
  
  
def search(arr, N, x):
  
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
  
  
# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)
  
    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)