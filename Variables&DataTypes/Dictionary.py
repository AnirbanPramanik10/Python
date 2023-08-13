d = {101: "abc", 102: "def", 103: "ghi", 104: "jkl"}
print(d)

d = {}
d["Laptop"] = 40000
d["Mobile"] = 15000
d["Earphone"] = 1000
print(d)

d = {110: 'abc', 101: 'xyz', 105: 'pqr'}
print(d.get(110))
print(d.get(125))
print(d.get(125, "NA"))

##############################

if 125 in d:
    print(d[125])
else:
    print("NA")

################################

d = {110: 'abc', 101: 'xyz', 105: 'pqr', 106: 'bcd'}

d[101] = "mno"
print(d)

# print('returning and removing 105', d.pop(105))
print(d.pop(105))

del d[106]
print(d)

d[108] = "cde"
print(d)

print('returning and removing last inserted', d.popitem())