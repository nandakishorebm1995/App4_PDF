from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 150)
    pdf.cell(w=0, h=20, txt=f'{row["Order"]}. {row["Topic"]}', align="L", ln=1)
    pdf.line(5, 30, 200, 30)

    # Set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(100, 100, 150)
    pdf.cell(w=0, h=20, txt=f'{row["Order"]}. {row["Topic"]}', align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(100, 100, 150)
        pdf.cell(w=0, h=20, txt=f'{row["Order"]}. {row["Topic"]}', align="R")

pdf.output("Output.pdf")

