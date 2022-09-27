import PyPDF4

def split(pdf_list,dir_name):
	pdf_path = [dir_name + '/' + f for f in pdf_list]
	merger = PyPDF4.PdfFileMerger()