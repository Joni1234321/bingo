from fpdf import FPDF
from datetime import date

OUTPUT_PATH = "user/bingoplader/"


class PDF(FPDF):
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


class PlatePDF(PDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', '', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, self.name, "B", 0, 'C')
        # Line break
        self.ln(20)

    def draw_plates(self, plates):
        # Draw settings
        self.add_page()
        # Draw each plate
        for plate in plates:
            self.draw_plate(plate)
            self.ln(20)

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.set_title("Plates - " + name)


class CombinedPlatePDF(PDF):
    def draw_plates(self, plates):
        # Draw each plate
        i = 0
        for plate in plates:
            if i % 3 == 0:
                # Add page, and header
                self.add_page()
                self.set_font('Arial', '', 15)
                self.cell(80)
                self.cell(30, 10, plates[0].name, "B", 0, 'C')
                self.ln(20)

            # Draw each plate
            self.draw_plate(plate)
            self.ln(20)
            i += 1

    def __init__(self, name):
        super().__init__()
        self.set_title("Combined Plates")


def player_to_pdf(name, plates):
    pdf = PlatePDF(name)
    pdf.draw_plates(plates)
    pdf.output(OUTPUT_PATH + name + ".pdf")


def all_plates_to_pdf(list_of_plates):
    pdf = CombinedPlatePDF("All")

    for plates in list_of_plates:
        pdf.draw_plates(plates)
    pdf.output(OUTPUT_PATH + "all.pdf")
