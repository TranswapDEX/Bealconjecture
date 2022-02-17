from random import randint

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6

x = (a**d) + (b**e)
y = c**f

aL = [1]
bL = [1]
cL = [1]
dL = [1]
eL = [1]
fL = [1]

while x != y:
		a = randint(1, 100)
		#while b % a == 0 or a % b == 0:	
		b = randint(1, 100)
		#while c % a == 0 or c % b == 0 or b % c == 0 or c % b == 0:
		c = randint(1, 100)
		d = randint(3, 100)
		e = randint(3, 100)
		f = randint(3, 100)
		x = (a**d) + (b**e)
		y = c**f
		aL[0] = a
		bL[0] = b
		cL[0] = c
		dL[0] = d
		eL[0] = e
		fL[0] = f

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)



'''
a = 0

for i in range(100000000):
	if i % 2 == 0:
		a = a + 1

print(a)

'''
