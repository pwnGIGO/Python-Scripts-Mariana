import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import grey
import os

def create_watermark(text):
    """
    Creates a PDF with the given text as a watermark.
    """
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.saveState()

    # Move the origin to the center of the page
    can.translate(letter[0] / 2, letter[1] / 2)
    
    # Rotate the canvas
    can.rotate(45)
    
    can.setFont('Helvetica', 26)
    can.setFillColor(grey, alpha=0.6)
    
    lines = text.split('\n')
    num_lines = len(lines)
    line_height = 25
    
    # Calculate the total height of the text block
    total_text_height = (num_lines - 1) * line_height
    
    # Calculate the starting Y position to center the text block vertically
    y_start = total_text_height / 2
    
    for line in lines:
        # Draw the string centered horizontally at x=0 (the new origin)
        can.drawCentredString(0, y_start, line)
        y_start -= line_height

    can.restoreState()
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    return PdfReader(packet)


def add_watermark(input_pdf_path, watermark_text, output_pdf_path):
    """
    Adds a watermark to a PDF file.
    """
    if not os.path.exists(input_pdf_path):
        print(f"Error: The file '{input_pdf_path}' was not found.")
        return

    watermark_pdf = create_watermark(watermark_text)
    watermark_page = watermark_pdf.pages[0]

    input_pdf = PdfReader(input_pdf_path)
    output_pdf = PdfWriter()

    for i in range(len(input_pdf.pages)):
        page = input_pdf.pages[i]
        page.merge_page(watermark_page)
        output_pdf.add_page(page)

    try:
        with open(output_pdf_path, "wb") as output_file:
            output_pdf.write(output_file)
        print(f"Watermark added. Output saved to {output_pdf_path}")
    except PermissionError:
        print(f"\nError: Permission denied.")
        print(f"Please make sure the file '{output_pdf_path}' is not open in another program and try again.")


if __name__ == "__main__":
    INPUT_FILE = "Registro PC Jorge Ávila 2025.pdf"
    OUTPUT_FILE = "Registro PC Jorge Ávila 2025_watermarked.pdf"
    WATERMARK_TEXT = "Para uso exclusivo de AVILA CONSULTORES\ncapacitación de brigada multifuncional\ndel 10 al 12 de noviembre de 2025"
    
    print(f"Adding watermark to {INPUT_FILE}...")
    add_watermark(INPUT_FILE, WATERMARK_TEXT, OUTPUT_FILE)