#Boy or girl
name = input()
mod = len(set(name))%2

if (mod == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")