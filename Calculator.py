// In this program we have created a simple basic calculator in which we will first take 2 inputs from the user and then we will ask the user which operation to perform. then we will perform the operation and give the required output.

n1 = float(input("Enter First number :- "))
n2 = float(input("Enter Second Number :- "))

print("Select Operation :- ")
print("1 - Addition ")
print("2 - Subtraction ")
print("3 - Multiplication ")
print("4 - Division ")

op = input("Enter Your Choice (1/2/3/4) :- ")
    
if(op=='1'):
    print("Addition = ",n1," + ",n2," = ",n1+n2)
elif(op=='2'):
    print("Subtraction = ",n1," - ",n2," = ",n1-n2)
elif(op=='3'):
    print("Multiplication = ",n1," * ",n2," = ",n1*n2)
elif(op=='4'):
    print("Division ",n1," / ",n2," = ",n1/n2)
else:
    print("WRONG CHOICE ....(Please Enter any one from the given operations)")


        



     
