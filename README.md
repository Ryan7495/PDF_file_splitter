# PDF File Splitter

Splits a pdf file with n pages into n pdfs; each 1 page.
Author: Ryan
Date: 01/25/20

## Requirements

Command line interface for running the program
    
    App: command prompt

python 3 installed
    
install pip by running the below command into your command line interface
    
    python -m pip install --upgrade pip --user
  
  
Install PyPDF2 by running the below command into your command line interface

    python -m pip install PyPDF2 --user
    

## Usage

To split a pdf named `example.pdf` into n pdfs; each pdf is seperate page:
Enter the command below into your command line interface

MacOS:

    python split_pdf.py example.pdf
    
Windows:
    
    ./split_pdf.py example.pdf
