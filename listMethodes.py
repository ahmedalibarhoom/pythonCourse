a = [1,2,3]

b = [4,5,6]
c = a + b
print(c)

s = 'a b c d e f'
z = s.split()
print(z)

if 'p' in z:
    print('p is in z')
else:
    print('p is not in z')

    for i in z:
        print(i)

        q = [4,2,7,1,3]
        q.sort()
        print(q)
q.reverse()
print(q)
print(q.index(1))
print(len(q))
print(min(q))
print(max(q))