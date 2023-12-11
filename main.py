from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()

    # set header
    pdf.set_font(family="arial", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, align="L", ln=1)
    pdf.line(10, 22, 200, 22)

    # set footer
    pdf.ln(260)
    pdf.set_font(family="arial", style="I", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", border=0, ln=1)

    for i in range(row["Pages"]-1):
        pdf.add_page()

        # set footer
        pdf.ln(272)
        pdf.set_font(family="arial", style="I", size=12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", border=0, ln=1)







pdf.output("output.pdf")
