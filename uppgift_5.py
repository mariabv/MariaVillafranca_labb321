def is_integer_try(s):
    try:
        int(s)
        return True
    except ValueError:
        return False;
		
def rama (sum):
	sum = int(sum)
	am = sum
	j = 0
	b = 1 
	kb = 1
	aa = []
	bb = []
	while kb < sum and b < am:
		m = sum - kb
		a = 1
		ka = 1
		while ka <= m:
			if ka == m:
				aa.append(a)
				bb.append(b)
				j += 1
				am = a
				break
			else:
				a += 1
				ka = a**3
		b += 1
		kb = b**3
	if j == 0:
		ret = '[]'
	elif j == 1:
		ret = '[('+str(aa[0])+','+str(bb[0])+')]'
	else:
		ret = '[('+str(aa[0])+','+str(bb[0])+'),('+str(aa[1])+','+str(bb[1])+')]'
	return ret;
	
print ('This program checks if a solution in natural numbers exists for equation a^3 + b^3  = n\n\n')
n = input('n = ')
if is_integer_try(n):
	n = int(n)
	if n > 0:
		print (rama(n))
	else:
		print ('Sorry, I can calculate only for natural numbers.\n')
else:
	print ('Sorry, I can calculate only for integer numbers.\n')
input('Press ENTER to exit, please')