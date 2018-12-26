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
 
 
    for i in range(nbPagesInRecto):
        if ((nbPagesInRecto - nbPagesInVerso) == 1) and (i == nbPagesInRecto):
            page = RECTO.getPage(i)
            RECTOVERSO.addPage(page)

        else:
            page = RECTO.getPage(i)
            RECTOVERSO.addPage(page)

            page = VERSO.getPage(i)
            RECTOVERSO.addPage(page)

 
    with open('RECTOVERSO.pdf', 'wb') as f:
        RECTOVERSO.write(f)

main()