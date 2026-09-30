# -*- coding: utf-8 -*-
"""
Section A Builder: Tugas Tertulis Individu
Pertemuan 4: Manajemen Ruang Lingkup Proyek
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_a(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_heading_2 = helpers['add_heading_2']
    add_heading_3 = helpers['add_heading_3']
    add_body_p = helpers['add_body_p']
    add_num_p = helpers['add_num_p']
    add_bullet_p = helpers['add_bullet_p']
    add_subbullet_p = helpers['add_subbullet_p']
    create_table = helpers['create_table']

    add_heading_1(doc, "A. TUGAS TERTULIS INDIVIDU")

    # =========================================================================
    # SOAL 1
    # =========================================================================
    add_heading_2(doc, "1. Apa yang dimaksud dengan manajemen ruang lingkup proyek dan mengapa area pengetahuan ini penting dalam keberhasilan proyek?")
    
    add_body_p(doc,
        "Manajemen Ruang Lingkup Proyek (Project Scope Management) adalah area pengetahuan manajemen proyek yang mencakup proses-proses "
        "yang diperlukan untuk memastikan bahwa proyek mencakup seluruh pekerjaan yang disyaratkan, dan HANYA pekerjaan yang disyaratkan, "
        "untuk menyelesaikan proyek dengan sukses (PMI, 2018, hal. 129). Prinsip esensial dari manajemen ruang lingkup berfokus pada "
        "pendefinisian batas-batas yang tegas (boundary definition) antara apa yang termasuk dalam pekerjaan proyek (in-scope) dan apa yang "
        "berada di luar pekerjaan proyek (out-of-scope). Dengan kata lain, manajemen ruang lingkup bertindak sebagai filter pelindung yang "
        "menjaga agar komitmen deliverable yang telah disepakati antara tim pelaksana dan pemangku kepentingan (stakeholder) tetap "
        "terkendali, terukur, dan tidak terdistorsi sepanjang siklus hidup proyek.")

    add_body_p(doc,
        "Area pengetahuan Manajemen Ruang Lingkup Proyek memegang peranan yang sangat vital dan menentukan bagi keberhasilan proyek "
        "berdasarkan lima alasan fundamental berikut:")

    add_num_p(doc, "1.", "Fondasi Utama Penetapan Batasan Segitiga Besi (The Bedrock of Triple Constraints):",
        "Ruang lingkup adalah pilar penentu ukuran dari dua batasan utama lainnya, yaitu jadwal (waktu) dan anggaran (biaya). "
        "Estimasi durasi aktivitas (Schedule Management) dan estimasi biaya per paket kerja (Cost Management) tidak akan pernah dapat "
        "dilakukan secara realistis tanpa adanya kepastian ruang lingkup yang terdefinisi dengan jelas. Ketidakpastian pada ruang lingkup "
        "secara otomatis akan melipatgandakan risiko deviasi jadwal dan pembengkakan biaya proyek secara eksponensial.")

    add_num_p(doc, "2.", "Benteng Perlindungan terhadap Bahaya Scope Creep dan Biaya Tersembunyi:",
        "Salah satu penyebab kegagalan proyek yang paling lazim dalam industri rekayasa perangkat lunak dan sistem informasi adalah "
        "terjadinya 'scope creep'—yaitu ekspansi fitur atau penambahan tugas tanpa evaluasi dampak formal. Manajemen ruang lingkup "
        "menyediakan mekanisme tata kelola (governance) yang ketat melalui baseline ruang lingkup (scope baseline) dan prosedur perubahan "
        "resmi, sehingga setiap penambahan fungsi harus dikompensasi dengan penyesuaian waktu dan biaya yang seimbang.")

    add_num_p(doc, "3.", "Penyelaras Ekspektasi Pemangku Kepentingan (Managing Stakeholder Expectations):",
        "Kerap kali terjadi kesenjangan persepsi (expectation gap) yang tajam antara apa yang dibayangkan oleh pengguna akhir (user/sponsor) "
        "dengan apa yang dipahami dan dirancang oleh tim pengembang teknis. Manajemen ruang lingkup memfasilitasi proses elisitasi, dokumentasi, "
        "dan verifikasi formal, sehingga seluruh pihak memiliki bahasa dan interpretasi yang seragam mengenai kriteria keberhasilan produk "
        "sebelum eksekusi dimulai.")

    add_num_p(doc, "4.", "Pengendali Fokus Kerja dan Efisiensi Alokasi Sumber Daya Tim:",
        "Dengan batas kerja yang terdokumentasi rapi, tim proyek dapat mencurahkan seluruh konsentrasi, keahlian, dan jam kerja mereka "
        "hanya pada komponen deliverables yang benar-benar memberikan nilai bisnis (business value) bagi organisasi. Hal ini mencegah "
        "terbuangnya waktu dan energi tim untuk mengerjakan fungsi-fungsi sekunder yang tidak esensial atau sekadar keinginan sesaat "
        "tanpa persetujuan sponsor.")

    add_num_p(doc, "5.", "Dasar Formal Pengujian Mutu dan Penerimaan Akhir Produk (Acceptance Baseline):",
        "Sebuah proyek tidak dapat dinyatakan selesai hanya berdasarkan klaim sepihak tim pengembang bahwa aplikasi telah selesai dikoding. "
        "Penerimaan akhir (formal sign-off) oleh sponsor mensyaratkan adanya kriteria penerimaan (acceptance criteria) yang jelas dan terukur. "
        "Manajemen ruang lingkup menyediakan tolok ukur pengujian objektif tersebut melalui dokumen spesifikasi kebutuhan dan WBS Dictionary, "
        "sehingga proses serah terima kontrak dapat berlangsung secara transparan dan berkekuatan hukum tetap.")

    # =========================================================================
    # SOAL 2
    # =========================================================================
    add_heading_2(doc, "2. Sebutkan dan jelaskan secara singkat enam proses dalam manajemen ruang lingkup proyek!")
    
    add_body_p(doc,
        "Mengacu pada standar internasional Project Management Body of Knowledge (PMBOK Guide) Edisi Ke-6 (PMI, 2018, hal. 129–171), "
        "Manajemen Ruang Lingkup Proyek dioperasionalkan melalui enam proses terstruktur yang tersebar dalam dua kelompok proses "
        "(Process Groups), yaitu Kelompok Proses Perencanaan (Planning) dan Kelompok Proses Pemantauan dan Pengendalian (Monitoring & Controlling). "
        "Keenam proses tersebut diuraikan sebagai berikut:")

    add_num_p(doc, "1.", "Plan Scope Management (Merencanakan Manajemen Ruang Lingkup):",
        "Proses menyusun rencana manajemen ruang lingkup yang mendokumentasikan bagaimana ruang lingkup proyek dan produk akan didefinisikan, "
        "divalidasi, dan dikendalikan sepanjang proyek berjalan. Output utama dari proses ini adalah Rencana Manajemen Ruang Lingkup "
        "(Scope Management Plan) dan Rencana Manajemen Kebutuhan (Requirements Management Plan) yang menjadi pedoman operasional bagi tim.")

    add_num_p(doc, "2.", "Collect Requirements (Mengumpulkan Kebutuhan):",
        "Proses menentukan, mendokumentasikan, dan mengelola kebutuhan serta ekspektasi pemangku kepentingan guna mencapai sasaran proyek. "
        "Proses ini menjadi dasar bagi penetapan ruang lingkup produk dan proyek melalui serangkaian teknik elisitasi seperti wawancara, "
        "focus groups, dan workshop. Output utamanya meliputi Dokumentasi Kebutuhan (Requirements Documentation) dan Matriks Penelusuran Kebutuhan "
        "(Requirements Traceability Matrix - RTM).")

    add_num_p(doc, "3.", "Define Scope (Mendefinisikan Ruang Lingkup):",
        "Proses mengembangkan deskripsi terperinci mengenai proyek dan produk yang akan dihasilkan. Berdasarkan hasil analisis kebutuhan, "
        "proses ini menyaring kebutuhan-kebutuhan yang realistis dan menyusun batasan kerja yang tegas. Output utamanya adalah Pernyataan "
        "Ruang Lingkup Proyek (Project Scope Statement) yang memuat deskripsi ruang lingkup, deliverables utama, kriteria penerimaan, "
        "serta batasan (constraints) dan asumsi proyek.")

    add_num_p(doc, "4.", "Create WBS (Membuat Work Breakdown Structure):",
        "Proses memecah (dekomposisi) deliverables proyek dan seluruh pekerjaan proyek menjadi komponen-komponen yang lebih kecil, terstruktur, "
        "dan lebih mudah dikelola hingga mencapai level terendah yang disebut work package. Output utama dari proses ini adalah Scope Baseline, "
        "yang terdiri dari Project Scope Statement yang telah disetujui, bagan WBS, dan Kamus WBS (WBS Dictionary).")

    add_num_p(doc, "5.", "Validate Scope (Memvalidasi Ruang Lingkup):",
        "Proses memformalkan penerimaan (formal sign-off) dari pemangku kepentingan (klien/sponsor) atas deliverables proyek yang telah "
        "diselesaikan dan diverifikasi kualitasnya. Berada pada kelompok proses Pemantauan dan Pengendalian, proses ini berfokus pada "
        "inspeksi deliverables untuk memastikan kesesuaian dengan kriteria penerimaan. Output utamanya adalah Deliverables yang Diterima "
        "(Accepted Deliverables) dan Permintaan Perubahan (Change Requests) jika ditemukan ketidaksesuaian.")

    add_num_p(doc, "6.", "Control Scope (Mengendalikan Ruang Lingkup):",
        "Proses memantau status ruang lingkup proyek dan produk serta mengelola perubahan terhadap baseline ruang lingkup secara proaktif. "
        "Proses ini memastikan bahwa seluruh usulan modifikasi ruang lingkup diproses melalui prosedur formal pengendalian perubahan "
        "(Perform Integrated Change Control) guna mencegah penyusupan ruang lingkup liar (scope creep). Output utamanya meliputi "
        "Informasi Kinerja Pekerjaan (Work Performance Information), Permintaan Perubahan, serta Pembaruan Rencana Manajemen Proyek.")

    add_body_p(doc, "Ringkasan interaksi dan komponen ITTO (Inputs, Tools & Techniques, Outputs) dari keenam proses manajemen ruang lingkup disajikan pada Tabel 1 di bawah ini:")

    # Table 1: 6 Proses Scope Management
    headers_t1 = ["No", "Nama Proses", "Kelompok Proses", "Tujuan Utama", "Input Kunci", "Tools & Techniques", "Output Utama"]
    col_widths_t1 = [0.8, 2.5, 2.2, 3.5, 3.2, 3.2, 3.1]
    data_t1 = [
        [
            "1", "Plan Scope Management", "Planning",
            "Menetapkan pedoman tata kelola pendefinisian, validasi, dan kontrol lingkup proyek.",
            "Project Charter, Project Management Plan, EEFs, OPAs",
            "Expert Judgment, Data Analysis (Alternatives Analysis), Meetings",
            "Scope Management Plan, Requirements Management Plan"
        ],
        [
            "2", "Collect Requirements", "Planning",
            "Menggali dan mendokumentasikan kebutuhan pemangku kepentingan secara komprehensif.",
            "Project Charter, Scope Management Plan, Stakeholder Register",
            "Interviews, Focus Groups, Facilitated Workshops, Prototyping, Surveys",
            "Requirements Documentation, Requirements Traceability Matrix (RTM)"
        ],
        [
            "3", "Define Scope", "Planning",
            "Mengembangkan deskripsi detail proyek dan produk serta menetapkan batasan in/out.",
            "Project Charter, Requirements Documentation, Risk Register",
            "Expert Judgment, Data Analysis, Decision Making, Product Analysis, Interpersonal Skills",
            "Project Scope Statement, Project Documents Updates"
        ],
        [
            "4", "Create WBS", "Planning",
            "Mendekomposisi deliverable menjadi paket kerja (work package) yang mudah dikelola.",
            "Project Scope Statement, Requirements Documentation, OPAs",
            "Decomposition, Expert Judgment",
            "Scope Baseline (Approved Scope Statement, WBS, WBS Dictionary)"
        ],
        [
            "5", "Validate Scope", "Monitoring & Controlling",
            "Memperoleh penerimaan formal dari klien/sponsor atas deliverable yang selesai.",
            "Project Management Plan, Verified Deliverables (dari Control Quality), Work Performance Data",
            "Inspection (Reviews, Product Walkthroughs, Audits), Decision Making",
            "Accepted Deliverables, Work Performance Information, Change Requests"
        ],
        [
            "6", "Control Scope", "Monitoring & Controlling",
            "Memantau status pelaksanaan lingkup dan mengendalikan perubahan baseline.",
            "Scope Baseline, Requirements Traceability Matrix, Work Performance Data",
            "Data Analysis (Variance Analysis, Trend Analysis)",
            "Work Performance Information, Change Requests, Scope Baseline Updates"
        ]
    ]
    create_table(doc, col_widths_t1, headers_t1, data_t1, align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.JUSTIFY, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # =========================================================================
    # SOAL 3
    # =========================================================================
    add_heading_2(doc, "3. Apa perbedaan antara ruang lingkup proyek (project scope) dan ruang lingkup produk (product scope)? Berikan contoh untuk memperjelas!")
    
    add_body_p(doc,
        "Meskipun kata 'ruang lingkup' (scope) sering digunakan secara bergantian dalam percakapan informal, standar profesional PMBOK Guide "
        "(PMI, 2018, hal. 131) membedakan secara tegas antara Ruang Lingkup Produk (Product Scope) dan Ruang Lingkup Proyek (Project Scope). "
        "Memahami distingsi kedua konsep ini adalah syarat mutlak bagi tim proyek guna membedakan antara entitas yang dibangun dan proses "
        "rekayasa yang ditempuh untuk membangunnya.")

    add_bullet_p(doc, "Ruang Lingkup Produk (Product Scope):",
        "Merujuk pada fitur, fungsi, karakteristik fisik, spesifikasi teknis, dan kapabilitas operasional yang mencirikan produk, layanan, "
        "atau hasil akhir yang ingin diwujudkan. Product scope berorientasi pada 'APA yang sedang dibangun' (WHAT is being built / the deliverable). "
        "Keberhasilan pemenuhan product scope diukur berdasarkan spesifikasi kebutuhan produk (product requirements), standar mutu desain, "
        "serta kriteria penerimaan fungsional yang disetujui klien.")

    add_bullet_p(doc, "Ruang Lingkup Proyek (Project Scope):",
        "Merujuk pada seluruh totalitas pekerjaan, aktivitas, proses manajemen, pengujian, koordinasi administratif, dan upaya yang wajib "
        "dilaksanakan oleh tim proyek untuk menghasilkan produk dengan fitur dan fungsi yang telah disyaratkan. Project scope berorientasi "
        "pada 'BAGAIMANA pekerjaan tersebut dilaksanakan' (HOW the work is delivered / the processes, management, and execution effort). "
        "Keberhasilan pemenuhan project scope diukur berdasarkan rencana manajemen proyek, yaitu Scope Baseline (yang mencakup WBS dan WBS Dictionary), "
        "jadwal, dan kepatuhan anggaran.")

    add_heading_3(doc, "Contoh Konkret Penerapan pada Proyek PRE-02 (Sistem Prediksi Probabilitas Keterlambatan Proyek Berbasis Machine Learning):")
    add_body_p(doc,
        "Untuk memperjelas perbedaan di antara keduanya dalam situasi riil, perhatikan implementasi pada proyek kelompok kami (PRE-02):")

    add_bullet_p(doc, "Contoh Product Scope pada Proyek PRE-02:",
        "1) Model Machine Learning klasifikasi probabilistik (Random Forest, Gradient Boosting, dan Neural Network) dengan aktivasi sigmoid "
        "dan kalibrasi Platt Scaling / Isotonic Regression; 2) Antarmuka dasbor web yang menampilkan kurva kalibrasi (Calibration Curve), "
        "skor Brier Score, dan metrik Log Loss; 3) Mekanisme early warning alert otomatis yang memicu status waspada ketika probabilitas keterlambatan "
        "proyek melebihi ambang batas 0.65; 4) Modul REST API dengan endpoint /predict_proba yang menerima payload JSON parameter progres aktual "
        "dan mengembalikan nilai probabilitas float antara 0.00 hingga 1.00.")

    add_bullet_p(doc, "Contoh Project Scope pada Proyek PRE-02:",
        "1) Pelaksanaan wawancara dan workshop pengumpulan data parameter proyek bersama calon pengguna dan dosen pembimbing; 2) Penulisan "
        "dokumen System Requirement Specification (SRS) dan Project Charter; 3) Aktivitas data gathering, data cleansing, dan normalisasi dataset "
        "proyek historis; 4) Perancangan skrip eksperimen pemodelan berbasis Python Scikit-Learn dan PyTorch; 5) Pelaksanaan pengujian cross-validation "
        "k-fold 5-tahap; 6) Penyelenggaraan rapat sprint mingguan tim pengembang; 7) Penyusunan draf laporan riset ilmiah berformat IMRAD; "
        "8) Pelatihan pemanfaatan sistem bagi pengguna akhir; dan 9) Aktivitas penutupan proyek serta pengarsipan kode sumber ke repositori GitHub.")

    add_body_p(doc, "Perbandingan sistematis antara kedua domain ruang lingkup tersebut dirangkum dalam Tabel 2 di bawah ini:")

    # Table 2: Product Scope vs Project Scope
    headers_t2 = ["Dimensi Perbandingan", "Ruang Lingkup Produk (Product Scope)", "Ruang Lingkup Proyek (Project Scope)"]
    col_widths_t2 = [3.5, 7.2, 7.3]
    data_t2 = [
        [
            "Pertanyaan Kunci",
            "APA yang sedang dibangun dan bagaimana wujud/karakteristiknya? (What is to be delivered?)",
            "BAGAIMANA pekerjaan dikerjakan untuk menghasilkan produk tersebut? (How will it be delivered?)"
        ],
        [
            "Fokus Utama",
            "Fitur, fungsi, performa teknis, kapabilitas, dan estetika fisik produk/sistem.",
            "Seluruh aktivitas rekayasa, tata kelola manajemen proyek, penjaminan mutu, logistik, dan pelaporan."
        ],
        [
            "Tolok Ukur Keberhasilan",
            "Diukur dari pemenuhan spesifikasi teknis dan kriteria penerimaan produk (Product Requirements).",
            "Diukur dari kepatuhan terhadap Scope Baseline (WBS), Schedule Baseline, dan Cost Baseline."
        ],
        [
            "Dokumen Rujukan Utama",
            "Product Requirements Document (PRD), System Design Specification, User Manual, Blueprint.",
            "Project Charter, Project Management Plan, Work Breakdown Structure (WBS), WBS Dictionary."
        ],
        [
            "Pihak Penentu Utama",
            "Pengguna akhir (end-user), pemilik produk (Product Owner), sponsor bisnis, dan analis sistem.",
            "Manajer Proyek (Project Manager), Manajer PMO, Scrum Master, dan seluruh tim pelaksana proyek."
        ],
        [
            "Dampak Perubahan",
            "Perubahan kebutuhan produk akan secara langsung mengubah arsitektur teknis produk.",
            "Perubahan proses pengerjaan (misal dari Waterfall ke Agile) belum tentu mengubah fitur akhir produk."
        ],
        [
            "Penyelesaian (Completion)",
            "Dinyatakan selesai saat produk diuji dan diterima (accepted) secara fungsional oleh klien.",
            "Dinyatakan selesai saat seluruh kontrak ditutup, aset diarsipkan, dan tim dibubarkan (Project Closure)."
        ]
    ]
    create_table(doc, col_widths_t2, headers_t2, data_t2, align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # =========================================================================
    # SOAL 4
    # =========================================================================
    add_heading_2(doc, "4. Sebutkan minimal empat teknik yang dapat digunakan untuk mengumpulkan kebutuhan pemangku kepentingan dan jelaskan kelebihan masing-masing!")
    
    add_body_p(doc,
        "Dalam proses Collect Requirements (PMI, 2018, hal. 142–145), manajer proyek dan tim analis dapat memanfaatkan berbagai teknik elisitasi "
        "kebutuhan guna mengekstraksi ekspektasi, kebutuhan fungsional, dan kebutuhan non-fungsional dari pemangku kepentingan. "
        "Berikut disajikan enam teknik utama beserta analisis kelebihan dan karakteristik implementasinya:")

    add_num_p(doc, "1.", "Wawancara Mendalam (In-Depth Interviews):",
        "Teknik interaksi langsung secara tatap muka (one-on-one) atau daring antara analis dan pemangku kepentingan kunci dengan "
        "mengajukan pertanyaan terstruktur, semi-terstruktur, atau terbuka guna menggali informasi yang bersifat konfidensial atau spesifik.")
    add_subbullet_p(doc, "Kelebihan Utama:",
        "Sangat efektif untuk membangun hubungan interpersonal dan kepercayaan; mampu menggali pengetahuan tersirat (tacit knowledge) "
        "serta kebutuhan emosional yang sulit diungkapkan secara tertulis; memungkinkan analis mengamati bahasa tubuh, menangkap nada bicara, "
        "dan langsung mengajukan pertanyaan klarifikasi mendalam saat muncul pernyataan yang ambigu.")

    add_num_p(doc, "2.", "Lokakarya Terfasilitasi (Facilitated Workshops / JAD / QFD):",
        "Sesi kerja kolaboratif terstruktur yang mempertemukan seluruh pemangku kepentingan lintas fungsional (pengembang, desainer, manajer bisnis, "
        "dan perwakilan pengguna akhir) yang dipandu oleh fasilitator netral untuk menyelaraskan ekspektasi dan merumuskan kebutuhan produk secara cepat.")
    add_subbullet_p(doc, "Kelebihan Utama:",
        "Mempercepat penyelarasan persepsi lintas divisi secara dramatis; secara instan menyelesaikan konflik kepentingan antardepartemen "
        "melalui musyawarah terarah; membangun rasa memiliki (shared ownership) dan komitmen bersama yang tinggi atas ruang lingkup solusi yang disepakati.")

    add_num_p(doc, "3.", "Kelompok Terfokus (Focus Groups):",
        "Pertemuan terarah yang menghadirkan perwakilan pemangku kepentingan dan Subject Matter Experts (SMEs) yang telah dikualifikasi "
        "sebelumnya untuk mendiskusikan topik, preferensi, atau permasalahan produk tertentu di bawah bimbingan moderator profesional.")
    add_subbullet_p(doc, "Kelebihan Utama:",
        "Mendorong dinamika interaksi kelompok yang hidup, di mana ide atau masukan dari satu peserta dapat memicu tanggapan "
        "kritis dan ide-ide baru dari peserta lain; sangat efisien untuk memvalidasi konsep fitur atau desain produk sebelum masuk ke fase rekayasa penuh.")

    add_num_p(doc, "4.", "Kuesioner dan Survei (Questionnaires and Surveys):",
        "Kumpulan pertanyaan tertulis terstruktur (pilihan ganda, skala Likert, dan isian singkat) yang didistribusikan kepada responden target "
        "dalam jumlah besar melalui instrumen digital (seperti Google Forms atau platform survei daring).")
    add_subbullet_p(doc, "Kelebihan Utama:",
        "Mampu menjangkau audiens pemangku kepentingan yang sangat luas dan tersebar secara geografis dalam waktu singkat dengan biaya murah; "
        "menghasilkan data kuantitatif objektif yang dapat dianalisis secara statistik; serta menjamin privasi/anonimitas responden sehingga masukan "
        "yang diperoleh cenderung lebih jujur dan objektif.")

    add_num_p(doc, "5.", "Pembuatan Prototipe (Prototyping & Storyboarding):",
        "Metode penyediaan model kerja awal (working model), mock-up visual interaktif, atau wireframe dari produk sebelum produk final dibangun.")
    add_subbullet_p(doc, "Kelebihan Utama:",
        "Mengubah konsep abstrak menjadi representasi visual konkret yang dapat disentuh dan dioperasikan langsung oleh pengguna; "
        "secara drastis menekan risiko ambiguitas kebutuhan; serta memungkinkan siklus umpan balik cepat (rapid feedback loop) sehingga kesalahan desain "
        "dapat diperbaiki sebelum investasi coding besar-besaran dilakukan.")

    add_num_p(doc, "6.", "Analisis Dokumen (Document Analysis):",
        "Proses penelaahan mendalam terhadap artefak organisasi yang sudah ada, seperti SOP, undang-undang kepatuhan, laporan audit sistem, "
        "kontrak bisnis, diagram alir proses eksisting, dan dokumentasi sistem warisan (legacy systems).")
    add_subbullet_p(doc, "Kelebihan Utama:",
        "Sangat efisien dan hemat biaya karena tidak menyita waktu wawancara pemangku kepentingan yang padat; memberikan landasan data faktual "
        "mengenai aturan bisnis formal organisasi; serta mampu mengungkap kebutuhan tersembunyi yang terlupakan oleh pengguna saat wawancara.")

    add_body_p(doc, "Matriks evaluasi komparatif teknik pengumpulan kebutuhan disajikan pada Tabel 3 di bawah ini:")

    # Table 3: Comparative Analysis of Requirement Gathering Techniques
    headers_t3 = ["Teknik Elisitasi", "Kelebihan Utama", "Kelemahan/Keterbatasan", "Konteks Penggunaan Paling Tepat"]
    col_widths_t3 = [2.8, 5.5, 5.5, 4.2]
    data_t3 = [
        [
            "Wawancara (Interviews)",
            "Interaksi personal mendalam, fleksibel, mampu menangkap nuansa emosional dan kebutuhan tersirat.",
            "Membutuhkan waktu lama, biaya tinggi, rawan bias pewawancara, data kualitatif sulit diagregasi.",
            "Menggali visi strategis dari eksekutif/sponsor dan kebutuhan spesifik para ahli kunci."
        ],
        [
            "Lokakarya (Facilitated Workshops)",
            "Konsensus cepat, menyelaraskan perselisihan lintas bidang, efisiensi waktu, komitmen tinggi.",
            "Memerlukan fasilitator berpengalaman, logistik rumit, potensi didominasi peserta vokal.",
            "Inisiasi proyek berskala besar dengan pemangku kepentingan yang memiliki kepentingan berbeda."
        ],
        [
            "Kelompok Terfokus (Focus Groups)",
            "Menghasilkan ide-ide spontan melalui dinamika kelompok, diskusi terfokus bersama pakar.",
            "Peserta pasif enggan bicara, potensi groupthink, kesimpulan tidak mencerminkan populasi luas.",
            "Eksplorasi persepsi pasar, preferensi antarmuka pengguna, dan analisis penerimaan konsep."
        ],
        [
            "Kuesioner & Survei",
            "Jangkauan populasi masif, biaya per responden rendah, hasil terukur secara statistik, anonim.",
            "Pertanyaan kaku tanpa klarifikasi instan, tingkat respons sering rendah, rawan salah tafsir.",
            "Menilai tingkat kepuasan ribuan pengguna akhir dan memprioritaskan fitur pada produk massal."
        ],
        [
            "Prototipe (Prototyping)",
            "Konkret, mengurangi multitafsir, umpan balik dini sangat akurat, validasi kelayakan desain.",
            "Pengguna mengira sistem sudah selesai, biaya pembuatan mockup awal, potensi gold plating.",
            "Pengembangan perangkat lunak interaktif, desain UI/UX web/mobile, sistem AI baru."
        ],
        [
            "Analisis Dokumen",
            "Data faktual terverifikasi, independen dari jadwal narasumber, biaya sangat ekonomis.",
            "Dokumen sering usang (outdated), tidak mencerminkan praktik lapangan aktual, butuh waktu baca.",
            "Proyek modernisasi sistem legasi, migrasi basis data, dan kepatuhan regulasi industri."
        ]
    ]
    create_table(doc, col_widths_t3, headers_t3, data_t3, align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # =========================================================================
    # SOAL 5
    # =========================================================================
    add_heading_2(doc, "5. Apa yang dimaksud dengan Work Breakdown Structure (WBS) dan apa fungsi utamanya dalam manajemen proyek?")
    
    add_body_p(doc,
        "Berdasarkan standar PMBOK Guide Edisi Ke-6 (PMI, 2018, hal. 156) dan literatur fundamental Larson & Gray (2021, hal. 125), "
        "Work Breakdown Structure (WBS) didefinisikan sebagai dekomposisi hierarkis yang berorientasi pada deliverables (deliverable-oriented "
        "hierarchical decomposition) dari seluruh ruang lingkup pekerjaan yang harus dilaksanakan oleh tim proyek untuk mencapai tujuan "
        "proyek dan menghasilkan deliverables yang disyaratkan. WBS mengorganisasikan dan mendefinisikan totalitas ruang lingkup proyek "
        "dalam bentuk diagram pohon (tree structure) atau daftar berindentasi (outline format). Elemen pada level terendah dari WBS "
        "disebut sebagai Work Package (paket kerja), yaitu unit pekerjaan terkecil yang dapat diestimasi durasi dan biayanya, dijadwalkan, "
        "dimonitor, serta dikendalikan secara independen oleh penanggung jawab tunggal.")

    add_body_p(doc,
        "WBS bukan sekadar daftar tugas (to-do list) acak, melainkan artefak paling sentral yang mendasari seluruh perencanaan proyek. "
        "Adapun enam fungsi utama WBS dalam manajemen proyek meliputi:")

    add_num_p(doc, "1.", "Pondasi Utama Penjadwalan Proyek (Foundation for Activity Scheduling):",
        "WBS memecah deliverable makro menjadi work packages yang terukur. Dari work package inilah proses berikutnya (Define Activities "
        "pada Project Schedule Management) dapat mendefinisikan daftar aktivitas spesifik, menentukan urutan ketergantungan (precedence relationship), "
        "serta membentuk diagram jaringan kerja (network diagram) untuk menemukan Jalur Kritis (Critical Path).")

    add_num_p(doc, "2.", "Kerangka Kerja Estimasi Biaya dan Penganggaran Terperinci (Bottom-Up Cost Budgeting):",
        "Melalui struktur hierarki WBS, tim manajemen proyek dapat melakukan teknik estimasi biaya dari bawah ke atas (bottom-up estimating). "
        "Biaya tenaga kerja, perangkat lunak, lisensi, dan material diestimasi secara presisi pada level work package, lalu diagregasikan "
        "secara bertingkat (cost roll-up) ke control accounts hingga membentuk Baseline Anggaran Biaya Proyek (Cost Baseline).")

    add_num_p(doc, "3.", "Penegakan Akuntabilitas Kerja Melalui Penugasan Sumber Daya (RAM/RACI Mapping):",
        "WBS memungkinkan integrasi yang mulus dengan Struktur Rincian Organisasi (Organizational Breakdown Structure - OBS). "
        "Titik temu antara elemen WBS dan unit OBS membentuk Control Account dan Responsibility Assignment Matrix (RAM) atau matriks RACI "
        "(Responsible, Accountable, Consulted, Informed), yang memastikan setiap paket pekerjaan memiliki satu individu penanggung jawab mutlak "
        "(single point of accountability).")

    add_num_p(doc, "4.", "Basis Sistem Pengendalian Kinerja Terintegrasi (Earned Value Management / EVM):",
        "Dalam fase eksekusi dan pengendalian, kemajuan fisik proyek diukur berdasarkan penyelesaian deliverable pada masing-masing work package. "
        "Hal ini menjadi dasar kalkulasi parameter Earned Value Management—seperti Planned Value (PV), Earned Value (EV), dan Actual Cost (AC)—guna "
        "mengevaluasi varians jadwal (Schedule Variance) dan varians biaya (Cost Variance) secara objektif dan matematis.")

    add_num_p(doc, "5.", "Alat Komunikasi Transparan dan Penyelaras Visi Tim (Universal Scope Communication):",
        "WBS menyajikan visualisasi holistik tingkat tinggi yang intuitif mengenai keseluruhan arsitektur proyek. Artefak ini menjadi sarana "
        "komunikasi efektif bagi sponsor, eksekutif, analis, developer, hingga klien, sehingga semua pihak dapat melihat secara transparan "
        "kontribusi modul kerja masing-masing terhadap gambaran besar proyek.")

    add_num_p(doc, "6.", "Instrumen Identifikasi dan Mitigasi Risiko Proyek (Structured Risk Breakdown):",
        "WBS memfasilitasi proses identifikasi risiko secara terstruktur. Tim proyek dapat menelaah potensi kegagalan, kendala teknis, "
        "dan ketidakpastian secara spesifik pada masing-masing paket kerja, bukan sekadar menebak risiko di tingkat proyek secara makro.")

    # =========================================================================
    # SOAL 6
    # =========================================================================
    add_heading_2(doc, "6. Jelaskan apa yang dimaksud dengan aturan 100% (100% rule) dalam pembuatan WBS dan mengapa aturan ini penting!")
    
    add_body_p(doc,
        "Aturan 100% (The 100% Rule) adalah aksioma dan kaidah emas paling fundamental dalam penyusunan Work Breakdown Structure yang "
        "pertama kali dirumuskan secara formal oleh Gregory T. Haugan (2002) dan diintegrasikan secara ketat dalam standar PMBOK Guide "
        "(PMI, 2018, hal. 161). Aturan ini menyatakan bahwa:")

    add_body_p(doc,
        "\"WBS harus mencakup 100% dari seluruh pekerjaan yang didefinisikan oleh ruang lingkup proyek yang telah disetujui, dan TIDAK MEMUAT "
        "pekerjaan apa pun di luar ruang lingkup tersebut—tidak kurang dan tidak lebih (neither more nor less).\"",
        bold_prefix="Definisi Formal Aturan 100%:")

    add_body_p(doc,
        "Prinsip Aturan 100% ini berlaku secara konsisten dan mutlak pada seluruh tingkatan hierarki WBS (induk dan anak):")

    add_bullet_p(doc, "Konsistensi Agregasi Vertikal (Parent-Child Summation):",
        "Jumlah total pekerjaan, waktu, dan biaya dari elemen-elemen turunan/anak (child elements) pada suatu level hierarki WBS harus "
        "tepat setara dengan 100% pekerjaan dari elemen induknya (parent element). Tidak boleh ada bagian pekerjaan induk yang tertinggal "
        "tanpa terpetakan pada elemen anak, dan elemen anak tidak boleh memuat pekerjaan tambahan yang tidak ada dalam cakupan elemen induk.")

    add_bullet_p(doc, "Penyertaan Seluruh Upaya Manajemen (Inclusion of Project Management Work):",
        "Pekerjaan proyek dalam WBS bukan hanya mencakup deliverable produk fisik atau teknis (seperti coding atau testing), melainkan "
        "wajib menyertakan 100% upaya manajemen proyek itu sendiri (seperti koordinasi rapat, pelaporan status, pengadaan, dan audit kualitas). "
        "Dalam struktur WBS profesional, Manajemen Proyek (Project Management) umumnya ditempatkan sebagai elemen Level 1 tersendiri.")

    add_body_p(doc,
        "Penerapan Aturan 100% ini memegang peranan krusial dan mutlak penting bagi kelangsungan proyek karena empat alasan utama:")

    add_num_p(doc, "1.", "Menjamin Ketiadaan Pekerjaan Tersembunyi yang Tertinggal (Eliminating Blind Spots):",
        "Jika WBS hanya mencakup 90% pekerjaan, berarti terdapat 10% 'pekerjaan siluman' (seperti migrasi basis data, pengujian integrasi beban, "
        "atau pelatihan pengguna) yang tidak direncanakan. Ketika proyek dieksekusi, pekerjaan yang tertinggal ini pasti akan menuntut pengerjaan, "
        "yang seketika menghancurkan jadwal dan anggaran proyek karena ketiadaan alokasi dana.")

    add_num_p(doc, "2.", "Mencegah Terjadinya Scope Creep dan Pekerjaan Gelap (No Extraneous Work):",
        "Sisi sebaliknya dari aturan 100% adalah pelarangan keras mencantumkan pekerjaan melebihi 100%. Tim teknis sering kali tergiur untuk "
        "menambahkan fitur-fitur canggih yang tidak diminta klien (gold plating). Aturan 100% memotong potensi pemborosan sumber daya ini "
        "karena setiap tugas yang dikerjakan wajib memiliki kode sah dalam WBS.")

    add_num_p(doc, "3.", "Menjamin Validitas Matematis Agregasi Anggaran dan Jadwal (Bottom-Up Roll-Up Integrity):",
        "Dalam kalkulasi penganggaran dan estimasi durasi, angka pada level ringkasan diperoleh dari penjumlahan (roll-up) paket kerja di bawahnya. "
        "Aturan 100% memastikan tidak terjadi penghitungan ganda (double-counting) dan tidak ada celah yang terlewat, sehingga angka total anggaran "
        "dan estimasi biaya proyek dapat dipertanggungjawabkan secara audit keuangan.")

    add_num_p(doc, "4.", "Menjaga Kepatuhan Kontraktual dan Kepastian Hukum:",
        "Bagi proyek berbasis kontrak komersial, WBS yang mematuhi aturan 100% menjadi instrumen hukum yang mengikat. Klien tidak dapat "
        "menuntut pekerjaan di luar WBS tanpa addendum kontrak baru, dan kontraktor wajib menyerahkan seluruh paket kerja yang tertera tanpa alasan.")

    # =========================================================================
    # SOAL 7
    # =========================================================================
    add_heading_2(doc, "7. Apa perbedaan antara WBS dan WBS Dictionary? Mengapa WBS Dictionary diperlukan sebagai pelengkap WBS?")
    
    add_body_p(doc,
        "Dalam manajemen ruang lingkup proyek, Work Breakdown Structure (WBS) dan Kamus WBS (WBS Dictionary) adalah dua artefak yang saling "
        "melengkapi dan bersama dengan Project Scope Statement membentuk dokumen dasar yang sah, yaitu Scope Baseline (PMI, 2018, hal. 161–162).")

    add_bullet_p(doc, "Work Breakdown Structure (WBS):",
        "WBS adalah diagram struktur hierarkis grafis (atau daftar berindentasi) yang memvisualisasikan arsitektur dekomposisi ruang lingkup "
        "proyek dari level teratas hingga level paket kerja. Format WBS didesain ringkas, skematis, dan hanya menampilkan Kode WBS (WBS code) "
        "serta Frasa Singkat Judul Deliverable (misal: '1.2.3 Pelatihan Model Random Forest').")

    add_bullet_p(doc, "WBS Dictionary (Kamus WBS):",
        "WBS Dictionary adalah dokumen tekstual naratif terperinci yang menyertai WBS dan memberikan rincian penjelasan operasional, teknis, "
        "dan kontraktual untuk setiap elemen WBS, khususnya pada level paket kerja (work package). WBS Dictionary memuat atribut lengkap, "
        "termasuk kode penomoran, deskripsi rincian tugas (statement of work), deliverables spesifik yang dihasilkan, kriteria penerimaan mutu "
        "(acceptance criteria), penanggung jawab teknis, sumber daya yang dibutuhkan, estimasi durasi dan biaya, batasan dan asumsi, "
        "serta referensi kontrak atau spesifikasi teknis.")

    add_body_p(doc,
        "WBS Dictionary mutlak diperlukan sebagai pelengkap WBS karena alasan-alasan kritis berikut:")

    add_num_p(doc, "1.", "Mengeliminasi Multitafsir dan Kerancuan Semantik dari Judul WBS:",
        "Judul paket kerja pada diagram WBS selalu bersifat singkat (hanya 2–4 kata). Judul seperti 'Desain Basis Data' atau 'Pengembangan Modul API' "
        "dapat ditafsirkan sangat berbeda oleh pihak-pihak terkait. Pengembang mungkin menganggapnya hanya sebatas membuat tabel dasar, sementara "
        "klien membayangkan arsitektur terdistribusi dengan replikasi multi-region. WBS Dictionary memberikan batasan eksplisit mengenai apa "
        "yang sebenarnya harus dikerjakan.")

    add_num_p(doc, "2.", "Menetapkan Batasan Tugas yang Ditegaskan (Explicit Boundary Setting):",
        "WBS Dictionary mendefinisikan dengan jelas apa yang termasuk dalam pekerjaan paket kerja tersebut dan apa yang secara tegas dikecualikan. "
        "Hal ini mencegah developer memperluas pekerjaannya sendiri atau salah mengira bahwa tugas tersebut mencakup tanggung jawab paket kerja lain.")

    add_num_p(doc, "3.", "Menyediakan 'Definition of Done' Melalui Kriteria Penerimaan Mutu Objektif:",
        "Setiap paket kerja dalam WBS Dictionary memuat Acceptance Criteria yang terukur. Dokumen ini menjadi pedoman bagi Quality Assurance (QA) "
        "dan pemangku kepentingan untuk menguji apakah deliverable telah rampung secara sah. Tanpa WBS Dictionary, tim tidak memiliki standar "
        "kesepakatan objektif kapan suatu paket kerja dapat dinyatakan 'selesai 100%'.")

    add_num_p(doc, "4.", "Landasan Pengikatan Tanggung Jawab Operasional dan Kontraktual:",
        "WBS Dictionary menugaskan penanggung jawab spesifik (Accountable Owner) dan merinci kebutuhan sumber daya. Hal ini menjadikannya "
        "dasar kontrak kerja internal yang kuat, sehingga tidak ada celah bagi anggota tim untuk saling melempar tanggung jawab atas keterlambatan tugas.")

    add_body_p(doc, "Tabel komparasi karakteristik antara WBS dan WBS Dictionary disajikan pada Tabel 4 di bawah ini:")

    # Table 4: WBS vs WBS Dictionary
    headers_t4 = ["Parameter Pembeda", "Work Breakdown Structure (WBS)", "Kamus WBS (WBS Dictionary)"]
    col_widths_t4 = [3.5, 7.2, 7.3]
    data_t4 = [
        [
            "Format Penyajian",
            "Diagram pohon hierarkis grafis (chart) atau struktur daftar berindentasi ringkas.",
            "Dokumen naratif berbasis tabel/formulir terstruktur dengan uraian detail per komponen."
        ],
        [
            "Tingkat Kedalaman Detail",
            "Makro dan ringkas; hanya memuat hierarki kode penomoran dan nama deliverables.",
            "Mikro dan komprehensif; memuat ruang lingkup kerja, spesifikasi teknis, dan prasyarat tugas."
        ],
        [
            "Informasi Kriteria Mutu",
            "Tidak mencantumkan kriteria penerimaan teknis maupun standar pengujian.",
            "Memuat kriteria penerimaan (acceptance criteria) dan standar kualitas kelulusan secara rinci."
        ],
        [
            "Alokasi Penanggung Jawab",
            "Hanya menyajikan struktur pembagian kerja tanpa detail nama penanggung jawab.",
            "Mencantumkan penanggung jawab tunggal (owner/lead) dan sumber daya yang dialokasikan."
        ],
        [
            "Peran Utama",
            "Menunjukkan struktur arsitektur dekomposisi totalitas proyek secara visual dan menyeluruh.",
            "Memberikan makna kontekstual, kejelasan batasan, dan petunjuk operasional pelaksanaan kerja."
        ]
    ]
    create_table(doc, col_widths_t4, headers_t4, data_t4, align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # =========================================================================
    # SOAL 8
    # =========================================================================
    add_heading_2(doc, "8. Jelaskan perbedaan antara Validate Scope dan Control Scope dalam hal tujuan, waktu pelaksanaan, dan output yang dihasilkan!")
    
    add_body_p(doc,
        "Meskipun kedua proses ini sama-sama berada di dalam Kelompok Proses Pemantauan dan Pengendalian (Monitoring & Controlling) serta "
        "berfokus pada pengelolaan ruang lingkup proyek, Validate Scope dan Control Scope memiliki orientasi filosofis, tujuan operasional, "
        "waktu pelaksanaan, serta output yang sangat berbeda (PMI, 2018, hal. 163–171).")

    add_body_p(doc,
        "Distingsi fundamental antara kedua proses tersebut dapat dibedakan melalui tiga dimensi utama:")

    add_num_p(doc, "1.", "Tujuan Pelaksanaan (Objectives):",
        "Perbedaan mendasar pada sasaran akhir yang ingin dicapai:")
    add_subbullet_p(doc, "Validate Scope:",
        "Bertujuan untuk memperoleh penerimaan formal (formal customer/sponsor sign-off) dari pemangku kepentingan atas deliverables proyek yang telah diselesaikan. Proses ini berfokus pada kesesuaian deliverables terhadap ekspektasi klien dan kriteria penerimaan produk.")
    add_subbullet_p(doc, "Control Scope:",
        "Bertujuan untuk memantau status pelaksanaan ruang lingkup proyek dan produk, membandingkan performa aktual terhadap Scope Baseline, serta mengendalikan perubahan yang diajukan guna mencegah pembengkakan ruang lingkup yang tidak terkendali (scope creep).")

    add_num_p(doc, "2.", "Waktu Pelaksanaan (Timing & Frequency):",
        "Perbedaan pada momentum dan intensitas pelaksanaan:")
    add_subbullet_p(doc, "Validate Scope:",
        "Dilaksanakan secara periodik pada tonggak pencapaian tertentu, yaitu saat suatu deliverable utama selesai diverifikasi kualitasnya secara internal (Control Quality), pada setiap akhir fase siklus hidup proyek, atau pada penutupan akhir proyek.")
    add_subbullet_p(doc, "Control Scope:",
        "Dilaksanakan secara terus menerus dan berkesinambungan (continuously) sepanjang seluruh siklus hidup proyek, mulai dari hari pertama eksekusi hingga hari terakhir penutupan proyek, untuk mengawasi setiap pergerakan tugas harian tim.")

    add_num_p(doc, "3.", "Output yang Dihasilkan (Outputs):",
        "Perbedaan pada artefak hasil luaran proses:")
    add_subbullet_p(doc, "Validate Scope:",
        "Output utamanya adalah Deliverables yang Diterima Secara Resmi (Accepted Deliverables) yang ditandatangani oleh klien/sponsor, serta Permintaan Perubahan (Change Requests) jika deliverable ditolak atau membutuhkan penyempurnaan (defect repair).")
    add_subbullet_p(doc, "Control Scope:",
        "Output utamanya adalah Informasi Kinerja Pekerjaan (Work Performance Information) berupa analisis varians ruang lingkup, Permintaan Perubahan tindakan korektif/preventif, serta Pembaruan Rencana Manajemen Proyek (terutama revisi Scope Baseline jika perubahan disetujui CCB).")

    add_body_p(doc, "Perbandingan komparatif mendalam antara Validate Scope dan Control Scope disajikan secara komprehensif pada Tabel 5 di bawah ini:")

    # Table 5: Validate Scope vs Control Scope
    headers_t5 = ["Dimensi Analisis", "Proses Validate Scope", "Proses Control Scope"]
    col_widths_t5 = [3.2, 7.4, 7.4]
    data_t5 = [
        [
            "Definisi Esensial",
            "Proses memformalkan penerimaan dari klien/sponsor atas deliverables proyek yang telah selesai.",
            "Proses memantau status ruang lingkup proyek dan produk serta mengelola perubahan baseline."
        ],
        [
            "Fokus Perhatian Utama",
            "Penerimaan pelanggan (Customer/Stakeholder Acceptance) atas hasil deliverables nyata.",
            "Pengendalian varians kinerja dan pencegahan perubahan liar (Scope Creep Prevention)."
        ],
        [
            "Waktu Pelaksanaan",
            "Periodik; dilakukan pada akhir penyelesaian deliverable, akhir fase, atau akhir proyek.",
            "Kontinu dan proaktif; dipantau secara harian/mingguan sepanjang proyek berjalan."
        ],
        [
            "Aktor Utama yang Terlibat",
            "Klien eksternal, Sponsor proyek, Komite Penerimaan, didampingi oleh Manajer Proyek.",
            "Manajer Proyek, Tim Analis Pengendali, Project Controller, dan Tim Pengembang internal."
        ],
        [
            "Keterkaitan dengan Quality",
            "Menerima Verified Deliverables yang telah lolos uji akurasi teknis dari proses Control Quality.",
            "Memantau apakah aktivitas aktual tim menyimpang dari Scope Baseline yang disepakati."
        ],
        [
            "Teknik Analisis Kunci",
            "Inspeksi (Inspection), Product Walkthroughs, Uji Penerimaan Pengguna (User Acceptance Testing).",
            "Analisis Data (Variance Analysis, Trend Analysis, Earned Value Scope Tracking)."
        ],
        [
            "Output Utama",
            "Accepted Deliverables (formal sign-off), Change Requests (jika ada cacat), Dokumen Pembaruan.",
            "Work Performance Information (Scope Variance), Change Requests (koreksi), Scope Baseline Updates."
        ],
        [
            "Konsekuensi Jika Gagal",
            "Sponsor menolak serah terima produk akhir, perselisihan pembayaran, dan penahanan dana kontrak.",
            "Terjadinya perluasan ruang lingkup liar (scope creep), keterlambatan jadwal masif, dan kebangkrutan biaya."
        ]
    ]
    create_table(doc, col_widths_t5, headers_t5, data_t5, align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT])

    # =========================================================================
    # SOAL 9
    # =========================================================================
    add_heading_2(doc, "9. Apa yang dimaksud dengan scope creep dan bagaimana cara mencegahnya?")
    
    add_body_p(doc,
        "Scope Creep didefinisikan dalam PMBOK Guide (PMI, 2018, hal. 168) sebagai ekspansi atau perluasan ruang lingkup produk atau proyek "
        "yang terjadi secara tidak terkendali (uncontrolled expansion) tanpa adanya penyesuaian yang proporsional terhadap parameter batasan lainnya, "
        "yaitu jadwal (waktu), anggaran (biaya), dan alokasi sumber daya. Fenomena scope creep biasanya merayap secara perlahan dan halus "
        "melalui permintaan-permintaan kecil yang tampaknya sepele—seperti permintaan pengguna: 'Tolong tambahkan satu tombol kecil di halaman ini' "
        "atau 'Bisakah format laporannya diubah sedikit?'. Namun akumulasi dari puluhan permintaan informal ini pada akhirnya menyebabkan tim "
        "mengalami beban kerja berlebih, kehabisan anggaran, dan keterlambatan jadwal rilis yang parah.")

    add_body_p(doc,
        "Scope creep umumnya dipicu oleh beberapa akar masalah: 1) Definisi ruang lingkup awal yang ambigu dan tidak tuntas; 2) Komunikasi "
        "informal langsung antara klien dan developer tanpa sepengetahuan manajer proyek; 3) Ketidakmampuan manajer proyek bersikap asertif "
        "dalam menolak permintaan sponsor; dan 4) Praktik 'gold plating', yaitu kebiasaan developer menambahkan fitur mewah tanpa diminta "
        "karena motif kepuasan teknis pribadi.")

    add_body_p(doc,
        "Untuk mencegah dan memitigasi bahaya fatal scope creep, manajemen proyek modern menerapkan enam strategi komprehensif berikut:")

    add_num_p(doc, "1.", "Menyusun Scope Baseline dan Scope Statement yang Rinci dan Eksplisit di Awal Proyek:",
        "Pencegahan paling efektif dilakukan pada fase perencanaan. Pernyataan Ruang Lingkup Proyek (Project Scope Statement) harus ditulis "
        "secara sangat spesifik dengan mencantumkan bukan hanya apa yang termasuk dalam proyek (in-scope), tetapi secara eksplisit memuat "
        "daftar hal-hal yang TIDAK termasuk dalam proyek (out-of-scope). Hal ini menetapkan ekspektasi yang tegas sejak awal.")

    add_num_p(doc, "2.", "Menegakkan Prosedur Formal Pengendalian Perubahan (Perform Integrated Change Control):",
        "Setiap permintaan penambahan, modifikasi, atau pengurangan fitur—tanpa terkecuali—harus diajukan secara tertulis melalui formulir "
        "Permintaan Perubahan resmi (Change Request Form). Tim proyek dilarang keras mengubah satu baris kode pun atas instruksi lisan. "
        "Permintaan tersebut harus dievaluasi dampaknya terhadap biaya dan waktu secara holistik, lalu disetujui secara resmi oleh Dewan "
        "Pengendali Perubahan (Change Control Board - CCB) sebelum dieksekusi.")

    add_num_p(doc, "3.", "Memanfaatkan Matriks Penelusuran Kebutuhan (Requirements Traceability Matrix - RTM):",
        "RTM menghubungkan setiap kebutuhan fungsional perangkat lunak secara langsung ke tujuan bisnis di Project Charter. "
        "Ketika seorang pemangku kepentingan meminta fitur baru, manajer proyek dapat menguji fitur tersebut menggunakan RTM: "
        "apakah fitur ini mendukung tujuan bisnis yang disahkan? Jika tidak memiliki korelasi bisnis yang valid, permintaan tersebut dapat "
        "ditolak secara objektif atau dialihkan ke rilis versi berikutnya.")

    add_num_p(doc, "4.", "Melarang Keras Praktik 'Gold Plating' di Tingkat Tim Teknis:",
        "Manajer proyek harus menanamkan disiplin profesional kepada seluruh programmer dan data scientist bahwa menambahkan fitur ekstra "
        "tanpa persetujuan bukan merupakan tanda kehebatan, melainkan sebuah pelanggaran tata kelola manajemen proyek. Tim hanya diizinkan "
        "membangun apa yang telah disetujui dalam WBS Dictionary.")

    add_num_p(doc, "5.", "Edukasi Pemangku Kepentingan Mengenai Konsekuensi Batasan (Triple Constraints Trade-Off):",
        "Ketika sponsor atau klien meminta penambahan ruang lingkup, manajer proyek tidak boleh hanya sekadar mengatakan 'tidak', melainkan "
        "harus mengedukasi mereka tentang hukum trade-off: 'Kami siap menambahkan fitur prediksi real-time ini, namun hal ini membutuhkan tambahan "
        "biaya server sebesar Rp 15 juta dan perpanjangan jadwal peluncuran selama 3 minggu. Apakah Bapak/Ibu menyetujui kompensasi tersebut?'. "
        "Pendekatan rasional ini membuat pemangku kepentingan berpikir ulang sebelum mengajukan permintaan sembarangan.")

    add_num_p(doc, "6.", "Menerapkan Manajemen Rilis Bertahap Menggunakan Prioritas MoSCoW:",
        "Mengklasifikasikan kebutuhan menggunakan kerangka MoSCoW (Must have, Should have, Could have, Won't have this time). Permintaan baru "
        "yang muncul di tengah jalannya proyek secara default dimasukkan ke dalam kategori 'Won't have this time' untuk dikerjakan pada rilis "
        "fase berikutnya (Phase 2 / next sprint backlog), sehingga ruang lingkup fase berjalan tetap steril.")

    # =========================================================================
    # SOAL 10
    # =========================================================================
    add_heading_2(doc, "10. Buatlah daftar 10 kebutuhan (requirements) untuk proyek kelompok Anda menggunakan teknik wawancara atau kuesioner sederhana kepada pemangku kepentingan yang relevan!")
    
    add_body_p(doc,
        "Untuk proyek kelompok kami, yaitu PRE-02 dengan judul: 'Sistem Prediksi Probabilitas Keterlambatan Proyek Berbasis Machine Learning "
        "sebagai Early Warning System Manajemen Proyek', kami telah melaksanakan elisitasi kebutuhan melalui teknik wawancara mendalam "
        "(in-depth interview) dan kuesioner terstruktur semi-terbuka kepada empat pemangku kepentingan utama, yaitu: 1) Project Manager / "
        "Dosen Pembimbing (selaku Project Sponsor); 2) Lead Data Scientist (selaku Technical Architect); 3) Software Fullstack Engineer "
        "(selaku Tim Implementasi Sistem); dan 4) Project Scheduling Specialist / PMO Officer (selaku Pengguna Akhir / End-User).")

    add_body_p(doc,
        "Berdasarkan sintesis hasil elisitasi dan analisis kebutuhan tersebut, telah dirumuskan 10 kebutuhan spesifik proyek PRE-02 yang mencakup "
        "kebutuhan fungsional (functional requirements), kebutuhan kualitas data & machine learning, serta kebutuhan non-fungsional arsitektural. "
        "Kesepuluh kebutuhan tersebut disajikan dalam bentuk Matriks Penelusuran Kebutuhan (Requirements Traceability Matrix - RTM) pada Tabel 6:")

    # Table 6: RTM 10 Requirements
    headers_t6 = ["ID Req", "Kategori", "Pernyataan Deskripsi Kebutuhan", "Sumber & Teknik", "Prioritas", "Kriteria Penerimaan (Acceptance Criteria)", "Metode Verifikasi"]
    col_widths_t6 = [1.5, 2.0, 4.8, 2.7, 1.8, 3.7, 1.5]
    data_t6 = [
        [
            "REQ-PRE02-01",
            "Fungsional (Data Pipeline)",
            "Sistem harus mampu mengimpor, memvalidasi integritas skema, dan membersihkan dataset historis proyek (format CSV/XLSX) yang mencakup 7 fitur utama (progres aktual, sisa hari deadline, sisa backlog, utilisasi SDM, risiko aktif, frekuensi perubahan, dependency score).",
            "Lead Data Scientist & PMO; Wawancara Mendalam",
            "Must Have (Tinggi)",
            "Sistem berhasil memproses minimal 500 baris data proyek, menangani missing values secara otomatis tanpa crash sistem.",
            "Uji Fungsional & Unit Test"
        ],
        [
            "REQ-PRE02-02",
            "Fungsional (Machine Learning)",
            "Sistem harus mengimplementasikan dan melatih empat arsitektur model klasifikasi probabilistik: Logistic Regression, Random Forest, Gradient Boosting, dan Neural Network dengan output aktivasi sigmoid terkalibrasi.",
            "Dosen Pembimbing & Data Scientist; Wawancara",
            "Must Have (Tinggi)",
            "Keempat algoritma berhasil dieksekusi dengan k-fold cross validation (k=5) dan menghasilkan estimasi nilai probabilitas float kontinu [0.0 - 1.0].",
            "Uji Komputasi & Code Review"
        ],
        [
            "REQ-PRE02-03",
            "Kualitas Performa ML",
            "Model prediksi yang dipilih harus memiliki performa kalibrasi probabilitas yang unggul dengan nilai Brier Score < 0.18 dan Area Under ROC Curve (AUC-ROC) minimal 0.80 pada data pengujian validasi independen.",
            "Project Sponsor & Data Scientist; Kuesioner Teknis",
            "Must Have (Tinggi)",
            "Brier Score terverifikasi secara matematis pada laporan eksperimen dan kurva kalibrasi mendekati garis diagonal ideal 45 derajat.",
            "Evaluasi Metrik Kuantitatif"
        ],
        [
            "REQ-PRE02-04",
            "Fungsional (Early Warning)",
            "Sistem harus memiliki mekanisme peringatan dini (Early Warning Alert) otomatis dengan konfigurasi ambang batas (threshold alert) default sebesar 0.65 untuk mengklasifikasikan status proyek (Aman, Waspada, Bahaya).",
            "PMO Officer & Project Manager; Wawancara Kebutuhan",
            "Must Have (Tinggi)",
            "Ketika input kondisi proyek menghasilkan output probabilitas >= 0.65, sistem secara visual menampilkan badge warna merah bertuliskan 'Status: Keterlambatan Tinggi'.",
            "Demonstrasi Skenario Sistem"
        ],
        [
            "REQ-PRE02-05",
            "Fungsional (REST API)",
            "Sistem harus menyediakan antarmuka Application Programming Interface (REST API) berbasis FastAPI dengan endpoint POST /api/v1/predict_proba yang menerima payload JSON parameter proyek dan mengembalikan respon probabilitas secara instan.",
            "Software Fullstack Engineer; Wawancara Arsitektur",
            "Must Have (Tinggi)",
            "Latency respon API rata-rata di bawah 300 ms per permintaan dan mengembalikan format respon JSON standar dengan status code HTTP 200 OK.",
            "Uji Beban API (Postman / Locust)"
        ],
        [
            "REQ-PRE02-06",
            "Antarmuka (Dashboard UI)",
            "Sistem harus menyediakan antarmuka dasbor monitoring berbasis web yang responsif untuk memvisualisasikan kurva kalibrasi probabilitas, grafik perbandingan model, dan form simulasi interaktif parameter kondisi proyek.",
            "End-User (PMO Officer); Kuesioner Preferensi UI",
            "Should Have (Sedang)",
            "Dasbor web dapat dibuka secara optimal pada resolusi desktop (1920x1080) dan tablet tanpa pergeseran elemen visual (UI breakage).",
            "Inspeksi UI/UX & User Walkthrough"
        ],
        [
            "REQ-PRE02-07",
            "Fungsional (Analisis Fitur)",
            "Sistem harus mampu menyajikan analisis Feature Importance (menggunakan bobot model atau nilai koefisien) untuk menjelaskan faktor kondisi kerja mana yang paling dominan memicu lonjakan risiko keterlambatan proyek.",
            "Project Manager & PMO; Wawancara Mendalam",
            "Should Have (Sedang)",
            "Sistem menampilkan visualisasi diagram batang horizontal 5 fitur teratas yang paling berkontribusi terhadap prediksi keterlambatan.",
            "Uji Fungsional Verifikasi Fitur"
        ],
        [
            "REQ-PRE02-08",
            "Kinerja & Efisiensi",
            "Waktu eksekusi pelatihan ulang model (model retraining) untuk seluruh dataset historis tidak boleh melebihi 120 detik pada lingkungan spesifikasi komputasi standar CPU dual-core tanpa GPU khusus.",
            "Lead Data Scientist; Kuesioner Teknis",
            "Could Have (Rendah)",
            "Log eksekusi training script mencatat total wall-clock execution time di bawah 2 menit pada data uji 1.000 record.",
            "Pengukuran Benchmark Waktu"
        ],
        [
            "REQ-PRE02-09",
            "Keamanan & Hak Akses",
            "Sistem harus menerapkan autentikasi berbasis token JWT (JSON Web Token) untuk membatasi hak akses pengelolaan dataset latih dan pemicu retraining model hanya kepada peran Data Scientist dan Administrator.",
            "Project Sponsor & Fullstack Dev; Wawancara Tata Kelola",
            "Should Have (Sedang)",
            "Akses tanpa token bearer yang valid ditolak oleh backend dengan respon HTTP 401 Unauthorized secara konsisten.",
            "Uji Penetrasi Keamanan API"
        ],
        [
            "REQ-PRE02-10",
            "Tata Kelola & Dokumentasi",
            "Sistem harus disertai dengan dokumentasi teknis lengkap, mencakup User Guide pengoperasian dasbor, dokumentasi API Swagger/OpenAPI, dan laporan ilmiah komparasi eksperimen model berformat IMRAD.",
            "Dosen Pembimbing; Wawancara Persyaratan Akademis",
            "Must Have (Tinggi)",
            "Dokumentasi API Swagger dapat diakses aktif pada URL /docs dan draf dokumen laporan paper IMRAD disetujui oleh dosen pembimbing.",
            "Pemeriksaan Kelengkapan Dokumen"
        ]
    ]
    create_table(doc, col_widths_t6, headers_t6, data_t6, align_cols=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.JUSTIFY, WD_ALIGN_PARAGRAPH.LEFT])

    doc.add_page_break()
