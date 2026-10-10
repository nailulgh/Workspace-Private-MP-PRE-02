# -*- coding: utf-8 -*-
"""
Section E Builder: Daftar Pustaka Khusus Pertemuan 8
Pertemuan 8: Manajemen Kualitas Proyek
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_e(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_body_p = helpers['add_body_p']

    add_heading_1(doc, "E. DAFTAR PUSTAKA KHUSUS PERTEMUAN 8")

    add_body_p(doc,
        "Daftar pustaka ini memuat seluruh literatur acuan akademis, standar manajemen proyek internasional, "
        "serta buku teks fundamental manajemen mutu yang digunakan dalam penyusunan Lembar Kerja Mahasiswa (LKM) Pertemuan 8 "
        "mengikuti standar baku APA 7th Edition (American Psychological Association):")

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
        "Crosby, P. B. (1979). Quality Is Free: The Art of Making Quality Certain. New York, NY: McGraw-Hill Book Company.")

    add_hanging_indent_p(doc,
        "Deming, W. E. (1986). Out of the Crisis. Cambridge, MA: Massachusetts Institute of Technology, Center for Advanced Educational Services.")

    add_hanging_indent_p(doc,
        "Ishikawa, K. (1985). What Is Total Quality Control? The Japanese Way. Englewood Cliffs, NJ: Prentice-Hall.")

    add_hanging_indent_p(doc,
        "Juran, J. M., & Godfrey, A. B. (1999). Juran's Quality Handbook (5th ed.). New York, NY: McGraw-Hill.")

    add_hanging_indent_p(doc,
        "Kerzner, H. (2017). Project Management: A Systems Approach to Planning, Scheduling, and Controlling (12th ed.). Hoboken, NJ: John Wiley & Sons.")

    add_hanging_indent_p(doc,
        "Larson, E. W., & Gray, C. F. (2021). Project Management: The Managerial Process (8th ed.). New York, NY: McGraw-Hill Education.")

    add_hanging_indent_p(doc,
        "Nicholas, J. M., & Steyn, H. (2017). Project Management for Engineering, Business and Technology (5th ed.). London & New York: Routledge.")

    add_hanging_indent_p(doc,
        "Project Management Institute. (2017). A Guide to the Project Management Body of Knowledge (PMBOK® Guide) (6th ed.). Newtown Square, PA: Project Management Institute, Inc.")

    add_hanging_indent_p(doc,
        "Schwalbe, K. (2019). Information Technology Project Management (9th ed.). Boston, MA: Cengage Learning.")
