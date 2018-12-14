from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.image('files/modified_png.png', 20, 50, 250, 100)
pdf.output('files/png.pdf', 'F')