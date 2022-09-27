from download import download_exam
from split import split
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--d",help="please input the folder path in which you want to save your pdf",type=str)
	args = parser.parse_args()

	if args.d:
		save_dir = args.d
	else:
		save_dir = "./"
	
	pdf_list = download_exam(save_dir)
	# split(pdf_list,save_dir)

if __name__ == "__main__":
	main()