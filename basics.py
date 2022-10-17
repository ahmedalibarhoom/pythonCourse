b = 10
a = 10

print(id(a),id(b))

num1 = 100
print(type(num1))

num2 = 15.25
print(type(num2))

s = 'python'' ''sample'' string'
print(s)
print(type(s))
print(id(s))

s = 'new word'
print(s)
print(type(s))
print(id(s))


a = [10,20,30,40,'python','dang']
print(a)
print(id(a))
a.append(60)
print(a)
print(id(a))


t = (10,20,30)
print(t)

d = {'name':'ahmed','email':'ahmed.com','age':28}
print(d)

help(str)