import PyPDF4
import os

class	center_exam:

	def __init__(self,file_name) -> None:
		self.file_name = file_name
		self.year = int(self.file_name[:4])
		self.kind = self.file_name[12:14]
		if  self.year < 2015 and self.kind == "1a":
			self.category = ["式の計算","集合","二次関数","三角比の応用","確率"]
			self.page = [(2,3),(3,4),(4,6),(6,8),(8,10)]
			self.merge_order = [(x,y) for x,y in zip(self.category,self.page)]

	def split(self,dir_name):
		pdf_path = os.path.join(dir_name ,self.file_name)
		for category, pagerange in self.merge_order:
			merger = PyPDF4.PdfFileMerger()
			merger.append(pdf_path, pages=pagerange)
			save_dir = os.path.join(dir_name,self.kind,category)
			os.makedirs(save_dir, exist_ok=True)
			merge_pdf_path = os.path.join(save_dir,str(self.year) +".pdf")
			merger.write(merge_pdf_path)
			merger.close
	
	def split_into_one(self,dir_name,repeat_open=False):
		pdf_path = os.path.join(dir_name ,self.file_name)
		reader = PyPDF4.PdfFileReader(pdf_path)
		num_pages = reader.getNumPages()
		save_dir = os.path.join(dir_name,self.kind)
		os.makedirs(save_dir, exist_ok=True)
		for i in range(num_pages):
			if repeat_open:
				reader = PyPDF4.PdfFileReader(pdf_path)
			page = reader.getPage(i)
			writer = PyPDF4.PdfFileWriter()
			new_pdf_path = os.path.join(save_dir,str(self.year) + "_" + str(i+1) +".pdf")
			writer.addPage(page)
			with open(new_pdf_path, mode="wb") as f:
				writer.write(f)