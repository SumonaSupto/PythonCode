#input user name 
str = input("Enter your first name :")
print("Length of your name is :" , len(str))

#find function
print(str.count("$"))

#conditional statement
 
marks = float (input("Enter your marks :"))

if (marks > 90):
     print("A")
elif(marks >=80 and marks< 90):
     print("B")
elif(marks >= 70 and marks < 80):
     print("C")
else:
    print("D")##

    #even or odd

 a = int (input("Number1 :"))

if ((a %2 ) == 0):
     print("even number")
else:
     print("Odd number")

 # greast of 4 number
b = int (input("Number2 :"))
c = int (input("Number3 :"))
d = int (input("Number1 :"))


if (a > b and a > c  and a > d ):
    print("a is greatest")
elif(b > a and b > c and b > d):
       print("b is greatest")
elif(c > a and c > b and c > d):
       print("c is greatest")
else:
    print("d is greatest")

#multiple of seven

if((a % 7) == 0):
     print("Multiple of seven")
else:
    print("Not multiple of seven")    

    

    
