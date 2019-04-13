import os
import json
import readpdf

def parse_filename(filename_w_ext):
    filename, file_extension = os.path.splitext(filename_w_ext)
    return filename

def parse_candidate(pdf_file_list):
    candidate_list = []
    for candidate in pdf_file_list:
        candidate_name = parse_filename(candidate).split('_')
        print(candidate_name)
        candidate_first = candidate_name[0]
        candidate_last = candidate_name[1]
        candidate_link = candidate
        candidate_obj = {'first': candidate_first,'last':candidate_last,'link':candidate_link}
        candidate_list.append(candidate_obj)
    return candidate_list

def create_txt_document(filename):
    file_path = './resume/' + filename
    text_source = readpdf.convert_pdf_to_txt(file_path)
    text_store_path = './document/' + utils.parse_filename(filename)
    with open(text_store_path, 'w') as txt_file:
        txt_file.write(text_source)

def create_json_document():
    all_candidate = []
    pdf_file_list = os.listdir('./resume/')
    for file_w_ext in pdf_file_list:
        filename = parse_filename(file_w_ext)
        file_path = './resume/' + file_w_ext
        candidate_content = readpdf.convert_pdf_to_txt(file_path)
        json_obj = {"filename":file_w_ext, "text":candidate_content}
        all_candidate.append(json_obj)
    return all_candidate

if __name__ == "__main__":
    # all_candidate = create_json_document()
    # with open("./candidate_info.json", 'w') as fd:
    #     json.dump(all_candidate, fd)
    with open("./document/candidate_info.json", 'r') as file:
        data = json.load(file)
        print(type(data[0]))
