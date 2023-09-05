from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Create a PDF file
pdf = SimpleDocTemplate(
    "generated_text.pdf",
    pagesize=letter
)

# Sample text
text = input("Enter a text: ") 



# Styles
styles = getSampleStyleSheet()

# Create a paragraph with text and a style
paragraph = Paragraph(text, styles["BodyText"])

# Build the PDF
pdf.build([paragraph])

print("PDF generated successfully!")
