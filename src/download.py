import time
import requests
from clint.textui import progress
from glob import glob

def download_exam(file_dir):
	subject_name = ["sugaku-1a.pdf","sugaku-2b.pdf"]
	
	host_name = "https://www.toshin.com/center/"
	old_path = "/pdf/q/"
	new_path = "/q/"

	download_url_name = []
	for fiscal_year in range(2008,2021,1):
		for sub in subject_name:
			if fiscal_year < 2012:
				url = host_name + str(fiscal_year) + old_path + sub
			elif fiscal_year < 2020:
				url = host_name + str(fiscal_year) + new_path + sub
			elif fiscal_year == 2020 :
				url = host_name.rstrip('/') + new_path + sub
			file_name = str(fiscal_year) + "_" + sub
			download_url_name.append((url, file_name))
	
	file_list = []
	for url, file_name in download_url_name:
		print(file_name + "をダウンロードしています")
		if len(glob(file_dir+'/'+file_name)):
			print("すでにダウンロードされています")
			file_list.append(file_name)
			continue
		print(url+"にアクセスしています..")

		try:
			file_size = int(requests.head(url,timeout=15).headers["content-length"])
		except KeyError:
			file_size = 0
		r = requests.get(url, stream=True, timeout=15)
		if file_size > 0:
			print("接続しました")
			with open(file_dir+file_name,'wb') as f:
				for chunk in progress.bar(r.iter_content(1024), expected_size=(file_size/1024 + 1)):
					f.write(chunk)
					f.flush()
				file_list.append(file_name)
		else:
			print("エラー：ダウンロードできませんでした")
			break
		time.sleep(2)
	return file_list