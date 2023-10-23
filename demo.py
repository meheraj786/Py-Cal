print("Enter first number: ")
a = int(input())

print("Enter Arithmatic operator: ")
ch = input()

print("Enter Second Number: ")
b = int(input())

if (ch == '+'):
    print("Addition is: " + str(a + b))
elif (ch == '-'):
    print("Substraction is: " + str(a - b))
elif (ch == '*'):
    print("Multiplication is: " + str(a * b))   
elif (ch == '/'):
    print("Division is: " + str(a / b)) 
elif (ch == '%'):
    print("Remainder is: " + str(a % b))        
else: 
    print("fuck man, are you a mad?")    