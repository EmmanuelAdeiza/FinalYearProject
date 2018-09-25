# CONVERT PDF INTO TEXT USING PYTHON

import pyPdf


def getPDFContent(path):
    content = ""
    num_pages = 1

    # PATH OF THE PDF FILE
    p = file("/home/jayakrishnan/finalcode//sad.pdf", "rb")
    pdf = pyPdf.PdfFileReader(p)
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content


# OPEN THE TEXT FILE
f = open('test.txt', 'w')

# CALL THE FUNCTION AND PASS THE PDF FILE
pdfl = getPDFContent("sample.pdf").encode("ascii", "ignore")
f.write(pdfl)
f.close()