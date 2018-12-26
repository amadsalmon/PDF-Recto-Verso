# PDF Recto Verso
PDF Recto Verso is a tool developed in Python to assemble two recto and verso PDF files into a single Recto-Verso PDF.
This helps you when your photocopier does not automatically scan the recto AND the verso of your documents.

## Requirements 
PDF Recto Verso is developed upon the PyPDF2 Python module. You need to have PyPDF2 in your framework in order to use PDF Recto Verso.
You can install PyPDF2 with the ```pip``` command. Open your terminal and type the following command:
```$ pip install PyPDF2```
## How to use it?
- Scan all the rectos of your document into a PDF file named RECTO.pdf
- Scan all the versos of your document into a PDF file named VERSO.pdf
- Place RECTO.pdf and VERSO.pdf in the same folder as the Python code file.
- Execute the Python code file (in a Terminal or in your IDE)
- The output file is in the same folder as the Python code file, as a PDF named RECTOVERSO.pdf! And you're done.

Now you may have noticed there are two versions of the code. One is called "normal" and the other "reversed".
The reversed version works for when you scanned your versos in a reversed order (the first page of the PDF is the last page of the document). If you

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
