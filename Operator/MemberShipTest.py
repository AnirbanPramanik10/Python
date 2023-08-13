s = "geeksforgeeks"

print("g" in s)  # checking for "g" in s

print("for" in s)  # checking for "for" in s

print("gk" in s)

############################################

d = {10: "abc", 20: "efg"}

print(10 in d)  # key 10 is in d

print(15 in d)  # key 15 is not in d

print("abc" in d)  # in look for key, so key "abc" not in d


###########################################

l = [10, 20, 30, 15]

print(30 in l)  # 30 is in list l

print([20, 30] in l)  # [20,30] is a list, which is not in l


##########################################

l = [10, 20, 30, 15]

print(30 not in l)

print(40 not in l)

print([20, 30] not in l)
