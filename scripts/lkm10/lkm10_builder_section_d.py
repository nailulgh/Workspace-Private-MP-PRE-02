# -*- coding: utf-8 -*-
"""
Section D Builder: Daftar Pustaka Khusus Pertemuan 10
Pertemuan 10: Manajemen Komunikasi Proyek
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_d(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_body_p = helpers['add_body_p']

    add_heading_1(doc, "D. DAFTAR PUSTAKA KHUSUS PERTEMUAN 10")

    add_body_p(doc,
        "Daftar pustaka ini memuat seluruh literatur acuan akademis, standar manajemen proyek internasional PMI, "
        "teori komunikasi klasik, serta rujukan rekayasa perangkat lunak yang digunakan dalam penyusunan Lembar Kerja Mahasiswa (LKM) "
        "Pertemuan 10 mengikuti format baku APA 7th Edition (American Psychological Association):")

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
        "Brooks, F. P. (1995). The Mythical Man-Month: Essays on Software Engineering (Anniversary ed.). Boston, MA: Addison-Wesley Professional.")

    add_hanging_indent_p(doc,
        "Edmondson, A. C. (2018). The Fearless Organization: Creating Psychological Safety in the Workplace for Learning, Innovation, and Growth. Hoboken, NJ: John Wiley & Sons.")

    add_hanging_indent_p(doc,
        "Kerzner, H. (2017). Project Management: A Systems Approach to Planning, Scheduling, and Controlling (12th ed.). Hoboken, NJ: John Wiley & Sons.")

    add_hanging_indent_p(doc,
        "Larson, E. W., & Gray, C. F. (2021). Project Management: The Managerial Process (8th ed.). New York, NY: McGraw-Hill Education.")

    add_hanging_indent_p(doc,
        "Project Management Institute. (2017). A Guide to the Project Management Body of Knowledge (PMBOK® Guide) (6th ed.). Newtown Square, PA: Project Management Institute, Inc.")

    add_hanging_indent_p(doc,
        "Project Management Institute. (2018). Pulse of the Profession: The Essential Role of Communications. Newtown Square, PA: Project Management Institute, Inc.")

    add_hanging_indent_p(doc,
        "Schwalbe, K. (2019). Information Technology Project Management (9th ed.). Boston, MA: Cengage Learning.")

    add_hanging_indent_p(doc,
        "Shannon, C. E., & Weaver, W. (1949). The Mathematical Theory of Communication. Urbana, IL: University of Illinois Press.")

    add_hanging_indent_p(doc,
        "West, M. A. (2012). Effective Teamwork: Practical Lessons from Organizational Research (3rd ed.). Chichester, UK: Wiley-Blackwell.")
