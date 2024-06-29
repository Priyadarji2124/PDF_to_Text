#chatgpt(my style description)(MORE EFFICIENT FOR EMBEDDED TEXTV  MEANS ONLY TEXT PDFS)
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import fitz  # PyMuPDF
import os

def pdf_to_text(pdf_file):
    # Open the PDF file and extract text
    pdf_document = fitz.open(pdf_file)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    pdf_document.close()
    return text

def save_text_to_file(text, output_file):
    # Save text to a file in the same folder as the script
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text extracted and saved to '{output_file}'")
    except UnicodeEncodeError as e:
        print(f"UnicodeEncodeError: {e}")
        # Handle the error by ignoring problematic characters
        text = text.encode('ascii', 'ignore').decode('ascii')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text saved to '{output_file}' after handling UnicodeEncodeError.")
    except Exception as e:
        print(f"Error saving text to file: {e}")

if __name__ == "__main__":
    # Replace 'path_to_your_pdf_file.pdf' with the path to your PDF file
    pdf_file_path = r'd:\\OCR\\2023_SE_ASSIGNMENT_3.pdf'
    
    
    # Extract text from PDF
    extracted_text = pdf_to_text(pdf_file_path)
    
    # Save extracted text to a text file
    script_dir = os.path.dirname(__file__) if '__file__' in locals() else os.getcwd()
    output_file_path = os.path.join(script_dir, 'output_text.txt')
    save_text_to_file(extracted_text, output_file_path)
