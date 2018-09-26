def visksprak(inrad):
	vokaler = 'aoueiyAOUEIY'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	for s in inrad:
		if s not in vokaler:
			utr += s
	return utr
print (visksprak('Far jag viska ditt namn?'))
input('press enter')
