def rovarsprak(inrad):
	vokaler = 'aouaeiyaoAOUaEIYao'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	for s in inrad:
		if s in konsonanter:
			utr += s
			utr += 'o'
			utr += s
		else:
			utr += s
	return utr
print (rovarsprak('Att vara eller att inte vara?'))
input('press enter')