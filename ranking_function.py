import metapy
import pytoml
import json
import re

def parse_json(file_name):
	with open(file_name, 'r') as file:
		data = json.load(file)
	for candidate in data:
		resume_name = candidate.get('filename')
		resume_text = candidate.get('text')
		cleaned_text = clean_text(resume_text)
		candidate_dict[cleaned_text] = resume_name
	candidate_text_list = list(candidate_dict.keys())
	return candidate_text_list

def clean_text(text):
	text = text.encode('ascii',errors='ignore').decode('utf-8')
	text = re.sub('\s+',' ',text)
	text = text.replace("\n", " ")
	return text

def generate_datafile(candidate_text_list):
	file = open("./resume_set/resume_set.dat", "w")
	for resume_txt in candidate_text_list:
		file.write(resume_txt + "\n")
	file.close()

def get_top_k_candidates(results, candidate_text_list):
	top_k_candidates = []
	for result_tuple in results:
		tmp_list = list(result_tuple)
		text_idx = tmp_list[0]
		text = candidate_text_list[text_idx]
		top_k_candidates.append(candidate_dict[text])
	return top_k_candidates

def ranking_function():
	cfg = "config.toml"
	idx = metapy.index.make_inverted_index(cfg)
	ranker = metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)

	with open(cfg, 'r') as fin:
		cfg_d = pytoml.load(fin)

	query_cfg = cfg_d['query-runner']
	if query_cfg is None:
		print("query-runner table needed in {}".format(cfg))
		sys.exit(1)

	top_k = 3
	query_path = query_cfg.get('query-path', 'queries.txt')

	query = metapy.index.Document()
	print('Running queries')
	with open(query_path) as query_file:
		line = query_file.readline()
		query.content(line.strip())
		results = ranker.score(idx, query, top_k)

	return results

candidate_dict = {}

if __name__ == '__main__':
	candidate_text_list = parse_json("./document/candidate_info.json")
	generate_datafile(candidate_text_list)
	final_result = ranking_function()
	final_candidates = get_top_k_candidates(final_result, candidate_text_list)
	print(final_candidates)
