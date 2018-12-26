#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 22:49:54 2018

@author: amadsalmon
"""

from PyPDF2 import PdfFileReader, PdfFileWriter


def main():
    RECTOVERSO = PdfFileWriter()

    RECTO = PdfFileReader(open('RECTO.pdf', 'rb'))
    VERSO = PdfFileReader(open('VERSO.pdf', 'rb'))

    nbPagesInRecto = RECTO.getNumPages()
    nbPagesInVerso = VERSO.getNumPages()
 
    #print("\n", "nbPagesInVerso : ", nbPagesInVerso, "\n")

 
    for i in range(nbPagesInRecto):
        print("Index i = ", i, end='\n')
        if ((nbPagesInRecto - nbPagesInVerso) == 1) and (i == nbPagesInRecto-1):
            page = RECTO.getPage(i)
            RECTOVERSO.addPage(page)
            print("ADDED FINAL RECTO PAGE NUMBER ", i, end='\n')

        else:
            page = RECTO.getPage(i)
            RECTOVERSO.addPage(page)
            print("ADDED RECTO PAGE NUMBER ", i, end='\n')
            
            #reversedPageNumber = nbPagesInVerso - i -1
            #print("\n", "reversedPageNumber : ", reversedPageNumber, "\n")
            #page = VERSO.getPage(reversedPageNumber)
            
            page = VERSO.getPage(nbPagesInVerso-1-i)
            
            
            RECTOVERSO.addPage(page)
            print("ADDED VERSO PAGE NUMBER ", -i, end='\n')

 
    with open('RECTOVERSO.pdf', 'wb') as f:
        RECTOVERSO.write(f)

main()