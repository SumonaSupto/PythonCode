#dictionary in python {key:value}

info = {
"name":"Sumona",
"reg": 9573,
"id": 2002056,
"subject": "cse"
}
print(info)

#mutable , unodered , access through key, don't allow duplicate key
#list and tuple is allowed as value
#empty dic = {}

print(info["name"])


#method for dictionary

print(info.keys()) #return all key
print(info.values()) #return all value
print(info.items()) # return all pair
print(info.get("subject")) #return the key according to the value
info.update({"city": "barishal"})#insert the additional item
print(info)


#set in python

# made with {}
#set is mutable  but  element is immutable and unordered
#set ignore duplicate value.ex- boy or girl
# list and dictionary is not allowed in set
# empty set = set ()

collection = {1,2,3,4,5}
collection2 = {4,5,6,7,}
print(collection)

#method of set 

collection.add(6)
print(collection)
collection.remove(6)
print(collection)
print(collection.pop()) # pic random value

print(collection.union(collection2)) #unique value

print(collection.intersection(collection2)) #common value