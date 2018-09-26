def allsprak(inrad):
	vokaler = 'aouaeiyaoAOUaEIYao'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	aa = []
	for word in inrad.split():
		bb = ""
		nw = ""
		log = True
		for s in word:
			if s in konsonanter and log:
				bb += s
			elif s in vokaler and log:
				nw += s
				log = False
			else:
				nw += s
		aa.append(nw+bb+'all')
	utr = ' '.join(aa)
	return utr
print (allsprak('frostig vinter'))
input('press enter')
