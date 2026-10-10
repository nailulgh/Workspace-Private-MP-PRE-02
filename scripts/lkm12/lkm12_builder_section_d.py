# -*- coding: utf-8 -*-
"""
Section D Builder: Daftar Pustaka Khusus Pertemuan 12
Pertemuan 12: Manajemen Risiko Proyek (Bagian II)
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_d(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_body_p = helpers['add_body_p']

    add_heading_1(doc, "D. DAFTAR PUSTAKA KHUSUS PERTEMUAN 12")

    add_body_p(doc,
        "Daftar pustaka ini memuat seluruh literatur acuan akademis, standar manajemen proyek internasional PMI, "
        "buku analisis keputusan kuantitatif, serta teori manajemen risiko rekayasa perangkat lunak yang digunakan dalam "
        "penyusunan Lembar Kerja Mahasiswa (LKM) Pertemuan 12 mengikuti format baku APA 7th Edition (American Psychological Association):")

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
        "Clemen, R. T., & Reilly, T. (2013). Making Hard Decisions with DecisionTools (3rd ed.). Mason, OH: South-Western Cengage Learning.")

    add_hanging_indent_p(doc,
        "Heldman, K. (2018). PMP: Project Management Professional Exam Study Guide (9th ed.). Indianapolis, IN: John Wiley & Sons, Inc.")

    add_hanging_indent_p(doc,
        "Hillson, D. (2009). Managing Risk in Projects. Farnham, UK: Gower Publishing.")

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

    add_hanging_indent_p(doc,
        "Vose, D. (2008). Risk Analysis: A Quantitative Guide (3rd ed.). Chichester, UK: John Wiley & Sons.")
