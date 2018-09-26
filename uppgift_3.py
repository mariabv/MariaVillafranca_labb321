def is_integer_try(s):
    """ returns True if string is an integer. """
    try:
        int(s)
        return True
    except ValueError:
        return False
print 'This program asks you to type two digital numbers and returns summa of their cubes\n\nSo, let\'s start...\n'
while True:
	a = input('Input a =  ')
	if a == 'q': break
	b = input('Input b =  ')
	if b == 'q': break
	if is_integer_try(a) and is_integer_try(a):
		a=int(a)
		b=int(b)
		print 'a^3 + b^3  = ',a**3+b**3,'\nTo exit type \'q\' please'
	else:
		print 'Sorry, I can calculate only for integers.\nTo exit type \'q\' please'
