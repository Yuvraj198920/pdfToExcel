# Project Name

This is python and React application to convert credit card transaction inside pdf to excel

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3
- Node.js and npm
- Tesseract OCR

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

#### Setting up the Backend

1. **Clone the Repository**

2. **Navigate to the Backend Directory**

3. **Create and Activate a Virtual Environment (optional but recommended)**

- For Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. **Install Required Python Packages**

5. **Install Tesseract OCR**

- For Windows, download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and run it. Note the installation path.
- For macOS, use Homebrew:
  ```
  brew install tesseract
  ```
- For Linux:
  ```
  sudo apt-get install tesseract-ocr
  ```

6. **Configure Tesseract Path (Windows)**

- If you're on Windows, you may need to add the path to the Tesseract executable in your Python script:
  ```python
  import pytesseract
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your path
  ```

2. **Install Node Modules**
   npm install

### Running the Application

Explain how to run the application.

- **To Run the Flask Backend**
  python app.py

- **To Run the React Frontend**
  npm start

#### Setting up the Frontend

1. **Navigate to the Frontend Directory**

## Adding File Upload Capability

1. pip install Flask-uploads
2. Set up file upload route inside app.py

## Possible issues

1. Flask python module is used along with werkzeug 3.0.1. This version of werkzeug has issue with upload file. So recommanded to not to use it
