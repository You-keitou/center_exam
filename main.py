from src.download import download_exam
import src.split as sp
import argparse
import os

def main():
	#コマンドライン引数
	parser = argparse.ArgumentParser()
	#フラグの追加　保存先ディレクトリーの指定
	parser.add_argument("--d",help="please input the folder path in which you want to save your pdf",type=str)
	args = parser.parse_args()
	#コマンドライン引数が渡されているのなら、それを保存先のディレクトリに指定
	if args.d:
		save_dir = args.d
		os.makedirs(save_dir, exist_ok=True)
	else:
	#そうでないなら、カレントディレクトリを保存先に指定
		save_dir = "./"
	
	pdf_list = download_exam(save_dir)

	for ob in pdf_list:
		a = sp.center_exam(ob)
		try:
			a.split(save_dir)
		except:
			try:
				a.split_into_one(save_dir)
			except:
				a.split_into_one(save_dir,repeat_open=True)
if __name__ == "__main__":
	main()