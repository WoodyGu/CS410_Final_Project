import os

def parse_filename(filename_w_ext):
    filename, file_extension = os.path.splitext(filename_w_ext)
    return filename

def create_pdf_document(filename):
    file_path = './resume/' + filename
    text_source = readpdf.convert_pdf_to_txt(file_path)
    text_store_path = './document/' + utils.parse_filename(filename)
    with open(text_store_path, 'r') as txt_file:
        txt_file.write(text_source)
