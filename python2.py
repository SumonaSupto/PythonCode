#All the power is within You...
#You can do anything and everything...(Swami Vivekananda)
str1 = "my name is Sumona.\nI am a Programmer"
str2 = "\nI am learning Python"
print(str1) #print str
print( str1+str2 ) #concatinate str
str3 = str1+str2
print(len (str3)) # length of the str.space is not ignored
#indexing
print(str3[5])
#slicing
print(str3[2:5]) #ending is not included
#negative indexing only for slicing
print(str1[-10:-1])
#function
print (str1.endswith("er")) #true
print(str1.capitalize()) 
print(str2.replace("Python","Java"))
print(str1.find("Sumona"))
print(str1.count("Sumona"))

#conditional statement
age = int(input("Enter your age :"))
if (age > 18):
    print("You can vote")
elif (age < 18):
    print("You cant't vote")  #indentation = proper spaceing (use replace of {})
else :
    print("Equal")

#nesting
    
    age = int(input("Enter your age :"))
if (age > 18):
    if(age > 90):
        print("You can't vote")
    else:
        print("You can vote")
  
elif (age < 18):
    print("You cant't vote")  
else :
    print("Equal")
    