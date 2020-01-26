"""
Splits a pdf file with n pages into n pdfs; each 1 page.
Author: Ryan Sawchuk
Date: 01/25/20
"""

import PyPDF2

import os
import sys

# If command line args dont wokr you can change the value
# of PDF to the file you want to split.
# Make sure you change the code from sys.argv[1] to PDF.
PDF = "example.pdf"
PATH = os.getcwd()
DIR_PATH = ""
# For windows you might have to change SLASH to `\`
SLASH = "/" # "\"

# Help menu
def help_message():
    print "To split a pdf named `example.pdf` into n pdfs; each pdf is seperate page:"
    print ""
    print "Usage: python split_pdf.py example.pdf"
    print ""
  
# Test if the user specified any arguments
if len(sys.argv[1:]) == 0:
    help_message()
    sys.exit(0)

# If Windows and MacOS
if os.name == "nt":
    pass

# Open given pdf for reading in binary
try:    # can replace sys.argv[1] with PDF
    pdf_file = open(sys.argv[1], "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    print(PATH)
    DIR_PATH = PATH + SLASH + os.path.splitext(pdf_file.name)[0]
    
    if os.path.isdir(DIR_PATH):
        os.rmdir(DIR_PATH)
    
    os.mkdir(DIR_PATH)
    print(DIR_PATH)
    
    
except IOError: # python 3 vs 2
    print("Unable to load: %s" % sys.argv[1])
    #print "Unable to load %s" % (sys.argv[1])
    sys.exit(0)
    
except OSError:
    print("Unable to make folder: %s" % os.path.splitext(pdf_file.name)[0])
    #print "Unable to make fold: %s" % os.path.splitext(pdf_file.name)[0]
    #sys.exit(0)


for page in range(pdf_reader.numPages):
    # read each page into a different pdf file
    print "page: %d" % (page)
    
    try:
        # Try and open a new pdf
        name = DIR_PATH + SLASH + "page" + str(page) + ".pdf"
        new_pdf = open(name, "wb")
        
        # Try and write a page to a new pdf
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))
        pdf_writer.write(new_pdf)
        new_pdf.close()
        
    except IOError:
        print("Unable to write: %s" % name)
    
# Close opened file
pdf_file.close()
    
    

