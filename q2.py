#Even or odd
a=int(input("Enter a:"))
if a%2==0:
    print("Even")
else:
    print("Odd")

#Positive Negative and Zero
a=int(input("Enter a:"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

#Largest of two numbers
a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a>b:
    print("a is largest")
else:
    print("b is largest")

#largest of 3 numbers
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")

#Voting eligibilty
a=int(input("Enter age:"))
if a>=18:
    print("eligible for Voting")
else:
    print("not eligible")

#Leap year
a=int(input("Enter year:"))
if a%4==0:
    print("Leap year")
else:
    print("Not a leap year")

#Grade
a=int(input("Enter Marks:"))
if a>=90 and a<=100:
    print("Grade:A")
elif a<90 and a>69:
    print("Grade:B")
elif a<70 and a>49:
    print("Grade:C")
else:
    print("Fail")

#Divisible by 7:
a=int(input("Enter a:"))
if a%7==0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

#simple calculator
a=int(input("Enter a:"))
b=int(input("Enter b:"))
o=int(input("Enter the Operation to be done:"))
if o==1:
    print("addition:",a+b)
elif o==2:
    print("subtraction:",a-b)
elif o==3:
    print("multiplication:",a*b)
elif o==4:
    print("division:",a/b)
else:
    print("Operation not available")

#Password Check
a=input("Enter Password length:")
if len(a)>=8:
    print("Strong password")
else:
    print("Weak password")
