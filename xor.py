#!/usr/bin/python3

import sys
from itertools import cycle, izip
from binascii import hexlify

def main():
	if len(sys.argv) != 3:
		usage()
	try:
		(key,fname) = sys.argv[1:]
	except Exception as e:
		print("[x] Error while parsing args")
		print("%s" % e)
		return
	sys.stderr.write("k: %s, fname: %s\n" % (key, fname))
	sys.stderr.write("k: 0x%s\n" % hexlify(key))
	sys.stderr.flush()


	with open(fname, "rb") as f:
		data=f.read()

	sys.stdout.write(xor(data, key))
	sys.stdout.flush()
	return


def usage():
	print("usage: %s <key> <filename>" % sys.argv[0])
	print("example: %s 's3cr3t' /etc/passwd" % sys.argv[0])
	sys.exit()


def xor(data, key):
	return ''.join(chr(ord(a)^ord(b)) for (a,b) in izip(data, cycle(key)))
	

if __name__=='__main__':
	main()
