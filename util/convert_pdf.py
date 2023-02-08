import pdfplumber
from util import remove_spaces


PDF_PATH = "text_files/x.pdf"
TXT_PATH = "text_files/txt/x.txt"


with pdfplumber.open(PDF_PATH) as pdf:
    
    total_num_pages = len(pdf.pages)
    print(f'total number of pages: {total_num_pages}')
    
    text = ''
    for i in range(total_num_pages):
        current_page = pdf.pages[i]
        
        # # only for the third volume
        # raw = current_page.extract_text()
        # raw_without_first_line = '\n'.join(raw.split('\n')[1:]) 
        # text += remove_spaces(raw_without_first_line) + '\n'
        
        text += remove_spaces(current_page.extract_text()) + '\n'

# write to file
with open(TXT_PATH, 'w') as f:
    f.write(text)
print('done.')
    