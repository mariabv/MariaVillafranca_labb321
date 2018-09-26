# Stars - ett program av ...
def triangel_bas_ned(a,b):
	i=0
	while b-2*i > 0:
		print((int(b/2)-i+a)*' '+(2*i+1)*'*')
		i += 1
triangel_bas_ned(2,9)
input ("\nPress Enter to exit")