from docx2pdf import convert

# Specify the input DOCX file path must be in same folder(replace with your file path)
input_docx = "mamu.docx"

# Specify the output PDF file path (replace with your desired output path)
output_pdf = "output.pdf"

try:
    convert(input_docx, output_pdf)
    print(f"Conversion successful. {input_docx} has been converted to {output_pdf}")
except Exception as e:
    print(f"Conversion failed: {str(e)}")
