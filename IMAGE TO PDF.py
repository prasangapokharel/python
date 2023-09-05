from PIL import Image
from reportlab.pdfgen import canvas

def image_to_pdf(image_path, pdf_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Get image dimensions
        width, height = img.size

    # Create a new PDF file
    c = canvas.Canvas(pdf_path, pagesize=(width, height))

    # Draw the image on the PDF -- the coordinates (0,0) specify the bottom-left corner
    c.drawImage(image_path, 0, 0, width=width, height=height)

    # Save the PDF file
    c.save()

# Use the function
image_path = r"C:\Users\godsu\Desktop\Python\man.jpeg"  # Replace with the path to your image file
pdf_path = r"output.pdf"  # Replace with the desired PDF output path
image_to_pdf(image_path, pdf_path)

print("Image has been converted to PDF.")
