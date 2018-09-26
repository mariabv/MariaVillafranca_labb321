def rovarsprak(inrad):
	vokaler = 'aouaeiyaoAOUaEIYao'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	i = 0
	for s in inrad:
		if s in konsonanter and i == 0:
			utr += s
			i = 2
		elif i == 0:
			utr += s
		else:
			i -= 1
	return utr
print (rovarsprak('Atottot vovarora elolloleror atottot inontote vovarora?'))
input('press enter')
