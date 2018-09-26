#!/usr/bin/python3
import sys
def allsprak(inrad):
	vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	j = 0
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
		j += 1
	utr = ' '.join(aa)
	return utr
def bebisprak(inrad):
	vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	j = 0
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
		j += 1
	utr = ' '.join(aa)
	return utr
def fikonsprak(inrad):
	vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	j = 0
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
		j += 1
	utr = ' '.join(aa)
	return utr
def overrovarsprak(inrad):
	vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
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
def rovarsprak(inrad):
	vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
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
def visksprak(inrad):
	vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	for s in inrad:
		if s not in vokaler:
			utr += s
	return utr
test= input()
for arg in sys.argv[1:]:
	if arg=='-h':
		print ('\nThe program translates the sentence to different languages')
		print ('Use parameters:')
		print ('-a allspråket, -b bebispråket, -f fikonspråket, -r rövarspråket, -o överrövarspråket, -v viskspråket')
		print ('The example of usage:')
		print ('To translate to rövarspråket you can type')
		print ('> oversattning.py -r')
		print ('and input the sentence to translate below')
	elif arg=='-a':
		print (allsprak(test))
	elif arg=='-b':
		print (bebisprak(test))
	elif arg=='-f':
		print (fikonsprak(test))
	elif arg=='-r':
		print (rovarsprak(test))
	elif arg=='-o':
		print (overrovarsprak(test))
	elif arg=='-v':
		print (visksprak(test))
	else:
		print ('For the translation set the language. Type \'oversattning.py -h\'  for more details.')
if len(sys.argv) <= 1:
    print ('For the translation set the language. Type \'oversattning.py -h\'  for more details.')
