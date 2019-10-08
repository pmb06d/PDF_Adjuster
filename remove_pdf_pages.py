# -*- coding: utf-8 -*-
"""
Created on Thu May 23 17:12:18 2019

@author: pbonnin
"""

from PyPDF2 import PdfFileWriter, PdfFileReader

def get_filepath():
    import tkinter
    from tkinter import filedialog
    root = tkinter.Tk()
    root.withdraw()
    return(filedialog.askopenfilename())

original_file = get_filepath()

# pass a list of page numbers you want to eliminate (page numbering starts from 0)
pages_to_exclude = [14, 15, 16]

# Shows the number of pages in the file
with open(original_file, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        
pages_to_keep = [i for i in list(range(number_of_pages)) if i not in pages_to_exclude]


infile = PdfFileReader(original_file, 'rb')

output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)


output_file = get_filepath()
with open(output_file, 'wb') as f:
    output.write(f)
    