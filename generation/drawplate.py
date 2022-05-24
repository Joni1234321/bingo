from fpdf import FPDF
from datetime import datetime, date

OUTPUT_PATH = "bingoplader/"

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', '', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, self.name, "B", 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
        self.cell(0, 10, str(date.today()), 0, 0, 'C')

    def draw_plate(self, plate):
        draw_array = plate.create_draw_array()

        self.set_font('Arial', 'B', 25)
        for r in draw_array:
            for c in r:
                content = ""
                if c != 0:
                    content = str(c)
                self.cell(20, 20, content, 1, 0, "C")
            self.ln()

    def __init__(self, plates):
        super().__init__()
        self.name = plates[0].name
        self.set_title("Plates - " + self.name)

        # Draw settings
        self.add_page()
        for plate in plates:
            self.draw_plate(plate)
            self.ln(20)


def player_to_pdf(plates):
    pdf = PDF(plates)
    pdf.output(OUTPUT_PATH + plates[0].name + ".pdf")
