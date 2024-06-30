#take input create list

movie = []
movie.append(input("Enter movie1:"))
movie.append(input("Enter movie2:"))
movie.append(input("Enter movie3:"))

print (movie)

#palindrom or not

list =[]
list.append(input("Enter:"))
list.append(input("Enter:"))
list.append(input("Enter:"))
list.append(input("Enter:"))

copy1 = list.copy()
copy1.reverse()

if(copy1 == list):
    print("this is palindrom")
else:
    print("Not palindrom")

