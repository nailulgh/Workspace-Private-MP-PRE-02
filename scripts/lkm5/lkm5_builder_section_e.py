# -*- coding: utf-8 -*-
"""
Section E Builder: Daftar Pustaka Khusus Pertemuan 5
Pertemuan 5: Manajemen Jadwal Proyek (Bagian I)
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_e(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_body_p = helpers['add_body_p']

    add_heading_1(doc, "D. DAFTAR PUSTAKA KHUSUS PERTEMUAN 5")
    
    add_body_p(doc,
        "Daftar pustaka ini memuat seluruh literatur rujukan akademis, standar manajemen proyek internasional PMI, "
        "serta buku teks acuan utama yang digunakan dalam penyusunan Lembar Kerja Mahasiswa (LKM) Pertemuan 5 ini "
        "mengikuti format baku APA 7th Edition (American Psychological Association):")

    references = [
        ("Badiru, A. B. (2019). ", "Project Management: Systems, Principles, and Applications", " (2nd ed.). Boca Raton, FL: CRC Press."),
        ("Kerzner, H. (2017). ", "Project Management: A Systems Approach to Planning, Scheduling, and Controlling", " (12th ed.). Hoboken, NJ: John Wiley & Sons."),
        ("Larson, E. W., & Gray, C. F. (2021). ", "Project Management: The Managerial Process", " (8th ed.). New York, NY: McGraw-Hill Education."),
        ("Moder, J. J., Phillips, C. R., & Davis, E. W. (1983). ", "Project Management with CPM, PERT and Precedence Diagramming", " (3rd ed.). New York, NY: Van Nostrand Reinhold."),
        ("Project Management Institute. (2017). ", "A Guide to the Project Management Body of Knowledge (PMBOK® Guide)", " (6th ed.). Newtown Square, PA: Project Management Institute, Inc."),
        ("Project Management Institute. (2019). ", "Practice Standard for Scheduling", " (3rd ed.). Newtown Square, PA: Project Management Institute, Inc."),
        ("Schwalbe, K. (2019). ", "Information Technology Project Management", " (9th ed.). Boston, MA: Cengage Learning.")
    ]

    for prefix, italic_title, suffix in references:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.first_line_indent = Inches(-0.5)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5

        r_pre = p.add_run(prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(12)
        r_pre.font.color.rgb = RGBColor(0, 0, 0)

        r_title = p.add_run(italic_title)
        r_title.font.name = "Times New Roman"
        r_title.font.size = Pt(12)
        r_title.font.italic = True
        r_title.font.color.rgb = RGBColor(0, 0, 0)

        r_suf = p.add_run(suffix)
        r_suf.font.name = "Times New Roman"
        r_suf.font.size = Pt(12)
        r_suf.font.color.rgb = RGBColor(0, 0, 0)
