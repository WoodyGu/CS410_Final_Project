from flask import Flask
from flask_cors import CORS
from flask import send_file
import gunicorn
import readpdf
import utils
import json
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/text/<filename>', methods=['GET'])
def get_pdf_content(filename):
    file_path = './resume/' + filename
    return readpdf.convert_pdf_to_txt(file_path)

@app.route('/api/ranking/<query>', methods=['GET'])
def rank_documents(query):
    pdf_file_list = os.listdir('./resume/')
    candidate_list = utils.parse_candidate(pdf_file_list)
    return json.dumps(candidate_list)

@app.route('/api/file/<filename>')
def get_pdf_file(filename):
    file_path = './resume/' + filename
    try:
        return send_file(file_path,attachment_filename=filename)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
