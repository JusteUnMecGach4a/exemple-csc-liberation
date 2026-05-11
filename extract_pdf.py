import fitz  # PyMuPDF
import json
import os

def extract_text_from_pdf(pdf_path, output_txt, output_json):
    """
    Extrait le texte d'un fichier PDF et le sauvegarde en formats TXT et JSON.
    """
    if not os.path.exists(pdf_path):
        print(f"Erreur : Le fichier '{pdf_path}' n'existe pas.")
        return

    print(f"Traitement de : {pdf_path}...")
    
    doc = fitz.open(pdf_path)
    extracted_data = {
        "metadata": doc.metadata,
        "pages": []
    }
    
    all_text = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        extracted_data["pages"].append({
            "page_number": page_num + 1,
            "content": text
        })
        
        all_text.append(f"--- Page {page_num + 1} ---\n{text}")

    # Sauvegarde en TXT
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("\n\n".join(all_text))
    
    # Sauvegarde en JSON
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)

    print(f"Extraction terminée !")
    print(f"Fichier texte : {output_txt}")
    print(f"Fichier JSON : {output_json}")

if __name__ == "__main__":
    PDF_FILE = "Projet social Libération 2026-2029.pdf"
    OUTPUT_TXT = "projet_social_extracted.txt"
    OUTPUT_JSON = "projet_social_extracted.json"
    
    extract_text_from_pdf(PDF_FILE, OUTPUT_TXT, OUTPUT_JSON)
