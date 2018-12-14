import PyPDF2 as pypdf

try:
    output_file = pypdf.PdfFileWriter()
    message = 'read pdf file'
    pdf_file = 'files/etrade.pdf'
    water_file = 'files/html.pdf'
    with open(pdf_file, "rb") as inFile, open(water_file, "rb") as overlay:
        read_pdf = pypdf.PdfFileReader(inFile)
        background = read_pdf.getPage(0)
        water_pdf = pypdf.PdfFileReader(overlay).getPage(0)

        background.mergePage(water_pdf)
        output_file.addPage(background)
        with open("modified.pdf", "wb") as outFile:
            output_file.write(outFile)
    # page_content = re.sub(r'\n', '', read_pdf.getPage(0).extractText())
    # page_content = read_pdf.getPage(0)
    # print(pdf_file, page_content)
    # read_pdf.mergePage(water_pdf.getPage(0))
    # output_file.addPage(read_pdf)
    # with open("../files/document-output.pdf", "wb") as outputStream:
    #     output_file.write(outputStream)

except Exception as e:
    print(e)
    message = 'Error - Cannot confirmed PDF Contents'

print(message)