def bebisprak(inrad):
	vokaler = 'aouaeiyaoAOUaEIYao'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	aa = []
	for word in inrad.split():
		bb = ""
		log = True
		for s in word:
			if s in konsonanter and log:
				bb += s
			elif s in vokaler and log:
				bb += s
				log = False
		aa.append(bb+bb+bb)
	utr = ' '.join(aa)
	return utr
print (bebisprak('naringsrik mat ar god'))
input('press enter')
