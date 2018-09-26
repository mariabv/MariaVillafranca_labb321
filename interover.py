#!/usr/bin/python3
import sys
def allsprak(inrad):
	vokaler = 'aouaeiyaoAOUaEIYao'
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
	vokaler = 'aouaeiyaoAOUaEIYao'
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
	vokaler = 'aouaeiyaoAOUaEIYao'
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
def visksprak(inrad):
	vokaler = 'aouaeiyaoAOUaEIYao'
	konsonanter = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	utr = ""
	for s in inrad:
		if s not in vokaler:
			utr += s
	return utr
while True:
	arg = input ('Vilket sprak onskas?\n1 Visk 2 Rovar 3 Bebis\n4 All 5 Fikon 6 Avsluta programmet\n\n')
	if arg=='4':
		test = input ('Din mening: ')
		print ('Allspraket: ',allsprak(test),'\n')
		continue	
	elif arg=='3':
		test = input ('Din mening: ')
		print ('Bebispraket: ',bebisprak(test),'\n')
		continue	
	elif arg=='5':
		test = input ('Din mening: ')
		print ('Fikonspraket: ',fikonsprak(test),'\n')
		continue	
	elif arg=='2':
		test = input ('Din mening: ')
		print ('Rovarspraket: ',rovarsprak(test),'\n')
		continue	
	elif arg=='1':
		test = input ('Din mening: ')
		print ('Viskspraket: ',visksprak(test),'\n')
		continue	
	elif arg=='6':
		break
	else:
		continue