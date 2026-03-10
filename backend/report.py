
from reportlab.pdfgen import canvas

def generate_report(path):

c=canvas.Canvas(path)
c.drawString(100,750,"AI Investigation Report")
c.save()
