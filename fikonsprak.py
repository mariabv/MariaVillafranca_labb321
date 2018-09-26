def fikonsprak(inrad):
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
				bb += s
				log = False
			else:
				nw += s
		aa.append('fi'+nw+bb+'kon')
	utr = ' '.join(aa)
	return utr
print (fikonsprak('anna och cissi springer en mil'))
input('press enter')
