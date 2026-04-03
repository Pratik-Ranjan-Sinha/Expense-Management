import csv
# from pypdf import PdfWriter
# from pypdf.xmp import XmpInformation
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import string


class report:
    def __init__(self):
        month = int(input("Enter month number (1-12): "))

        print("=" * 50)
        print("\tMonthly Report")
        print("=" * 50)

        file =open("data/expense.csv", "r")
        reader = csv.reader(file)

        next(reader) 
        
        chars = string.ascii_letters + string.digits
        randomText = ''.join(random.choices(chars, k=12))
        pdf = canvas.Canvas(f"reports/{randomText}.pdf", pagesize=letter)
        pdf.drawString(250, 750, "Report of the Month")
        Y = 710

        found = False
        for row in reader:
            date = row[2]
            m = int(date[5:7])

            if m == month:
                found = True

                pdf.drawString(100, Y, f"Amount: {row[0]}")
                Y -= 20
                pdf.drawString(100, Y, f"Category: {row[1]}")
                Y -= 20
                pdf.drawString(100, Y, f"Date: {row[2]}")
                Y -= 20
                pdf.drawString(100, Y, f"Description: {row[3]}")
                Y -= 40
                # Set metadata fields
                # xmp = XmpInformation.create()
                # xmp.dc_title = {"x-default": "Report"}
                # xmp.dc_description = {"\nAmount:", row[0]}
                # xmp.dc_description = {"Category:", row[1]}
                # xmp.dc_description = {"Date:", row[2]}
                # xmp.dc_description = {"Description:", row[3]}
                # xmp.pdf_producer = "pypdf"
                
                # # Create a writer and add the metadata
                # writer = PdfWriter()
                # writer.add_blank_page(612, 792)  # Add a page
                # writer.xmp_metadata = xmp
                # writer.write("report_xmp.pdf")
                
                print("\nAmount:", row[0])
                print("Category:", row[1])
                print("Date:", row[2])
                print("Description:", row[3])
                print("-" * 24)
        pdf.save()
        file.close()

        if not found:
            print("No expenses found for this month.")

