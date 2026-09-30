# -*- coding: utf-8 -*-
"""
Section C Builder: Tugas Ringkasan Individu
PMI18 Bab 4.1 – 4.2 (Hal. 75–89)
"""

import docx
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_c(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_heading_2 = helpers['add_heading_2']
    add_heading_3 = helpers['add_heading_3']
    add_body_p = helpers['add_body_p']
    add_num_p = helpers['add_num_p']
    add_bullet_p = helpers['add_bullet_p']
    create_table = helpers['create_table']
    
    add_heading_1(doc, "B. TUGAS RINGKASAN INDIVIDU: TELAAH PMI18 BAB 4.1 s.d. 4.2 (HAL. 75-89)")
    
    add_body_p(doc, 
        "Ringkasan akademis ini menyajikan telaah mendalam terhadap dua proses fondasional dalam manajemen integrasi proyek "
        "sebagaimana diatur dalam PMBOK Guide Edisi Ke-6 (PMI, 2018): Bab 4.1 Develop Project Charter (hal. 75-81) dan "
        "Bab 4.2 Develop Project Management Plan (hal. 82-89). Kedua proses ini membentuk fondasi tata kelola proyek dari fase "
        "konseptual hingga fase perencanaan operasional komprehensif.")

    # 1. Develop Project Charter
    add_heading_2(doc, "1. Telaah Proses Develop Project Charter (PMBOK Guide Bab 4.1, hal. 75-81)")
    add_body_p(doc, 
        "Develop Project Charter adalah proses mengembangkan dokumen yang secara formal mengotorisasi keberadaan suatu proyek "
        "dan memberikan wewenang kepada manajer proyek untuk menggunakan sumber daya organisasi dalam aktivitas-aktivitas proyek. "
        "Manfaat utama proses ini adalah menghasilkan keterikatan yang jelas antara proyek dengan sasaran strategis organisasi, "
        "menciptakan catatan formal atas keberadaan proyek, serta menetapkan batas langsung bagi penerimaan proyek oleh manajemen senior.")
        
    add_body_p(doc, 
        "Struktur ITTO (Inputs, Tools & Techniques, Outputs) dari proses Develop Project Charter disajikan dalam Tabel 3 di bawah ini:")
        
    headers_itto1 = ["Elemen ITTO", "Komponen Standar PMBOK Guide 6th Edition", "Deskripsi dan Esensi Fungsi"]
    data_itto1 = [
        [
            "INPUTS",
            "1. Business Documents:\n   - Business Case\n   - Benefits Management Plan\n2. Agreements\n3. Enterprise Environmental Factors (EEFs)\n4. Organizational Process Assets (OPAs)",
            "• Business Case menentukan kelayakan finansial dan justifikasi investasi.\n"
            "• Benefits Management Plan menjelaskan bagaimana manfaat proyek akan diwujudkan dan diukur.\n"
            "• Agreements mendokumentasikan niat awal, kontrak, atau MoU dengan pihak eksternal/internal.\n"
            "• EEFs & OPAs mencakup regulasi pemerintah, budaya korporat, template charter, dan database historis."
        ],
        [
            "TOOLS & TECHNIQUES",
            "1. Expert Judgment\n2. Data Gathering:\n   - Brainstorming\n   - Focus Groups\n   - Interviews\n3. Interpersonal & Team Skills:\n   - Conflict Management\n   - Facilitation\n   - Meeting Management\n4. Meetings",
            "• Penilaian ahli dari konsultan, PMO, atau asosiasi industri untuk validasi kelayakan.\n"
            "• Teknik pengumpulan data dari pemangku kepentingan kunci dan sponsor.\n"
            "• Keterampilan interpersonal untuk memediasi perbedaan ekspektasi stakeholder dan memfasilitasi konsensus sasaran proyek.\n"
            "• Pertemuan formal kickoff inisiasi bersama penyedia dana."
        ],
        [
            "OUTPUTS",
            "1. Project Charter\n2. Assumption Log",
            "• Project Charter: Dokumen formal otorisasi proyek memuat tujuan SMART, batasan makro, anggaran awal, jadwal milestone, dan mandat wewenang PM.\n"
            "• Assumption Log: Dokumen hidup yang mencatat seluruh asumsi strategis dan kendala operasional tingkat tinggi yang diidentifikasi sejak awal inisiasi."
        ]
    ]
    create_table(doc, [3.2, 5.0, 6.6], headers_itto1, data_itto1, 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.JUSTIFY])

    # 2. Develop Project Management Plan
    add_heading_2(doc, "2. Telaah Proses Develop Project Management Plan (PMBOK Guide Bab 4.2, hal. 82-89)")
    add_body_p(doc, 
        "Develop Project Management Plan adalah proses mendefinisikan, menyiapkan, dan mengoordinasikan seluruh rencana subsistem "
        "(subsidiary plans) serta baselines kinerja, kemudian mengintegrasikannya ke dalam satu dokumen rencana manajemen proyek yang komprehensif. "
        "Manfaat utama proses ini adalah menghasilkan dokumen acuan tunggal yang terintegrasi (single source of truth) yang mendefinisikan "
        "dasar dari seluruh pekerjaan proyek dan bagaimana pekerjaan tersebut akan dieksekusi, dipantau, dikendalikan, dan ditutup.")
        
    add_body_p(doc, 
        "Struktur ITTO (Inputs, Tools & Techniques, Outputs) dari proses Develop Project Management Plan disajikan dalam Tabel 4 di bawah ini:")
        
    headers_itto2 = ["Elemen ITTO", "Komponen Standar PMBOK Guide 6th Edition", "Deskripsi dan Esensi Fungsi"]
    data_itto2 = [
        [
            "INPUTS",
            "1. Project Charter\n2. Outputs from Other Processes\n3. Enterprise Environmental Factors (EEFs)\n4. Organizational Process Assets (OPAs)",
            "• Project Charter menjadi titik tolak batasan makro dan sasaran tingkat tinggi proyek.\n"
            "• Outputs from other processes mencakup seluruh rencana dan baseline dari 9 area pengetahuan lainnya (seperti schedule baseline dari manajemen jadwal, cost baseline dari manajemen biaya).\n"
            "• EEFs & OPAs meliputi sistem informasi manajemen proyek (PMIS), kebijakan pengadaan, dan prosedur pengendalian perubahan baku."
        ],
        [
            "TOOLS & TECHNIQUES",
            "1. Expert Judgment\n2. Data Gathering:\n   - Brainstorming\n   - Checklists\n   - Focus Groups\n   - Interviews\n3. Interpersonal & Team Skills:\n   - Conflict Management\n   - Facilitation\n   - Meeting Management\n4. Meetings",
            "• Pertimbangan para ahli teknis, arsitek sistem, manajer fungsional, dan akuntan biaya.\n"
            "• Checklists untuk memastikan tidak ada komponen subsidiary plan atau prosedur kepatuhan mutu yang terlewatkan.\n"
            "• Fasilitasi diskusi lintas bidang guna menyelaraskan konflik alokasi sumber daya antar-divisi."
        ],
        [
            "OUTPUTS",
            "1. Project Management Plan\n   (Terdiri atas:\n   - 10 Subsidiary Plans\n   - 3 Baselines Kinerja\n   - Komponen Tambahan)",
            "• Dokumen rencana induk terpadu yang memuat: Scope, Requirements, Schedule, Cost, Quality, Resource, Communications, Risk, Procurement, dan Stakeholder Plans.\n"
            "• Performance Measurement Baseline (PMB) yang terdiri atas Scope Baseline (WBS), Schedule Baseline, dan Cost Baseline.\n"
            "• Change Management Plan, Configuration Plan, Deskripsi Siklus Hidup, dan Pendekatan Pengembangan."
        ]
    ]
    create_table(doc, [3.2, 5.0, 6.6], headers_itto2, data_itto2, 
                 [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.JUSTIFY])

    add_body_p(doc, 
        "PMBOK Guide menekankan bahwa penyusunan Project Management Plan bukanlah kegiatan sekali jalan (one-time static event), "
        "melainkan menerapkan prinsip Elaborasi Progresif (Progressive Elaboration). Rencana ini terus diperbarui dan diperdalam seiring "
        "bertambahnya informasi faktual selama siklus hidup proyek melalui mekanisme persetujuan perubahan terpadu (Change Control).")

    # 3. Hubungan Struktural Antara Kedua Proses
    add_heading_2(doc, "3. Analisis Hubungan Antara Kedua Proses Tersebut")
    add_body_p(doc, 
        "Hubungan antara proses Develop Project Charter dan Develop Project Management Plan bersifat sekuensial, hierarkis, dan interdependen "
        "dalam tata kelola manajemen integrasi proyek (PMI, 2018; Kerzner, 2017):")
    add_num_p(doc, "a.", "Aliran Data dan Otorisasi (Hierarchical Ingestion):",
        "Project Charter adalah fondasi awal yang wajib disahkan terlebih dahulu sebelum Develop Project Management Plan dapat dimulai. "
        "Charter bertindak sebagai input primer yang tidak tergantikan bagi PMP. Tanpa charter yang sah, manajer proyek tidak memiliki dasar hukum "
        "maupun batasan terotorisasi untuk meminta waktu kerja dari para ahli fungsional dalam menyusun rencana terperinci.")
    add_num_p(doc, "b.", "Pagar Pembatas Strategis (Strategic Guardrail):",
        "Project Charter mengunci ruang lingkup tingkat tinggi dan sasaran bisnis yang disepakati oleh Sponsor. Selama proses penyusunan PMP, "
        "manajer proyek dan tim harus senantiasa merujuk pada Charter agar rencana detail (seperti dekomposisi WBS dan alokasi anggaran) "
        "tidak melenceng dari batasan yang telah diotorisasi. Charter berfungsi sebagai 'kompas pengarah' agar tim terhindar dari pemborosan sumber daya.")
    add_num_p(doc, "c.", "Evolusi dari Ketidakpastian Makro Menuju Kepastian Mikro:",
        "Kedua proses ini mencerminkan perjalanan peredaman ketidakpastian proyek (cone of uncertainty). Develop Project Charter bekerja pada tingkat "
        "ketidakpastian tinggi dengan mengestimasi durasi dan biaya makro (rough order of magnitude). Sebaliknya, Develop Project Management Plan "
        "mentransformasikan batasan makro tersebut menjadi paket kerja mikro, jadwal jalur kritis (Critical Path Method), dan garis dasar pengukuran kinerja (PMB) "
        "yang memiliki tingkat akurasi presisi tinggi.")

    # 4. Refleksi Singkat Relevansi dengan Proyek Kelompok (PRE-02)
    add_heading_2(doc, "4. Refleksi Singkat Relevansi Kedua Proses dengan Proyek Kelompok (PRE-02)")
    add_body_p(doc, 
        "Kedua proses integrasi di atas memiliki relevansi ganda yang sangat mendalam bagi proyek kelompok kami (PRE-02):")
    add_num_p(doc, "1.", "Relevansi Tata Kelola Proyek Riset Tim PRE-02:",
        "Penyusunan Project Charter pada Pertemuan 3 ini memberikan mandat resmi, memperjelas batasan ruang lingkup 8 pekan perkuliahan, "
        "mengunci alokasi anggaran operasional komputasi GPU Rp 45.000.000,-, serta membagi peran yang tegas antara Nailul (Data/ML), "
        "Mukti (Author/Naskah), dan Rafiq (Sistem/Validasi). Charter ini membentengi tim dari risiko ambisi berlebih (scope creep) "
        "yang dapat menggagalkan penyelesaian tugas akhir.")
    add_num_p(doc, "2.", "Relevansi Objek Penelitian terhadap Data Super ERP FNE:",
        "Dalam penelitian PRE-02, kami mengkaji secara empiris dokumen Project Management Plan (PMP) dari 8 sub-proyek Farm Nation Enterprise. "
        "Variabel bebas yang kami gunakan untuk melatih model Machine Learning—seperti Schedule Performance Index (SPI), Resource Utilization Rate, "
        "dan Predecessor Count—merupakan artefak nyata yang bersumber langsung dari Schedule Baseline dan Resource Management Plan pada dokumen PMP tersebut. "
        "Dengan memahami hakikat kedua proses ini, kami menyadari bahwa akurasi model machine learning kami sangat bergantung pada kualitas "
        "perencanaan baseline yang dirumuskan pada proses Develop Project Management Plan di tingkat konsorsium.")

print("Section C Builder written successfully.")
