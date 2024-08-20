# pdf_functions.py

from pypdf import PdfReader, PdfWriter, PdfMerger

def create_pdf(output_filename, content):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    import datetime

    c = canvas.Canvas(output_filename, pagesize=letter)
    c.drawString(100, 750, f"Content: {content}")
    c.drawString(100, 730, f"Date: {datetime.date.today()}")
    c.save()
    print(f"PDF '{output_filename}' created successfully.")

def merge_pdfs(output_filename, pdf_files):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as '{output_filename}'.")

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    watermark = PdfReader(watermark_pdf)
    writer = PdfWriter()

    watermark_page = watermark.pages[0]

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"Watermarked PDF saved as '{output_pdf}'.")

