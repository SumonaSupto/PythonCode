#list and tupple {array}
marks = [40 , 20, 70 , 80]
print(marks)
print(len (marks))
print(marks[2])
#list is like string bt list is mutable and string is immutable
marks[0] = 50
print(marks)
#slicing of list
print(marks[1:3])
#methosd in list

marks.append(10) #add element at the end
print(marks)
marks.sort() #ascending
print(marks)
marks.sort(reverse=True) #decending
print(marks)
marks.reverse()
print(marks)
marks.insert(2,1000)
print(marks)
marks.remove
print(marks)
marks.pop(2)
print(marks)


#tuple is a built-in data type like list but tuples is immutable unlike list

tup = (1,2 ,3,) #start with ()
print(type(tup))