'''
Install Xvfd:

$ sudo apt-get install xvfb
yum install xorg-x11-server-Xvfb

Install Fonts:

$ sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

Install wkhtmltopdf:

$ sudo apt-get install wkhtmltopdf
yum install wkhtmltopdf


wkhtmltopdf (OSX)
Install wkhtmltopdf:

$ brew install wkhtmltopdf

brew install Caskroom/cask/wkhtmltopdf


pip install html2pdf

'''


# from wkhtmltopdf import HTMLURLToPDF

# make_pdf = HTMLURLToPDF(
#     url='https://stanfordhealthcare.org/',
#     output_file='files/shc.pdf',
# )
# make_pdf.render()

from html2pdf import HTMLToPDF

output_file = 'hello.pdf'

HTML = """
    <!DOCTYPE html>
    <html>
        <body>
        <h1>Hello World</h1>
        </body>
    </html>
"""

h = HTMLToPDF(HTML, output_file)