from flask import Flask
from flask_cors import CORS
from flask import send_file
import gunicorn
import readpdf
import ranking_function
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
    # pdf_file_list = os.listdir('./resume/')
    with open("queries.txt", 'w') as fd:
        fd.write(str(query))
    candidate_text_list = ranking_function.parse_json("./document/candidate_info.json")
    ranking_function.generate_datafile(candidate_text_list)
    final_result = ranking_function.ranking_function(6)
    final_candidates = ranking_function.get_top_k_candidates(final_result, candidate_text_list, 6)
    qualified_candidate = utils.parse_candidate(final_candidates)
    return json.dumps(qualified_candidate)

@app.route('/api/file/<filename>')
def get_pdf_file(filename):
    file_path = './resume/' + filename
    try:
        return send_file(file_path,attachment_filename=filename)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
