# -*- coding: utf-8 -*-
"""
Section D Builder: Daftar Pustaka Khusus Pertemuan 9
Pertemuan 9: Manajemen Sumber Daya Proyek
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_d(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_body_p = helpers['add_body_p']

    add_heading_1(doc, "D. DAFTAR PUSTAKA KHUSUS PERTEMUAN 9")

    add_body_p(doc,
        "Daftar pustaka ini memuat seluruh literatur acuan akademis, standar manajemen proyek internasional PMI, "
        "serta rujukan ilmiah mengenai dinamika tim dan manajemen konflik yang digunakan dalam penyusunan Lembar Kerja Mahasiswa (LKM) Pertemuan 9 "
        "mengikuti format baku APA 7th Edition (American Psychological Association):")

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
        "Fisher, R., Ury, W., & Patton, B. (2011). Getting to Yes: Negotiating Agreement Without Giving In (3rd ed.). New York, NY: Penguin Books.")

    add_hanging_indent_p(doc,
        "Jehn, K. A. (1995). A multimethod examination of the benefits and detriments of intragroup conflict. Administrative Science Quarterly, 40(2), 256–282. https://doi.org/10.2307/2393638")

    add_hanging_indent_p(doc,
        "Kerzner, H. (2017). Project Management: A Systems Approach to Planning, Scheduling, and Controlling (12th ed.). Hoboken, NJ: John Wiley & Sons.")

    add_hanging_indent_p(doc,
        "Larson, E. W., & Gray, C. F. (2021). Project Management: The Managerial Process (8th ed.). New York, NY: McGraw-Hill Education.")

    add_hanging_indent_p(doc,
        "Mohammed, S., & Angell, L. C. (2004). Surface- and deep-level diversity in workgroups: Examining the moderating effects of team orientation and team process on relationship conflict. Journal of Organizational Behavior, 25(8), 1015–1039. https://doi.org/10.1002/job.293")

    add_hanging_indent_p(doc,
        "Project Management Institute. (2017). A Guide to the Project Management Body of Knowledge (PMBOK® Guide) (6th ed.). Newtown Square, PA: Project Management Institute, Inc.")

    add_hanging_indent_p(doc,
        "Schwalbe, K. (2019). Information Technology Project Management (9th ed.). Boston, MA: Cengage Learning.")

    add_hanging_indent_p(doc,
        "Thomas, K. W., & Kilmann, R. H. (1974). Thomas-Kilmann Conflict Mode Instrument. Mountain View, CA: Xicom / CPP, Inc.")

    add_hanging_indent_p(doc,
        "Tuckman, B. W. (1965). Developmental sequence in small groups. Psychological Bulletin, 63(6), 384–399. https://doi.org/10.1037/h0022100")

    add_hanging_indent_p(doc,
        "Tuckman, B. W., & Jensen, M. A. C. (1977). Stages of small-group development revisited. Group & Organization Studies, 2(4), 419–427. https://doi.org/10.1177/105960117700200404")

    add_hanging_indent_p(doc,
        "Verma, V. K. (1998). Conflict management. In Project Management Institute (Ed.), Project Management Handbook (pp. 353–376). Newtown Square, PA: Project Management Institute, Inc.")
