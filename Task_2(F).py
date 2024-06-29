#with reference to a yt video (https://pythonology.eu/what-is-the-best-python-pdf-library/) + chatgpt
import fitz
import os
from IPython.display import Image as IPImage, display

# Create a document object
pdf_path = r'd:\\OCR\\2023_SE_ASSIGNMENT_3.pdf'
doc = fitz.open(pdf_path) # or fitz.Document(filename)

# Extract the number of pages (int)
print(f"Number of pages: {doc.page_count}")

# the metadata (dict) e.g., the author,...
print("Metadata:", doc.metadata)

# Create an output directory
output_dir = "output_images"
os.makedirs(output_dir, exist_ok=True)

# Function to display and save an image
def display_and_save_image(pix, page_number, output_dir):
    image_path = os.path.join(output_dir, f"page-{page_number}.png")
    pix.save(image_path)
    display(IPImage(filename=image_path))
    print(f"Saved image: {image_path}")

# File to save extracted text
text_file_path = os.path.join(output_dir, "extracted_text.txt")

# Extract text and save images
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    for i in range(doc.page_count):
        page = doc.load_page(i)
        
        # Extract and save text
        text = page.get_text()
        text_file.write(f"Page {i + 1}:\n{text}\n\n")
        
        # Render and save image
        pix = page.get_pixmap()
        display_and_save_image(pix, page.number, output_dir)

# Get the links on all pages
for i in range(doc.page_count):
    page = doc.load_page(i)
    links = page.get_links()
    print(f"Links on page {i}:", links)

print(f"Text extracted and saved to '{text_file_path}'")
