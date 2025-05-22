import PyPDF2

pdf_files = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    with open(filename, 'rb') as f:
        merger.append(f)

merger.write('merged.pdf')
merger.close()
