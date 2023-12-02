# pdfToExcel

This is python and React application to convert pdf to excel

## Adding File Upload Capability

1. pip install Flask-uploads
2. Set up file upload route inside app.py

## Possible issues

1. Flask python module is used along with werkzeug 3.0.1. This version of werkzeug has issue with upload file. So recommanded to not to use it

## Steps

1. Create virtual environment
2. Install Flask library
3. Install pdfminer to read pdf
4. Install openpyxl to create excel
