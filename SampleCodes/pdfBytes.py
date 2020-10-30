
from sys import argv
import base64

script, filename = argv

file_path = 'files/{}'.format(filename)

print("Here's your file {}".format(file_path))


with open(file_path, 'rb') as pdf_file:
    encode_pdf = base64.b64encode(pdf_file.read())
    print(encode_pdf[:20], len(encode_pdf), encode_pdf[-20:])
    if isinstance(encode_pdf, bytes):
        encode_pdf = encode_pdf.decode('utf-8')

print(encode_pdf[:20], encode_pdf[-20:])

with open('files/output.pdf', 'wb') as pdf_file:
     pdf_file.write(base64.b64decode(encode_pdf))
