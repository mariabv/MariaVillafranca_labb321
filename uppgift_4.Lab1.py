sol=True
print ('This program checks if a solution in natural numbers exists for equation a^3 + b^3  = n\n\n')
n = input('n = ')
n = int(n)
am=n
b = 1
kb = 1
while kb < n and b < am:
    m = n - kb
    a = 1
    ka = 1
    while ka <= m:
        if ka == m:
			print 'a =',a,',  b =',b
			am=a
			sol=False
			break
        else:
			a += 1
			ka = a**3
			continue
	b += 1
	kb = b**3
	continue
if sol:
	print ('Sorry, no solution is found.\n')
input('Press ENTER to exit, please')
