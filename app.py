### 📂 Datei: app.py

import streamlit as st
from fpdf import FPDF
from docx import Document
from datetime import datetime
import os

st.set_page_config(page_title="Betriebsanweisung Generator", layout="centered")

st.title("📄 Betriebsanweisung Generator nach DGUV 211-010")

firmenname = st.text_input("Firmenname")
nr = st.text_input("Nummer")
arbeitsbereich = st.text_input("Arbeitsbereich")
arbeitsplatz = st.text_input("Arbeitsplatz")
taetigkeit = st.text_input("Tätigkeit")

gefahren = st.text_area("Gefahren für Mensch und Umwelt")
schutz = st.text_area("Schutzmaßnahmen und Verhaltensregeln")
verhalten_gefahrfall = st.text_area("Verhalten im Gefahrfall")
erste_hilfe = st.text_area("Erste Hilfe")
entsorgung = st.text_area("Sachgerechte Entsorgung")

pictogramme = st.file_uploader("Piktogramme hochladen", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

datum = datetime.today().strftime('%d.%m.%Y')

# PDF-Erstellung
def create_pdf(path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, f"{firmenname} - BETRIEBSANWEISUNG Nr. {nr}", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Arbeitsbereich: {arbeitsbereich}\nArbeitsplatz: {arbeitsplatz}\nTätigkeit: {taetigkeit}")

    sections = {
        "Gefahren für Mensch und Umwelt": gefahren,
        "Schutzmaßnahmen und Verhaltensregeln": schutz,
        "Verhalten im Gefahrfall": verhalten_gefahrfall,
        "Erste Hilfe": erste_hilfe,
        "Sachgerechte Entsorgung": entsorgung
    }

    for title, content in sections.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, title, ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, content)

    if pictogramme:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Piktogramme:", ln=True)
        for pict in pictogramme:
            tmp_path = os.path.join("/tmp", pict.name)
            with open(tmp_path, "wb") as f:
                f.write(pict.getbuffer())
            pdf.image(tmp_path, w=20)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Datum: {datum}   Unterschrift: ___________________", ln=True, align='L')

    pdf.output(path)

# DOCX-Erstellung
def create_docx(path):
    doc = Document()
    doc.add_heading(f"{firmenname} - BETRIEBSANWEISUNG Nr. {nr}", 0)
    doc.add_paragraph(f"Arbeitsbereich: {arbeitsbereich}\nArbeitsplatz: {arbeitsplatz}\nTätigkeit: {taetigkeit}")

    sections = {
        "Gefahren für Mensch und Umwelt": gefahren,
        "Schutzmaßnahmen und Verhaltensregeln": schutz,
        "Verhalten im Gefahrfall": verhalten_gefahrfall,
        "Erste Hilfe": erste_hilfe,
        "Sachgerechte Entsorgung": entsorgung
    }

    for title, content in sections.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(content)

    doc.add_paragraph(f"Datum: {datum}   Unterschrift: ___________________")
    doc.save(path)

# Buttons für Export
if st.button("📥 PDF erstellen"):
    pdf_path = "/tmp/betriebsanweisung.pdf"
    create_pdf(pdf_path)
    with open(pdf_path, "rb") as f:
        st.download_button("PDF herunterladen", f, file_name="betriebsanweisung.pdf")

if st.button("📥 DOCX erstellen"):
    docx_path = "/tmp/betriebsanweisung.docx"
    create_docx(docx_path)
    with open(docx_path, "rb") as f:
        st.download_button("Word-Datei herunterladen", f, file_name="betriebsanweisung.docx")


### 📂 Datei: requirements.txt

streamlit
fpdf
python-docx


### 📂 Datei: README.md

# Betriebsanweisung Generator

Generator für Betriebsanweisungen nach DGUV 211-010.

## Installation
```bash
pip install -r requirements.txt
```

## Start
```bash
streamlit run app.py
```

Danach im Browser öffnen:  
👉 http://localhost:8501
