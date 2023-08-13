a = 10
b = 1.5
print(a + b)

d = True
e = a + d
print(e)

d = False
e = a + d
print(e)

###################


s = '135'

i = 10 + int(s)  # str to int conversion

f = float(s)  # str to float conversion

print(i)
print(f)


####################

s = "Anirban"
print(list(s))
print(set(s))
print(tuple(s))

###################


l = ['a', 'b', 'c']

print('list to str', str(l))

a = 10

b = 11

print('int to str,', str(a) + str(b))

c = 12.5

print('float to str', str(c))

##################

t = (10, 20, 30)

print('tuple to list', list(t))

s = {10, 20, 30}

print('set to list', list(s))


################

# int to binary

a = 20

print('int to binary 20-->', bin(a))

print('int to hexa 20-->', hex(a))

print('int to octa 20-->', oct(a))


################

# int to binary

a = "1000101"

print('binary to int', int(a, 2))  # base is 2

b = "12"

print('oct to int', int(b, 8))  # base is 8

c = "A1"

print('hexa to int', int(c, 16))    # base is 16

