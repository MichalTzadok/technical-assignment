import markdown
import pdfkit
import os

WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

def convert_md_to_pdf(input_md_file, output_pdf_file):
    # Read the content of the Markdown file
    with open(input_md_file, "r", encoding="utf-8") as f:
        md_text = f.read()
    
    # Convert Markdown to HTML
    html = markdown.markdown(md_text)
    
    # Convert HTML to PDF using pdfkit
    pdfkit.from_string(html, output_pdf_file, configuration=config)
    print(f"PDF successfully created: {output_pdf_file}")

if __name__ == "__main__":
    input_file = "input.md"    # Markdown input file
    output_file = "output.pdf" # Output PDF file
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
    else:
        convert_md_to_pdf(input_file, output_file)
