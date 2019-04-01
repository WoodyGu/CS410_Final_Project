from flask import Flask
import readpdf

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/text/<filename>', methods=['GET'])
def get_pdf_content(filename):
    file_path = './resume/' + filename
    return readpdf.convert_pdf_to_txt(file_path)

if __name__ == '__main__':
    app.run()
