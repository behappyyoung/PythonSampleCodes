# -*- coding: utf-8 -*-
from xhtml2pdf import pisa

import cStringIO as StringIO

HTML = """
        <!DOCTYPE html>
        <html>
            <body>
            <p>
            You are being offered a blood test that looks at your genetic material (DNA). The goal of this test is to better understand your
            \/your child&quote;s medical condition.
This form summarizes the key points, risks and bene ts of this test so that you can make an informed decision about whether or not to have this test. Other test options may be available. 
Please discuss any questions with your doctor and/or genetic counselor.
<strong>What is exome/genome testing?</strong>
</p>
<p>
Exome or genome testing (called “genomic testing”) examines many genes in your body to look for a genetic cause for your health issues. Our genes are tiny instructions in our cells that determine who we are. They in uence things like whether we are tall or short or have blue or brown eyes. Sometimes they also in uence whether we will develop a certain illness.
</p>
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