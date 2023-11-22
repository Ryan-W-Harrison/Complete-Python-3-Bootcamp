# class-notes_csv.py

dir_csv = f'{os.getcwd()}/15-PDFs-and-Spreadsheets'

import csv

# openpyxl for excel files

data = open(f'{dir_csv}/example.csv')
data

csv_data = csv.reader(data)
data_lines = list(csv_data)


data = open(f'{dir_csv}/example.csv', encoding = 'utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
data_lines[:3]


for line in data_lines[:5]:
    print(line)


all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)

# pdfs
os.system("pip install PyPDF2")
import PyPDF2

f = open(f'{dir_csv}/Working_Business_Proposal.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)
len(pdf_reader.pages)

page_number = 0
page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
page_one_text
#f.close()

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one);
pdf_output = open(f'{dir_csv}/Some_New_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()


f = open(f'{dir_csv}/Working_Business_Proposal.pdf', 'rb')

pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)
for p in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[0]
    pdf_text.append(page.extract_text())

pdf_text
print(pdf_text[3])
