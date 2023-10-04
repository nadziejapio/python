from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 48)
        self.cell(180, 50, "CS50 Shirtificate", align="C")
        self.ln(60)


pdf = PDF()
pdf.add_page()
pdf.set_margin(0)
pdf.set_auto_page_break(0)
pdf.set_font(size=24)
pdf.image("shirtificate.png", keep_aspect_ratio=True, )
pdf.set_text_color(255,255,255)
pdf.cell(0, -260, input("Name: ") + " took CS50", align="C")
pdf.output("shirtificate.pdf")