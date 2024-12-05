from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


def make_receipt(data, out_file_name="receipt.pdf"):
  """Generates a PDF receipt from a list of data.

  Args:
      data: A list of lists, where each inner list represents a row in the receipt.
          Each inner list should contain three elements:
              - The name of the item
              - The cost of the item
              - The tax for the item
      out_file_name: The name of the output PDF file.

  Returns:
      None
  """

  # Create a SimpleDocTemplate object
  pdf = SimpleDocTemplate(out_file_name, pagesize=A4)

  # Get a sample style sheet
  styles = getSampleStyleSheet()

  # Create a title paragraph
  title = Paragraph("Dessert Shop Receipt", styles["Heading1"])
  title.alignment = 1

  # Create a table style
  style = TableStyle([
      ("BOX", (0, 0), (-1, -1), 1, colors.black),
      ("GRID", (0, 0), (-1, -1), 1, colors.black),
      ("BACKGROUND", (0, 0), (3, 0), colors.gray),
      ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
      ("ALIGN", (0, 0), (-1, -1), "CENTER"),
      ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
  ])

  # Create a table object
  table = Table(data, style=style)

  # Build the PDF
  pdf.build([title, table])


# Example usage
DATA = [
    ["Name", "Cost", "Tax"],
    ["Candy Corn", "$0.38", "$0.03"],
    ["Gummy Bears", "$0.09", "$0.01"],
    # ... Add more items here ...
    ["Subtotal", "", ""],  # Replace with calculated subtotal
    ["Order Tax", "", ""],  # Replace with calculated total tax
    ["Total", "", ""],  # Replace with calculated total cost
    ["Total Items", "", ""],  # Replace with total number of items
]

make_receipt(DATA)
