# Stars - ett program av ...
def triangel_bas_ned(a,b):
	i=0
	s=''
	while b-2*i > 0:
		s=s+((int(b/2)-i+a)*' '+(2*i+1)*'*'+'\n')
		i += 1
	return s;
print (triangel_bas_ned(3,11))
input ("\nPress Enter to exit")