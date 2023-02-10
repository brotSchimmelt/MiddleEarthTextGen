import pdfplumber
from helper import remove_spaces


INPUT_PDF_PATH = "../text_files/x.pdf"
OUTPUT_TXT_PATH = "../text_files/txt/x.txt"


with pdfplumber.open(INPUT_PDF_PATH) as pdf:
    
    total_num_pages = len(pdf.pages)
    print(f'total number of pages: {total_num_pages}')
    
    text = ''
    for i in range(total_num_pages):
        current_page = pdf.pages[i]
        
        # # only for the third volume
        # # skip first line on each page
        # raw = current_page.extract_text()
        # raw_without_first_line = '\n'.join(raw.split('\n')[1:]) 
        # text += remove_spaces(raw_without_first_line) + '\n'
        
        text += remove_spaces(current_page.extract_text()) + '\n'

# write to file
with open(OUTPUT_TXT_PATH, 'w') as f:
    f.write(text)
print('done.')
    