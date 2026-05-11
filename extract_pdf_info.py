import PyPDF2
import os

def extract_text_from_pdf(pdf_path, output_txt):
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Analyzing PDF: {pdf_path}")
            print(f"Number of pages: {num_pages}")

            full_text = ""
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                full_text += f"--- Page {page_num + 1} ---\n"
                full_text += page.extract_text() + "\n\n"

            with open(output_txt, 'w', encoding='utf-8') as out_file:
                out_file.write(full_text)
            
            print(f"Extraction successful! Content saved to {output_txt}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_file = r"D:\Projets\CSC_Liberation\Projet social Libération 2026-2029.pdf"
    output_file = "extracted_project_social.txt"
    extract_text_from_pdf(pdf_file, output_file)
