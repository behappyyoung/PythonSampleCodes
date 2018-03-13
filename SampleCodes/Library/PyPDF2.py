import PyPDF2, re

try:
        pdf_file = ''
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        page_content = re.sub(r'\n', '', read_pdf.getPage(0).extractText())


except Exception as e:
        message = 'Error - Cannot confirmed PDF Contents'
