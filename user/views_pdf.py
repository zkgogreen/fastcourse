from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pdfrw import PdfReader, PdfWriter
from io import BytesIO

def generate_english_certificate(request):
    # Generate the PDF with the provided name
    response = FileResponse(merge_pdf_template("zakaria"))
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    return response

def merge_pdf_template(name):
    # Create a new PDF with the name
    output_pdf = PdfWriter()
    name_pdf = PdfReader("media/kelas/tensorflow.pdf")
    page = name_pdf.pages[0]

    # Create a new PDF document using ReportLab
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 100, name)
    c.save()

    # Merge the two PDFs
    new_pdf = PdfReader(buffer)
    page.mergePage(new_pdf.pages[0])
    output_pdf.add_page(page)

    # Save the merged PDF to a file
    output_pdf.write("output.pdf")

    return "output.pdf"
