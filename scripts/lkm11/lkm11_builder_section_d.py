# -*- coding: utf-8 -*-
"""
Section D Builder: Daftar Pustaka Khusus Pertemuan 11
Pertemuan 11: Manajemen Risiko Proyek (Bagian I)
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_d(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_body_p = helpers['add_body_p']

    add_heading_1(doc, "D. DAFTAR PUSTAKA KHUSUS PERTEMUAN 11")

    add_body_p(doc,
        "Daftar pustaka ini memuat seluruh literatur acuan akademis, standar manajemen proyek internasional PMI, "
        "buku teks rekayasa perangkat lunak, serta teori psikologi keputusan risiko yang digunakan dalam penyusunan "
        "Lembar Kerja Mahasiswa (LKM) Pertemuan 11 mengikuti format baku APA 7th Edition (American Psychological Association):")

    def add_hanging_indent_p(document, text):
        p = document.add_paragraph()
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Inches(-0.5)
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        return p

    add_hanging_indent_p(doc,
        "Boehm, B. W. (1981). Software Engineering Economics. Englewood Cliffs, NJ: Prentice-Hall.")

    add_hanging_indent_p(doc,
        "Boehm, B. W. (1991). Software risk management: Principles and practices. IEEE Software, 8(1), 32–41. https://doi.org/10.1109/52.62930")

    add_hanging_indent_p(doc,
        "Cooper, D. F., & Chapman, C. B. (1987). Risk Analysis for Large Projects: Models, Methods and Cases. Chichester, UK: John Wiley & Sons.")

    add_hanging_indent_p(doc,
        "Heldman, K. (2018). PMP: Project Management Professional Exam Study Guide (9th ed.). Indianapolis, IN: John Wiley & Sons, Inc.")

    add_hanging_indent_p(doc,
        "Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263–291. https://doi.org/10.2307/1914185")

    add_hanging_indent_p(doc,
        "Kerzner, H. (2017). Project Management: A Systems Approach to Planning, Scheduling, and Controlling (12th ed.). Hoboken, NJ: John Wiley & Sons.")

    add_hanging_indent_p(doc,
        "Larson, E. W., & Gray, C. F. (2021). Project Management: The Managerial Process (8th ed.). New York, NY: McGraw-Hill Education.")

    add_hanging_indent_p(doc,
        "Project Management Institute. (2017). A Guide to the Project Management Body of Knowledge (PMBOK® Guide) (6th ed.). Newtown Square, PA: Project Management Institute, Inc.")

    add_hanging_indent_p(doc,
        "Project Management Institute. (2019). The Standard for Risk Management in Portfolios, Programs, and Projects. Newtown Square, PA: Project Management Institute, Inc.")

    add_hanging_indent_p(doc,
        "Schwalbe, K. (2019). Information Technology Project Management (9th ed.). Boston, MA: Cengage Learning.")
