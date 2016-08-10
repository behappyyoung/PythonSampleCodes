from sys import argv
import zlib, base64
f = open('row_text.txt')
txt = f.read()
print(txt, len(txt))

comtext = zlib.compress(txt, 9)
print(comtext, len(comtext))
backtxt = zlib.decompress(comtext)
print(backtxt, len(backtxt))
if txt == backtxt:
	print('correct')
else:
	print('wrong')

# with base64 encoding
code = base64.b64encode(zlib.compress(txt, 9))
print(code, len(code))
backtxt2 = zlib.decompress(base64.b64decode(code))
print(backtxt2, len(backtxt2))
if txt == backtxt:
	print('correct')
else:
	print('wrong')