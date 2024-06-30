print ("sumona" , "supto")
print (23+55)
name= "Jahid Sajal"
age=24
love= 100.1
print ("My hubby's name is:",name,)
print ("His age is:",age)
print ("He loves me:",love,"%")
print (type(name))
print(type(age))
print(type(love))
#relational operator always gives true or false
print (name==age)#false
print (name!=age)#true
#some special assingment operator (=,+=,-=,*=,/=,%=,**=)
age += 20
print (age)#work of +=
#logical operator not , and ,or
#not for single value 
print (not False) #ex
print (not(age <love))
#and true when both true
#or when one is true
#False  when both are false
#type conversion (atomatic), type casting (by force)
#input("Enter your name:")
name2 = input("Enter your name:")
print ("My name is :", name2)
# input is always str so we have to typecast to define the type

age2= int(input("Enter your age:"))
print ("My age is :", age2)

