name = input('enter your name:')
Age = int(input('enter your age:'))

if Age >= 18:
    print('you get beer')
else:
    print('you cannot')
    print("come back after", (18 - Age), "years")

print('hello' , name)
print('your age is' , Age)