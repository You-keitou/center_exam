import time
import requests
from clint.textui import progress

def download_exam(file_dir):
	subject_name = ["sugaku-1a.pdf","sugaku-2b.pdf"]
	old_path = "/pdf/q/"
	new_path = "/q/"
	kyotsu_path = "/data/285/"
	host_name = "https://www.toshin.com/center/"
	host_name_kyotu = "https://www.toshin.com/kyotsutest/"

	download_path_name = []
	for fiscal_year in range(2008,2022,1):
		for sub in subject_name:
			if fiscal_year < 2012:
				download_path_name.append((host_name + str(fiscal_year) + old_path + sub, str(fiscal_year) + "_" + sub))
			elif fiscal_year < 2020:
				download_path_name.append((host_name + str(fiscal_year) + new_path + sub, str(fiscal_year) + "_" + sub))
			else :
				download_path_name.append((host_name_kyotu + str(fiscal_year) + kyotsu_path + sub, str(fiscal_year) + "_" + sub))

	
	for url, file_name in download_path_name:
		print(file_name + "をダウンロードしています")
		print(url+"にアクセスしています..")

		file_size = int(requests.head(url,timeout=10).headers["content-length"])
		r = requests.get(url, stream=True, timeout=10)
		if file_size > 0:
			print("接続しました")
			with open(file_dir+file_name,'wb') as f:
				for chunk in progress.bar(r.iter_content(1024), expected_size=(file_size/1024 + 1)):
					f.write(chunk)
					f.flush()
		else:
			print("エラー：ダウンロードできませんでした。")
			break
		time.sleep(5)
