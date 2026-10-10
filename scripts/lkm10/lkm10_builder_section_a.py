# -*- coding: utf-8 -*-
"""
Section A Builder: Tugas Tertulis Individu
Pertemuan 10: Manajemen Komunikasi Proyek
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
    add_heading_2(doc, "1. Apa yang dimaksud dengan manajemen komunikasi proyek dan mengapa area pengetahuan ini penting dalam keberhasilan proyek?")
    add_body_p(doc,
        "Manajemen Komunikasi Proyek (Project Communications Management) adalah area pengetahuan manajemen proyek yang mencakup proses-proses "
        "yang diperlukan untuk memastikan bahwa kebutuhan informasi proyek dan para pemangku kepentingannya (stakeholders) terpenuhi secara tepat "
        "waktu, akurat, dan efektif melalui pengembangan artefak informasi serta pelaksanaan aktivitas komunikasi yang terstruktur "
        "(PMBOK® Guide 6th Edition, PMI, 2017). Manajemen komunikasi tidak hanya berfokus pada pengiriman pesan semata, melainkan menjamin "
        "keseluruhan siklus hidup informasi—mulai dari perencanaan (planning), pengumpulan (collecting), pembuatan (creating), pendistribusian (distributing), "
        "penyimpanan (storing), penemuan kembali (retrieving), pengelolaan (managing), hingga disposisi akhir (disposition) informasi proyek.")
    
    add_body_p(doc,
        "Urgensi area pengetahuan manajemen komunikasi terhadap keberhasilan proyek didasari oleh faktor-faktor kritis berikut:")
    add_num_p(doc, "Proporsi Aktivitas Manajer Proyek (The 90% Rule): Berbagai literatur standar industri (PMI, 2017; Larson & Gray, 2021) menegaskan bahwa seorang Manajer Proyek menghabiskan sekitar 90% dari total waktu kerjanya untuk berkomunikasi—baik dengan tim teknis, sponsor, klien, maupun pemangku kepentingan eksternal. Komunikasi merupakan instrumen utama kepemimpinan untuk mengarahkan, memotivasi, dan menyelaraskan seluruh elemen proyek.", 1)
    add_num_p(doc, "Penyebab Utama Kegagalan Proyek: Berdasarkan riset empiris PMI dalam laporan Pulse of the Profession, komunikasi yang tidak efektif merupakan kontributor utama dari 56% proyek yang gagal memenuhi sasaran ruang lingkup, jadwal, atau anggaran. Kegagalan komunikasi memicu kesalahpahaman kebutuhan, pengerjaan ulang (rework), konflik interpersonal, dan hilangnya kepercayaan pemangku kepentingan.", 2)
    add_num_p(doc, "Jembatan Antara Ranah Teknis dan Strategis (Konteks Proyek PRE-02): Dalam proyek rekayasa perangkat lunak berbasis Machine Learning seperti PRE-02 (Sistem Prediksi Probabilitas Keterlambatan Proyek), komunikasi bertindak sebagai penerjemah kritis antara kompleksitas matematis data science (misal: kalibrasi probabilitas Brier Score, ECE, kurva ROC) dengan kebutuhan praktis Manajer Proyek yang membutuhkan insight risiko keterlambatan yang lugas dan dapat ditindaklanjuti (actionable early warning).", 3)

    # =========================================================================
    # SOAL 2
    # =========================================================================
    add_heading_2(doc, "2. Sebutkan dan jelaskan tiga proses dalam manajemen komunikasi proyek!")
    add_body_p(doc,
        "Berdasarkan standar PMBOK® Guide 6th Edition (PMI, 2017, hal. 359–393), manajemen komunikasi proyek terdiri dari tiga proses "
        "utama yang terintegrasi secara siklis di sepanjang tahapan proyek:")

    headers_q2 = ["Nama Proses", "Kelompok Proses (Process Group)", "Definisi, Tujuan, dan Mekanisme Kerja", "Output Utama"]
    data_q2 = [
        [
            "1. Plan Communications Management\n(Merencanakan Manajemen Komunikasi)",
            "Planning\n(Perencanaan)",
            "Proses mengembangkan pendekatan dan rencana yang tepat untuk aktivitas komunikasi proyek berdasarkan kebutuhan informasi masing-masing pemangku kepentingan atau kelompok, aset proses organisasi yang tersedia, dan kebutuhan proyek. Proses ini menentukan siapa yang membutuhkan informasi apa, kapan informasi tersebut dibutuhkan, format penyajian, serta saluran yang digunakan.",
            "• Communications Management Plan\n• Pembaruan Project Management Plan\n• Pembaruan Project Documents"
        ],
        [
            "2. Manage Communications\n(Mengelola Komunikasi)",
            "Executing\n(Pelaksanaan)",
            "Proses memastikan pengumpulan, pembuatan, pendistribusian, penyimpanan, pengambilan, pengelolaan, pemantauan, dan disposisi akhir informasi proyek yang tepat waktu dan sesuai dengan rencana komunikasi. Proses ini mengeksekusi rencana komunikasi, memfasilitasi arus informasi yang efektif antar-tim, merespons permintaan informasi ad-hoc, dan memastikan pemahaman pesan secara utuh.",
            "• Project Communications (laporan status, presentasi, memo)\n• Pembaruan Project Management Plan\n• Pembaruan Project Documents\n• Pembaruan Organizational Process Assets"
        ],
        [
            "3. Monitor Communications\n(Memantau Komunikasi)",
            "Monitoring & Controlling\n(Pemantauan & Pengendalian)",
            "Proses memastikan bahwa kebutuhan informasi proyek dan para pemangku kepentingannya terpenuhi secara optimal sepanjang siklus hidup proyek. Proses ini mengevaluasi efektivitas pesan dan media yang digunakan, mengidentifikasi kesenjangan atau hambatan komunikasi, serta melakukan penyesuaian strategi komunikasi secara berkelanjutan.",
            "• Work Performance Information\n• Change Requests (permintaan perubahan rencana komunikasi)\n• Pembaruan Project Management Plan\n• Pembaruan Project Documents"
        ]
    ]
    create_table(doc, headers_q2, data_q2)

    # =========================================================================
    # SOAL 3
    # =========================================================================
    add_heading_2(doc, "3. Jelaskan apa yang dimaksud dengan Communications Management Plan! Sebutkan minimal delapan komponen yang harus ada dalam rencana tersebut!")
    add_body_p(doc,
        "Communications Management Plan (Rencana Manajemen Komunikasi) adalah dokumen komponen dari rencana manajemen proyek (Project Management Plan) "
        "yang mendeskripsikan secara komprehensif bagaimana, kapan, dan oleh siapa informasi proyek akan dikelola, distrukturkan, "
        "dipantau, dan disebarluaskan (PMI, 2017). Dokumen ini berfungsi sebagai peta jalan formal komunikasi yang memastikan seluruh pemangku kepentingan "
        "menerima informasi yang relevan pada waktu yang tepat melalui media yang paling efisien, sekaligus menghindari kelebihan beban informasi (information overload).")
    
    add_body_p(doc,
        "Komponen-komponen penting yang wajib dimuat dalam Communications Management Plan mencakup minimal delapan elemen berikut (diuraikan sepuluh komponen standar industri):")
    
    add_num_p(doc, "Kebutuhan Komunikasi Pemangku Kepentingan (Stakeholder Communication Requirements): Identifikasi kebutuhan informasi spesifik dari setiap pemangku kepentingan berdasarkan analisis kekuasaan, kepentingan, dan dampak mereka terhadap proyek.", 1)
    add_num_p(doc, "Informasi yang Dikomunikasikan (Information to be Communicated): Rincian konten informasi yang akan didistribusikan, termasuk bahasa penyampaian, format laporan, tingkat kedalaman (level of detail), dan struktur data.", 2)
    add_num_p(doc, "Alasan Distribusi Informasi (Reason/Purpose for Distribution): Justifikasi mengapa informasi tersebut perlu disebarkan kepada audiens tertentu (misalnya: untuk persetujuan anggaran, kesadaran risiko, atau pemantauan kemajuan teknis).", 3)
    add_num_p(doc, "Jangka Waktu dan Frekuensi Distribusi (Timeframe and Frequency): Jadwal dan ritme penyampaian informasi, seperti laporan harian (daily standup), ringkasan kemajuan mingguan, laporan status bulanan, atau pelaporan berbasis pencapaian milestone.", 4)
    add_num_p(doc, "Pihak Penanggung Jawab Penyampaian (Sender / Responsible Person): Individu atau peran yang bertanggung jawab menyusun, memverifikasi, dan mengirimkan informasi (misalnya: Project Manager, Technical Lead, atau Data Science Lead).", 5)
    add_num_p(doc, "Pihak Penerima Informasi (Target Audience / Recipients): Daftar pemangku kepentingan, kelompok, atau individu yang menjadi target penerima informasi resmi.", 6)
    add_num_p(doc, "Metode dan Teknologi Saluran Komunikasi (Methods and Technologies): Saluran atau media yang digunakan untuk mendistribusikan informasi (misalnya: email resmi, repositori GitHub, rapat tatap muka/telekonferensi, dashboard proyek, atau aplikasi pesan instan).", 7)
    add_num_p(doc, "Alokasi Sumber Daya untuk Komunikasi (Resources Allocated): Sumber daya finansial, lisensi perangkat lunak kolaborasi (Slack, Jira, Zoom), dan alokasi jam kerja tim yang dicadangkan khusus untuk kegiatan komunikasi proyek.", 8)
    add_num_p(doc, "Proses Eskalasi Isu (Escalation Process): Alur hierarkis dan batas waktu (timeframe) untuk menaikkan isu-isu kritis yang tidak dapat diselesaikan pada level operasional tim kepada level manajemen yang lebih tinggi.", 9)
    add_num_p(doc, "Glosarium Terminologi Umum (Glossary of Common Terminology): Kamus istilah teknis, akronim, dan definisi standar proyek guna mencegah ambiguitas semantik dan miskomunikasi antar-pemangku kepentingan multidisiplin.", 10)

    # =========================================================================
    # SOAL 4
    # =========================================================================
    add_heading_2(doc, "4. Sebutkan dan jelaskan tiga metode komunikasi (interaktif, push, pull)! Berikan contoh penggunaan masing-masing metode dalam proyek!")
    add_body_p(doc,
        "Dalam standar PMBOK® Guide (PMI, 2017, hal. 374), metode komunikasi diklasifikasikan ke dalam tiga kategori utama "
        "berdasarkan mekanisme aliran informasi dan tingkat interaksi partisipan:")

    headers_q4 = ["Metode Komunikasi", "Definisi & Mekanisme Aliran Pesan", "Karakteristik & Kelebihan", "Keterbatasan Utama", "Contoh Penerapan Nyata dalam Proyek (PRE-02)"]
    data_q4 = [
        [
            "1. Interactive Communication\n(Komunikasi Interaktif)",
            "Komunikasi multidireksional (dua arah atau lebih) yang berlangsung secara waktu-nyata (synchronous) antara dua atau lebih pihak yang bertukar informasi.",
            "• Umpan balik (feedback) seketika\n• Memungkinkan klarifikasi langsung\n• Paling efektif untuk pemecahan masalah kompleks, negosiasi, dan konsensus",
            "• Memerlukan sinkronisasi waktu partisipan\n• Menghabiskan waktu jika tidak dikelola dengan agenda ketat",
            "• Rapat koordinasi mingguan (Sprint Review) tim PRE-02\n• Sesi pembahasan trade-off model machine learning antara Lead Data Scientist dan Backend Engineer\n• Rapat telekonferensi klarifikasi kebutuhan dengan Dosen Pengampu"
        ],
        [
            "2. Push Communication\n(Komunikasi Dorong / Searah)",
            "Informasi dikirimkan atau didistribusikan secara langsung kepada penerima tertentu yang berhak tanpa menjamin adanya penerimaan atau pemahaman seketika.",
            "• Menjangkau banyak penerima secara cepat\n• Menjamin pengiriman informasi spesifik ke target\n• Menciptakan rekam jejak tertulis formal",
            "• Tidak menjamin bahwa pesan telah dibaca, dipahami, atau ditindaklanjuti oleh penerima\n• Risiko memicu kelebihan email (inbox overload)",
            "• Pengiriman laporan status kemajuan proyek mingguan via email resmi kepada Dosen Pengampu\n• Pengiriman memo perubahan baseline jadwal\n• Notifikasi bot otomatis di Discord/Slack saat pipeline pelatihan model selesai dijalankan"
        ],
        [
            "3. Pull Communication\n(Komunikasi Tarik / Mandiri)",
            "Informasi disediakan dan disimpan pada repositori atau sistem terpusat, di mana para pemangku kepentingan mengakses dan mengambil informasi tersebut secara mandiri (on-demand) sesuai kebutuhan.",
            "• Sangat efisien untuk volume informasi besar atau audiens luas\n• Penerima mengakses informasi kapan saja tanpa mengganggu pengirim\n• Menghemat bandwidth komunikasi tim",
            "• Membutuhkan inisiatif dan disiplin dari penerima untuk mengakses data\n• Memerlukan pemeliharaan repositori yang teratur agar tetap mutakhir",
            "• Repositori kode sumber GitHub/GitLab untuk kode pelatihan model PRE-02\n• Dashboard metrik evaluasi model (MLflow / Weights & Biases) untuk memantau AUC-ROC dan Brier Score\n• Portal Google Drive / Notion untuk arsip dokumen KAK, SRS, dan LKM"
        ]
    ]
    create_table(doc, headers_q4, data_q4)

    # =========================================================================
    # SOAL 5
    # =========================================================================
    add_heading_2(doc, "5. Mengapa model pengirim-penerima (sender-receiver model) dengan umpan balik penting dalam komunikasi proyek? Jelaskan!")
    add_body_p(doc,
        "Model Pengirim-Penerima (Sender-Receiver Model)—yang berakar dari teori komunikasi matematis Claude Shannon dan Warren Weaver (1949) "
        "serta diadaptasi dalam standar PMBOK® Guide (PMI, 2017)—menggambarkan proses komunikasi linier yang disempurnakan menjadi siklus dinamis "
        "melalui sembilan elemen kunci:")
    
    add_bullet_p(doc, "Pengirim (Sender): Pihak yang menginisiasi pesan dengan menerjemahkan ide atau gagasan menjadi simbol/kode (Encoding).")
    add_bullet_p(doc, "Pesan (Message): Output berwujud dari proses pengkodean (ide, data teknis, instruksi, dokumen).")
    add_bullet_p(doc, "Media/Saluran (Channel/Medium): Jalur fisik atau digital yang digunakan untuk mentransmisikan pesan (email, suara, visual).")
    add_bullet_p(doc, "Hambatan/Gangguan (Noise): Segala faktor yang mendistorsi kejelasan pesan, seperti hambatan semantik, bias emosional, perbedaan latar belakang budaya, atau gangguan jaringan.")
    add_bullet_p(doc, "Penerima (Receiver): Pihak yang menerima pesan dan menerjemahkan simbol-simbol tersebut menjadi pemahaman bermakna (Decoding).")
    add_bullet_p(doc, "Konfirmasi Penerimaan (Acknowledgment): Tanda bahwa pesan fisik telah sampai ke penerima, namun belum tentu dipahami.")
    add_bullet_p(doc, "Umpan Balik (Feedback): Respons verbal atau tertulis dari penerima yang mengindikasikan apakah pesan telah dipahami dengan benar sesuai maksud awal pengirim.")

    add_body_p(doc,
        "Keberadaan elemen umpan balik (feedback loop) sangat krusial dalam komunikasi proyek karena alasan-alasan fundamental berikut:")
    add_num_p(doc, "Mencegah Ilusi Komunikasi (Eliminating Illusion of Communication): George Bernard Shaw pernah menyatakan bahwa \"Masalah terbesar dalam komunikasi adalah ilusi bahwa komunikasi telah terjadi.\" Tanpa umpan balik, pengirim mengasumsikan penerima telah memahami instruksi persis seperti apa yang dimaksudkan. Umpan balik memvalidasi keselarasan pemahaman mental antara kedua belah pihak.", 1)
    add_num_p(doc, "Mendeteksi dan Mengoreksi Distorsi (Noise Correction): Dalam lingkungan proyek teknologi informasi yang sarat terminologi rumit, noise semantik sangat tinggi. Melalui umpan balik (seperti parafrase atau konfirmasi spesifikasi), pengirim dapat segera mendeteksi jika terjadi misinterpretasi dan mengoreksinya sebelum dieksekusi menjadi kode program yang salah.", 2)
    add_num_p(doc, "Menutup Siklus Akuntabilitas (Closing the Loop): Umpan balik mengubah komunikasi satu arah yang pasif menjadi dialog kolaboratif yang akuntabel. Hal ini memastikan penerima siap mengemban tanggung jawab atas deliverables yang ditugaskan.", 3)
    add_num_p(doc, "Relevansi Kritis pada Proyek PRE-02: Ketika Data Scientist mengomunikasikan ambang batas peringatan dini keterlambatan (misal: probabilitas >= 0.65 memicu status Bahaya), tim antarmuka (UI/UX) dan backend harus memberikan umpan balik berupa prototipe respons API. Umpan balik ini memastikan bahwa parameter numerik model diinterpretasikan secara seragam di seluruh subsistem.", 4)

    # =========================================================================
    # SOAL 6
    # =========================================================================
    add_heading_2(doc, "6. Sebutkan dan jelaskan lima langkah komunikasi efektif menurut PMI (Listen Intently, Think Clearly, Discuss Openly, Develop Sensitivity, Respond Quickly to Needs)!")
    add_body_p(doc,
        "Untuk mentransformasikan model komunikasi teoritis ke dalam praktik manajemen proyek yang berdampak tinggi, "
        "PMI merumuskan lima langkah terstruktur untuk mencapai komunikasi yang efektif:")

    add_num_p(doc, "Listen Intently (Mendengarkan dengan Sungguh-Sungguh dan Penuh Perhatian): Langkah ini menuntut keterlibatan active listening (mendengarkan secara aktif). Manajer proyek dan anggota tim harus menyingkirkan gangguan eksternal (gadget, multitasking), menghentikan dorongan untuk menyela, serta menyimak tidak hanya kata-kata yang diucapkan tetapi juga nada suara dan bahasa tubuh pembicara guna menangkap makna tersirat dan kekhawatiran yang mendasari.", 1)
    add_num_p(doc, "Think Clearly (Berpikir Jernih Sebelum Merespons): Menahan diri dari reaksi spontan yang reaktif atau emosional. Langkah ini melibatkan proses sintesis informasi: memverifikasi fakta, memisahkan asumsi dari bukti objektif, menganalisis dampak terhadap tujuan proyek, dan menyusun kerangka respons yang logis, terstruktur, serta berorientasi pada pemecahan masalah.", 2)
    add_num_p(doc, "Discuss Openly (Mendiskusikan Masalah Secara Terbuka dan Transparan): Membangun lingkungan dialog yang jujur tanpa rasa takut terhadap konsekuensi negatif (psychological safety). Isu teknis, keterlambatan jadwal, atau keterbatasan kapasitas tim harus diungkapkan secara transparan di atas meja agar dapat dipecahkan bersama, bukan disembunyikan demi menjaga reputasi semu.", 3)
    add_num_p(doc, "Develop Sensitivity (Mengembangkan Kepekaan Empatik dan Interpersonal): Memahami bahwa setiap anggota tim dan pemangku kepentingan memiliki latar belakang kognitif, keahlian, budaya kerja, dan tingkat tekanan yang berbeda. Kepekaan ini memungkinkan komunikator untuk menyesuaikan gaya bahasa, nada bicara, dan pilihan media agar pesan dapat diterima tanpa menimbulkan resistensi emosional atau ketersinggungan.", 4)
    add_num_p(doc, "Respond Quickly to Needs (Merespons Kebutuhan Informasi Secara Cepat dan Akuntabel): Menjaga ritme dan ketepatan waktu dalam memberikan jawaban, klarifikasi, atau data yang dibutuhkan oleh pemangku kepentingan. Penundaan respons menciptakan ketidakpastian (bottleneck) dan merusak kepercayaan timbal balik, sedangkan respons cepat memperlancar alur kerja operasional proyek.", 5)

    # =========================================================================
    # SOAL 7
    # =========================================================================
    add_heading_2(doc, "7. Menurut Anda, mengapa komunikasi yang efektif dalam tim proyek sering menjadi tantangan terbesar dibandingkan dengan aspek teknis proyek?")
    add_body_p(doc,
        "Dalam lanskap rekayasa perangkat lunak dan manajemen proyek teknologi informasi, paradoks yang sering dihadapi adalah bahwa "
        "kegagalan proyek lebih sering dipicu oleh faktor manusia (human factors) daripada kelemahan algoritma teknis. Komunikasi yang efektif "
        "menjadi tantangan terbesar karena faktor-faktor analitis berikut:")

    add_num_p(doc, "Deterministik Teknis vs Dinamika Psikososial: Masalah teknis (coding bug, konfigurasi server, optimasi hyperparameter) bersifat deterministik dan matematis—aturan sintaksisnya pasti, logikanya biner (benar/salah), dan dapat didebug menggunakan metode ilmiah yang terukur. Sebaliknya, komunikasi melibatkan psikologi manusia yang probabilistik, sarat emosi, rentan bias kognitif, dan dipengaruhi oleh persepsi subjektif yang tidak dapat diselesaikan hanya dengan rumus matematika.", 1)
    add_num_p(doc, "Perbedaan Paradigma Disiplin Ilmu (Silo Mentality): Tim proyek TI modern terdiri dari peran-peran dengan latar belakang kognitif yang sangat kontras. Data Scientist berpikir dalam kerangka probabilitas, inferensi statistik, dan ketidakpastian model; Software Engineer berpikir dalam logika arsitektur modular, determinisme sistem, dan efisiensi waktu eksekusi; sementara Project Manager dan Klien berpikir dalam matriks bisnis, timeline, dan anggaran. Menjembatani jurang epistemologis antar-spesialisasi ini menuntut fleksibilitas komunikasi luar biasa.", 2)
    add_num_p(doc, "Fenomena Keengganan Menyampaikan Berita Buruk (The Mum Effect): Anggota tim sering kali ragu atau takut mengomunikasikan keterlambatan, kegagalan eksperimen model ML, atau hambatan teknis kepada pimpinan karena kekhawatiran akan disalahkan atau dinilai tidak kompeten. Akibatnya, isu-isu kritis terkubur hingga akhirnya meledak menjadi krisis proyek yang tidak terhindarkan.", 3)
    add_num_p(doc, "Asumsi Tersirat (Implicit Assumptions) dan Kutukan Pengetahuan (Curse of Knowledge): Para ahli teknis sering berasumsi bahwa apa yang ada di kepalanya juga dipahami dengan mudah oleh orang lain. Mereka menggunakan akronim dan jargon rumit tanpa menyadari bahwa pemangku kepentingan non-teknis kehilangan pemahaman mendasar, memicu rasa frustrasi di kedua belah pihak.", 4)

    # =========================================================================
    # SOAL 8
    # =========================================================================
    add_heading_2(doc, "8. Sebutkan dan jelaskan strategi praktis untuk meningkatkan komunikasi dalam tim proyek berdasarkan hasil penelitian dan praktik terbaik!")
    add_body_p(doc,
        "Mengacu pada penelitian empiris dinamika tim (Larson & Gray, 2021; Schwalbe, 2019) dan praktik terbaik industri (Agile/PMI), "
        "terdapat enam strategi praktis yang terbukti mampu mendongkrak efektivitas komunikasi tim:")

    add_num_p(doc, "Rapat Sinkronisasi Singkat dan Teratur (Daily Standup / Check-in 10-15 Menit): Menyelenggarakan pertemuan sinkronisasi harian dengan batasan waktu ketat (timeboxing). Setiap anggota menjawab tiga pertanyaan kunci: apa yang telah diselesaikan, apa yang akan dikerjakan, dan hambatan apa yang dihadapi. Pendekatan ini menjaga transparansi harian, mencegah deviasi arah kerja, dan mengidentifikasi bottleneck sejak dini.", 1)
    add_num_p(doc, "Penyusunan Kontrak Tim (Team Charter / Team Contract) Sejak Inisiasi: Menyepakati aturan dasar (ground rules) komunikasi secara tertulis di awal proyek, meliputi: media komunikasi resmi yang disepakati, standar waktu respons pesan (SLA balasan), etika kehadiran dalam rapat, serta tata cara eskalasi dan resolusi perbedaan pendapat.", 2)
    add_num_p(doc, "Membangun Tata Kelola Mandiri (Self-Regulating Governance Melalui Peer Accountability): Mendorong budaya di mana anggota tim merasa bertanggung jawab langsung kepada rekan kerjanya, bukan sekadar kepada Manajer Proyek. Komunikasi yang intensif dan transparan menciptakan norma akuntabilitas sejawat, sehingga tim dapat saling mengoreksi secara mandiri tanpa memerlukan pengawasan mikromanajemen.", 3)
    add_num_p(doc, "Pemanfaatan Information Radiators (Visual Management): Menggunakan papan kanban digital (Trello, Jira, GitHub Projects) dan dashboard kemajuan yang dapat diakses publik oleh seluruh anggota tim. Informasi visual ini memancarkan status pekerjaan secara real-time (work-in-progress, backlog, selesai), sehingga mengurangi kebutuhan rapat status yang berulang-ulang.", 4)
    add_num_p(doc, "Pemisahan Saluran Komunikasi Formal vs Informal Secara Proporsional: Menentukan batas fungsional antara saluran formal (repositori Git, laporan kemajuan mingguan, email resmi) untuk dokumentasi audit dan keputusan strategis, serta saluran informal (grup WhatsApp, channel Discord) untuk koordinasi taktis cepat, diskusi santai, dan penguatan ikatan interpersonal tim.", 5)
    add_num_p(doc, "Membudayakan Keselamatan Psikologis (Psychological Safety): Diteliti oleh Amy Edmondson (Harvard) dan Project Aristotle (Google), iklim keselamatan psikologis menjamin bahwa anggota tim merasa aman untuk mengambil risiko interpersonal, mengakui kekeliruan kode/eksperimen data, bertanya tanpa takut dihakimi, dan menyuarakan ide inovatif secara terbuka.", 6)
