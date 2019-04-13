import os

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

def create_pdf_document(filename):
    file_path = './resume/' + filename
    text_source = readpdf.convert_pdf_to_txt(file_path)
    text_store_path = './document/' + utils.parse_filename(filename)
    with open(text_store_path, 'r') as txt_file:
        txt_file.write(text_source)
