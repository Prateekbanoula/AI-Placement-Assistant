import pdfplumber
def extract_text_from_pdf(pdf_path: str) -> str:
    full_text_list = []
    with pdfplumber.open(pdf_path) as pdf: 
        print(f"total pages: {len(pdf.pages)}")

        for page in pdf.pages:
           text = page.extract_text(layout=True)
           if text and text.strip():
               full_text_list.append(text)

    complete_text = "\n".join(full_text_list).strip()

    if not complete_text:
        raise ValueError(f"No text could be extracted from {pdf_path} — possibly a scanned/image-based PDF.")
    
    print(f"Extracted {len(complete_text)} characters from {pdf_path}")

    return complete_text  

if __name__ == "__main__":
    result = extract_text_from_pdf("C:/Users/prate/Downloads/prateek banoula.pdf")
    print(result)
    
    # layout=True preserves column structure — without it, multi-column
    # resumes get scrambled since extract_text() reads left-to-right
    # across the full page width by default
    #text = page.extract_text(layout=True)
    #text = page.extract_text_simple(x_tolerance=3, y_tolerance=3)
   

