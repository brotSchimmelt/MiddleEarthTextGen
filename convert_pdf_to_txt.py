import argparse

import pdfplumber
from tqdm import trange

from util.helper import remove_spaces, remove_spaces_concisely


def convert_page(page_number: int, pdf: pdfplumber.PDF) -> str:
    """Convert a single page of a pdf to string.

    Args:
        page_number (int): page number to convert
        pdf (pdfplumber.PDF): PDF object

    Returns:
        str: text of page
    """
    current_page = pdf.pages[page_number]

    # default case: convert complete page
    if not args.skip_first_line and not args.skip_last_line:
        return trim_spaces(current_page.extract_text()) + "\n"

    text = current_page.extract_text()

    # skip first line on each page
    if args.skip_first_line:
        text = trim_spaces("\n".join(text.split("\n")[1:])) + "\n"

    # skip last line on each page
    if args.skip_last_line:
        text = trim_spaces("\n".join(text.split("\n")[:-2])) + "\n"

    return text


#### ARGUMENTS ####
parser = argparse.ArgumentParser(description="Convert PDF to txt file")
parser.add_argument("input_pdf_path", type=str, help="path to input pdf file")
parser.add_argument("output_txt_name", type=str, help="name of output txt file")
parser.add_argument(
    "--skip_first_line", action="store_true", help="skip first line on each page"
)
parser.add_argument(
    "--skip_last_line", action="store_true", help="skip last line on each page"
)
parser.add_argument("--concise", action="store_true", help="write every page to 1 line")
parser.add_argument("--page", type=int, help="single page to convert")
parser.add_argument("--start_page", type=int, help="start page to convert")
parser.add_argument("--end_page", type=int, help="end page to convert")
args = parser.parse_args()
trim_spaces = remove_spaces_concisely if args.concise else remove_spaces

# check if page range is valid
if args.page and (args.start_page or args.end_page):
    raise ValueError(
        "You can either convert a single page or a range of pages, not both."
    )

if args.start_page and args.end_page and (args.start_page >= args.end_page):
    raise ValueError("Start page must be smaller than end page.")

# open pdf
with pdfplumber.open(args.input_pdf_path) as pdf:
    # convert single page
    if args.page:
        page = args.page - 1  # pdfplumber starts counting at 0
        print(f"converting page: {args.page}")
        text = convert_page(page, pdf)

    # convert page range
    elif args.start_page or args.end_page:
        start_page = args.start_page - 1 if args.start_page else 0
        end_page = args.end_page or len(pdf.pages)
        print(f"converting pages: {start_page + 1} - {end_page}")
        text = "".join(convert_page(page, pdf) for page in trange(start_page, end_page))

    else:
        # convert all pages
        total_num_pages = len(pdf.pages)
        print(f"total number of pages to convert: {total_num_pages}")
        text = "".join(convert_page(page, pdf) for page in trange(total_num_pages))


# write to txt file
with open(args.output_txt_name, "w") as f:
    f.write(text)
print(f"\nWritten to {args.output_txt_name}")
