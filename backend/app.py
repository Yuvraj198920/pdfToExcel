from flask import Flask, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

from pdf_processing import process_pdf
from data_parsing import parse_transactions
from excel_extraction import create_excel
from flask_cors import CORS


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            extracted_text = process_pdf(file_path)
            transactions = parse_transactions(extracted_text)
            create_excel(transactions, filename="output.xlsx")
            print(extracted_text)
            return '<pre>' + extracted_text + '</pre>'
            # return 'File uploaded and processed. Excel file created.'
        else:
            return 'No valid file provided', 400
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)