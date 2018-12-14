from xhtml2pdf import pisa

import cStringIO as StringIO

HTML = """
        <!DOCTYPE html>
        <html>
            <body>
            <h1>Hello World</h1>
            </body>
        </html>
    """
# result = StringIO.StringIO()
# pdf = pisa.pisaDocument(StringIO.StringIO(HTML), dest=result)
resultFile = open('files/ghtml.pdf', "w+b")
pisaStatus = pisa.CreatePDF(HTML,dest=resultFile)
resultFile.close()
print(pisaStatus)

# print(pdf, result, result.getvalue())