#chatgpt(whatsapp description)(MORE EFFICIENT FOR NON EMBEDDED TEXTV  MEANS TEXT AS WELL AS IMG OR ANY OTHER DATA PDFS)
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import fitz  # PyMuPDF
from PIL import Image
import io

# Configure tesseract executable path if not on system path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_to_text(pdf_path, output_txt_path, tesseract_lang='eng', tesseract_oem=3):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ''
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        
        # Convert the pixmap to a PIL image
        img = Image.open(io.BytesIO(pix.tobytes()))
        
        # Configure Tesseract parameters
        custom_config = f'--oem {tesseract_oem} -l {tesseract_lang}'
        text += pytesseract.image_to_string(img, config=custom_config)
        text += '\n\n'  # Add newlines to separate pages
    
    # Write text to output file
    with open(output_txt_path, 'w') as f:
        f.write(text)
    
# Print success message
    print(f'{output_txt_path} has been successfully created.')

if __name__ == "__main__":
    # Example usage
    pdf_path =  r'd:\\OCR\\2023_SE_ASSIGNMENT_3.pdf'
    output_txt_path = 'output.txt'
    pdf_to_text(pdf_path, output_txt_path, tesseract_lang='eng', tesseract_oem=3)
    
