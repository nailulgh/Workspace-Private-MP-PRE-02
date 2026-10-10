# -*- coding: utf-8 -*-
"""
Section A Builder: Tugas Tertulis Individu
Pertemuan 9: Manajemen Sumber Daya Proyek
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
    add_heading_2(doc, "1. Apa yang dimaksud dengan manajemen sumber daya proyek dan mengapa area pengetahuan ini penting dalam keberhasilan proyek?")
    add_body_p(doc,
        "Manajemen Sumber Daya Proyek (Project Resource Management) adalah area pengetahuan manajemen proyek yang mencakup proses-proses "
        "untuk mengidentifikasi, memperoleh (mengakuisisi), mengalokasikan, mengelola, dan mengendalikan sumber daya yang diperlukan "
        "agar proyek dapat diselesaikan secara sukses (PMBOK® Guide 6th Edition, PMI, 2017). "
        "Dalam pemutakhiran standar PMBOK edisi ke-6, cakupan area pengetahuan ini diperluas dari yang sebelumnya hanya berfokus pada "
        "sumber daya manusia (Human Resource Management) menjadi mencakup dua kategori sumber daya komprehensif:")
    add_bullet_p(doc, "Sumber Daya Manusia (Human Resources / Project Team): Personel tim kerja dengan keahlian teknis, kepemimpinan, dan kompetensi spesifik yang ditugaskan menjalankan aktivitas proyek.")
    add_bullet_p(doc, "Sumber Daya Fisik (Physical Resources): Aset material, fasilitas laboratorium/kantor, peralatan komputasi, perangkat keras, lisensi perangkat lunak, dan infrastruktur cloud pendukung.")
    
    add_body_p(doc,
        "Urgensi area pengetahuan ini terhadap keberhasilan proyek didasari oleh tiga faktor kunci:")
    add_num_p(doc, "Manusia Sebagai Penggerak Utama Deliverables: Rencana proyek, algoritma, dan jadwal yang paling canggih sekalipun tidak memiliki arti tanpa eksekusi oleh manusia. Produktivitas, motivasi, kohesi tim, dan kejelasan peran menjadi penentu langsung tercapainya sasaran proyek.", 1)
    add_num_p(doc, "Optimalisasi Alokasi dan Pencegahan Bottleneck: Keterbatasan sumber daya (resource constraints)—seperti keterbatasan komputasi GPU atau kelangkaan tenaga Data Scientist spesialis—dapat melumpuhkan proyek jika tidak dikelola melalui perataan beban (resource leveling) dan estimasi kapasitas yang akurat.", 2)
    add_num_p(doc, "Mitigasi Konflik dan Stres Tim (Konteks Proyek PRE-02): Dalam riset sistem peringatan dini machine learning PRE-02 yang memadukan keahlian Data Science, Machine Learning Engineering, Backend, dan UI/UX, kolaborasi lintas-fungsi rentan memicu friksi peran. Manajemen sumber daya yang efektif menjamin pembagian beban kerja berimbang sehingga mencegah burnout dan pergantian anggota tim (turnover).", 3)

    # =========================================================================
    # SOAL 2
    # =========================================================================
    add_heading_2(doc, "2. Sebutkan dan jelaskan enam proses dalam manajemen sumber daya proyek!")
    add_body_p(doc,
        "Berdasarkan kerangka PMBOK® Guide 6th Edition (PMI, 2017, hal. 307–357), manajemen sumber daya proyek terdiri dari enam proses "
        "terstruktur yang berkesinambungan:")
    
    add_num_p(doc, "Plan Resource Management (Merencanakan Manajemen Sumber Daya): Proses mendefinisikan bagaimana sumber daya fisik dan sumber daya tim akan diestimasi, diperoleh, dikelola, dan dimanfaatkan sepanjang proyek. Menghasilkan Resource Management Plan dan Team Charter.", 1)
    add_num_p(doc, "Estimate Activity Resources (Mengestimasi Sumber Daya Aktivitas): Proses memperkirakan jenis, kuantitas, karakteristik, dan profil kualifikasi personel, material, serta peralatan yang dibutuhkan untuk menuntaskan setiap aktivitas pekerjaan pada WBS.", 2)
    add_num_p(doc, "Acquire Resources (Mengakuisisi Sumber Daya): Proses mendapatkan staf tim proyek yang kompeten, fasilitas kerja, peralatan komputasi, perlengkapan, dan material yang dibutuhkan melalui negosiasi internal (dengan manajer fungsional) maupun pengadaan eksternal.", 3)
    add_num_p(doc, "Develop Team (Mengembangkan Tim): Proses meningkatkan kompetensi anggota tim, memfasilitasi interaksi sosial yang harmonis, serta membangun lingkungan kerja yang kondusif guna mendongkrak kinerja tim secara keseluruhan (fokus pada motivasi, pelatihan, dan team building).", 4)
    add_num_p(doc, "Manage Team (Mengelola Tim): Proses melacak kinerja individual anggota tim, memberikan umpan balik (feedback), menyelesaikan konflik interpersonal, serta mengelola perubahan penugasan personel untuk mengoptimalkan efektivitas kerja proyek.", 5)
    add_num_p(doc, "Control Resources (Mengendalikan Sumber Daya): Proses memastikan bahwa sumber daya fisik (infrastruktur server, alat, material) dialokasikan dan tersedia sesuai rencana, memantau utilisasi aktual terhadap baseline, serta mengeksekusi tindakan korektif jika terjadi deviasi ketersediaan.", 6)

    # =========================================================================
    # SOAL 3
    # =========================================================================
    add_heading_2(doc, "3. Sebutkan dan jelaskan lima tahap dalam Tuckman Model beserta ciri-ciri perilaku tim pada setiap tahap!")
    add_body_p(doc,
        "Tuckman Model (Bruce Tuckman, 1965; disempurnakan bersama Jensen, 1977) adalah kerangka perkembangan kelompok "
        "yang menggambarkan dinamika psikologis dan evolusi kinerja tim proyek melalui lima tahapan progresif:")

    headers_q3 = ["Tahap Perkembangan", "Karakteristik & Dinamika Kelompok", "Ciri-Ciri Perilaku Tim yang Teramati", "Peran/Gaya Manajer Proyek"]
    data_q3 = [
        ["1. Forming\n(Tahap Pembentukan)", "Tahap orientasi awal di mana anggota baru berkumpul, masih saling mengamati, menjaga jarak aman, dan berusaha menciptakan impresi positif.", "Anggota bersikap sangat sopan, formal, enggan berdebat, minim inisiatif mandiri, dan sangat bergantung pada instruksi langsung pimpinan proyek.", "Direktif (Directing): Menjelaskan visi, tujuan proyek, aturan dasar (ground rules), dan batas tanggung jawab."],
        ["2. Storming\n(Tahap Badai / Konflik)", "Tahap friksi di mana anggota mulai menyuarakan opini pribadi, mempertanyakan otoritas, berebut pengaruh, dan berselisih tentang metodologi kerja.", "Muncul perdebatan sengit, polarisasi kelompok, resistensi terhadap pembagian tugas, friksi interpersonal, dan penurunan sementara moral tim.", "Pelatih/Fasilitator (Coaching): Menengahi konflik, mengklarifikasi ekspektasi, membangun empati, dan menjaga fokus objektif."],
        ["3. Norming\n(Tahap Pembentukan Norma)", "Tahap rekonsiliasi di mana tim mulai menerima perbedaan, menyepakati konsensus metode kerja, dan membangun kohesi sosial yang solid.", "Tercipta rasa saling percaya, norma kerja (Team Charter) dihormati, komunikasi terbuka, saling membantu, dan lahirnya identitas tim (\"we\" mindset).", "Partisipatif (Supporting): Memfasilitasi kolaborasi, mendelegasikan wewenang moderat, dan memperkuat budaya apresiasi."],
        ["4. Performing\n(Tahap Berkinerja Optimal)", "Puncak kematangan tim di mana kelompok bertransformasi menjadi unit yang otonom, fleksibel, terkoordinasi secara mulus, dan sangat produktif.", "Pekerjaan diselesaikan dengan efisiensi tinggi, anggota mampu menyelesaikan konflik secara mandiri, berfokus pada solusi, dan inovasi berkembang.", "Delegatif (Delegating): Memberikan otonomi penuh, memantau kemajuan dari tingkat strategis, dan menghilangkan hambatan eksternal."],
        ["5. Adjourning\n(Tahap Pembubaran)", "Tahap penutupan proyek di mana seluruh deliverables telah selesai diserahkan dan tim dibubarkan secara administratif.", "Campuran rasa bangga atas pencapaian tujuan dan kecemasan menghadapi ketidakpastian penugasan berikutnya; dokumentasi pelajaran yang dipetik.", "Apresiatif (Celebrating): Mengakui kontribusi anggota tim, merayakan keberhasilan, dan memfasilitasi transisi pelepasan sumber daya."],
    ]
    create_table(doc, headers_q3, data_q3)

    # =========================================================================
    # SOAL 4
    # =========================================================================
    add_heading_2(doc, "4. Menurut Anda, mengapa tahap Storming sering dianggap sebagai tahap yang paling kritis dalam pembentukan tim? Jelaskan!")
    add_body_p(doc,
        "Tahap Storming dianggap sebagai titik paling kritis (make-or-break phase) dalam siklus hidup tim proyek karena "
        "tahap ini merupakan pengujian fundamental pertama terhadap ketahanan organisasi dan kedewasaan emosional para anggotanya. "
        "Urgensi kritis tahap Storming dapat dibedah melalui beberapa dimensi:")
    add_bullet_p(doc, "Ujian Eksistensial Tim (Destructive vs Productive Turning Point): Jika konflik pada tahap ini tidak dikelola secara profesional, tim dapat terjebak dalam disfungsi permanen, apatisme, perpecahan menjadi kubu-kubu saling bermusuhan (cliques), atau bahkan pembubaran tim sebelum menghasilkan produk apa pun.")
    add_bullet_p(doc, "Katalisator Kedewasaan dan Standar Kerja Sejati: Sikap sopan semu pada tahap Forming harus 'dihancurkan' agar asumsi-asumsi tersembunyi, perbedaan standar teknis, dan ketidakpuasan dapat muncul ke permukaan secara jujur. Hanya melalui konfrontasi gagasan yang terbuka pada tahap Storming-lah norma kerja yang autentik, kokoh, dan disepakati bersama (Norming) dapat lahir.")
    add_bullet_p(doc, "Penetapan Struktur Kekuasaan dan Kepercayaan: Pada fase inilah batas-batas kompetensi diuji. Anggota tim belajar menghormati keahlian spesifik rekannya—misalnya pada PRE-02, developer web mulai menghargai kerumitan tuning hyperparameter oleh tim Data Science, dan sebaliknya tim Data Science memahami keketatan latency API dari tim Backend.")

    # =========================================================================
    # SOAL 5
    # =========================================================================
    add_heading_2(doc, "5. Apa yang dimaksud dengan Responsibility Assignment Matrix (RAM) dan RACI Chart? Jelaskan perbedaan dan fungsi masing-masing!")
    add_body_p(doc,
        "Responsibility Assignment Matrix (RAM) adalah instrumen grafis berbentuk matriks tabel yang memetakan keterkaitan "
        "antara struktur pembagian pekerjaan proyek (Work Breakdown Structure / WBS) dengan struktur pengorganisasian tim kerja "
        "(Organizational Breakdown Structure / OBS). Tujuannya adalah memastikan bahwa setiap paket kerja atau aktivitas proyek "
        "secara eksplisit dialokasikan ke personel atau unit penanggung jawab tertentu tanpa ada bagian pekerjaan yang terlupakan (PMI, 2017).")
    
    add_body_p(doc,
        "Hubungan dan Perbedaan Antara RAM dan RACI Chart:")
    add_bullet_p(doc, "RAM adalah Konsep Payung (Umum): RAM merupakan kategori umum dari matriks penugasan. RAM tingkat tinggi (high-level RAM) dapat memetakan kelompok kerja WBS level atas ke departemen internal, sedangkan RAM tingkat rendah (low-level RAM) memetakan aktivitas spesifik ke individu.")
    add_bullet_p(doc, "RACI Chart adalah Format Khusus RAM yang Paling Populer: RACI Chart adalah implementasi paling terkenal dan operasional dari RAM. RACI mendefinisikan secara spesifik derajat keterlibatan setiap pemangku kepentingan menggunakan empat kode peran yang tegas: Responsible (R), Accountable (A), Consulted (C), dan Informed (I).")
    
    add_body_p(doc,
        "Fungsi Manajerial:")
    add_num_p(doc, "Menghilangkan Ambiguitas dan Keraguan Peran: Mencegah situasi di mana suatu tugas penting terabaikan karena semua orang mengira orang lain yang mengerjakannya (bystander effect).", 1)
    add_num_p(doc, "Mencegah Duplikasi dan Tumpang Tindih (Role Conflict): Menghindari dua personel mengerjakan hal yang sama dengan pendekatan yang saling bertentangan.", 2)
    add_num_p(doc, "Menjamin Akuntabilitas Tunggal: Memastikan selalu ada satu 'leher' yang dapat dimintai pertanggungjawaban akhir atas kualitas dan ketepatan waktu deliverables.", 3)

    # =========================================================================
    # SOAL 6
    # =========================================================================
    add_heading_2(doc, "6. Sebutkan dan jelaskan makna dari R, A, C, dan I dalam RACI Chart! Mengapa setiap tugas harus memiliki tepat satu orang yang accountable (A)?")
    add_body_p(doc, "Keempat parameter dalam matriks RACI memiliki definisi yuridis-operasional yang presisi:")
    
    add_bullet_p(doc, "Responsible (R) – Pelaksana Tugas: Pihak atau individu yang secara nyata melakukan pekerjaan (doer) dan menghasilkan deliverables fisik. Suatu tugas dapat memiliki lebih dari satu orang 'R' jika membutuhkan kerja sama tim teknis.")
    add_bullet_p(doc, "Accountable (A) – Penanggung Jawab Akhir / Pengambil Keputusan: Individu yang memegang kepemilikan akhir (ownership) atas penyelesaian tugas secara benar dan menyeluruh. Orang ini memiliki hak veto untuk menyetujui (approve) atau menolak deliverables sebelum diserahkan ke tingkat lebih tinggi.")
    add_bullet_p(doc, "Consulted (C) – Konsultan / Pakar Rujukan: Tenaga ahli atau pemangku kepentingan yang memiliki wawasan kritis dan wajib dimintai masukan sebelum keputusan diambil atau pekerjaan dituntaskan (komunikasi dua arah yang aktif / two-way communication).")
    add_bullet_p(doc, "Informed (I) – Penerima Informasi: Pihak yang perlu selalu diperbarui informasinya mengenai kemajuan, status, atau selesainya suatu deliverable karena pekerjaannya terdampak oleh hasil tugas tersebut (komunikasi satu arah / one-way communication).")

    add_body_p(doc,
        "Alasan Krusial Mengapa Setiap Tugas HARUS Memiliki Tepat Satu Akuntabel (Single Accountability Rule):")
    add_body_p(doc,
        "Prinsip 'If everyone is accountable, then no one is accountable' (Jika semua orang bertanggung jawab, maka tidak ada satu pun yang merasa bertanggung jawab). "
        "Memiliki lebih dari satu orang yang Accountable (A) akan memicu 'Dilusi Akuntabilitas' dan kelumpuhan pengambilan keputusan (decision paralysis). "
        "Ketika terjadi kegagalan atau pembengkakan durasi, pihak-pihak yang sama-sama berstatus 'A' cenderung saling menyalahkan (finger-pointing). "
        "Sebaliknya, jika tidak ada satu pun 'A', tugas tersebut menjadi 'anak yatim' (orphan task) yang kehilangan arah. "
        "Oleh karena itu, aturan emas dalam RACI adalah: Setiap baris aktivitas WAJIB memiliki tepat SATU huruf 'A'.")

    # =========================================================================
    # SOAL 7
    # =========================================================================
    add_heading_2(doc, "7. Sebutkan dan jelaskan tiga jenis konflik dalam tim proyek menurut penelitian University of Texas at El Paso!")
    add_body_p(doc,
        "Berdasarkan riset tipologi konflik organisasi yang dipelopori oleh Karen A. Jehn (1995) dan dielaborasi lebih lanjut "
        "oleh para peneliti manajemen proyek di University of Texas at El Paso (Mohammed & Angell, 2004; Verma, 1998), "
        "konflik dalam tim proyek diklasifikasikan ke dalam tiga dimensi fundamental:")

    headers_q7 = ["Jenis Konflik", "Definisi dan Sifat Konflik", "Penyebab Pemicu Utama", "Dampak Terhadap Kinerja Proyek"]
    data_q7 = [
        ["1. Task Conflict\n(Konflik Tugas / Konten)", "Perselisihan yang berkaitan dengan substansi tugas, konten pekerjaan, perbedaan pandangan teknis, interpretasi data, atau kriteria kelayakan luaran proyek.", "Perbedaan sudut pandang metodologi, standar teknologi (misalnya pemilihan framework ML vs arsitektur API), alokasi fitur prioritas.", "Positif / Produktif (pada tingkat moderat): Mendorong analisis kritis, memicu inovasi, mengidentifikasi kelemahan desain sejak dini, dan memperbaiki kualitas keputusan."],
        ["2. Relationship Conflict\n(Konflik Hubungan / Interpersonal)", "Perselisihan yang berakar pada ketidakcocokan personal, benturan kepribadian (personality clash), friksi ego, rasa tersinggung, kecemburuan, atau ketegangan emosional antar individu.", "Gaya komunikasi yang kasar/meremehkan, prasangka pribadi, perbedaan nilai budaya, rasa saling tidak percaya, dan frustrasi emosional.", "Sangat Destruktif / Negatif: Menguras energi psikologis, menurunkan kepuasan kerja, merusak kerja sama tim, memicu permusuhan terbuka, dan melumpuhkan produktivitas proyek."],
        ["3. Process Conflict\n(Konflik Proses / Logistik)", "Perselisihan mengenai tata kelola logistik eksekusi pekerjaan, mekanisme koordinasi, prosedur pendelegasian tugas, alur kerja, dan siapa yang bertanggung jawab melakukan apa.", "Ketidakjelasan pembagian wewenang, jadwal rapat yang tidak efisien, perebutan sumber daya fisik (misal giliran GPU server), dan SOP yang rancu.", "Negatif (jika berlarut-larut): Membuang waktu koordinasi, memicu perasaan ketidakadilan dalam pembagian beban kerja, dan menyebabkan keterlambatan timeline."],
    ]
    create_table(doc, headers_q7, data_q7)

    # =========================================================================
    # SOAL 8
    # =========================================================================
    add_heading_2(doc, "8. Sebutkan dan jelaskan lima strategi resolusi konflik yang dapat digunakan oleh manajer proyek beserta situasi penerapannya!")
    add_body_p(doc,
        "PMBOK® Guide (PMI, 2017, hal. 348–349) mengadopsi model Thomas-Kilmann Conflict Mode Instrument (TKI) "
        "yang memetakan lima teknik resolusi konflik berdasarkan dimensi ketegasan (assertiveness) dan kerja sama (cooperativeness):")

    headers_q8 = ["Teknik Resolusi Konflik", "Karakteristik & Mekanisme Tindakan", "Situasi yang Paling Tepat untuk Diterapkan", "Hasil Interaksi"]
    data_q8 = [
        ["1. Collaborating / Problem Solving\n(Kolaboratif / Pemecahan Masalah)", "Pendekatan proaktif di mana para pihak duduk bersama, mengeksplorasi perbedaan pandangan secara terbuka, membedah akar masalah, dan merumuskan solusi baru yang memuaskan kepentingan semua pihak.", "Isu sangat kritis bagi proyek; memerlukan konsensus jangka panjang; menggabungkan wawasan dari berbagai disiplin ilmu berbeda (misal integrasi model ML ke backend PRE-02).", "Win-Win Solution (Kemenangan Bersama)"],
        ["2. Compromising / Reconcile\n(Kompromi / Jalan Tengah)", "Pendekatan tawar-menawar di mana masing-masing pihak bersedia mengorbankan sebagian tuntutannya untuk mencapai solusi sementara yang dapat diterima bersama.", "Waktu sangat mendesak/deadline mendekat; kedua pihak memiliki kekuatan pengaruh yang seimbang; solusi komprehensif belum memungkinkan.", "Lose-Lose Moderat / Win-Win Parsial"],
        ["3. Forcing / Directing\n(Memaksakan Kehendak / Otoriter)", "Pendekatan direktif menggunakan kekuasaan formal manajer proyek untuk memaksakan suatu keputusan tanpa mempedulikan resistensi pihak yang berlawanan.", "Kondisi darurat krisis yang menuntut aksi instan; menegakkan kebijakan keselamatan/keamanan data yang tidak dapat ditawar; keputusan tidak populer yang vital.", "Win-Lose Solution (Menang-Kalah)"],
        ["4. Smoothing / Accommodating\n(Menghaluskan / Mengalah)", "Menekankan area kesepahaman dan mengecilkan area perbedaan guna memelihara keharmonisan hubungan kerja, bahkan dengan mengalah pada pandangan orang lain.", "Isu yang diperdebatkan jauh lebih penting bagi pihak lain daripada bagi diri sendiri; menjaga kedamaian tim jangka pendek; saat kita menyadari kita di posisi keliru.", "Lose-Win Solution (Mengalah demi Harmoni)"],
        ["5. Withdrawing / Avoiding\n(Menarik Diri / Menghindar)", "Menunda penanganan masalah, mundur dari perdebatan langsung, atau mengabaikan konflik untuk sementara waktu.", "Isu bersifat sepele; emosi kedua pihak sedang memuncak dan membutuhkan waktu untuk mendinginkan kepala (cooling-off); informasi belum lengkap.", "Postponed / No Resolution (Penundaan Solusi)"],
    ]
    create_table(doc, headers_q8, data_q8)

    # =========================================================================
    # SOAL 9
    # =========================================================================
    add_heading_2(doc, "9. Apa perbedaan antara konflik produktif dan konflik destruktif dalam tim proyek? Berikan contoh masing-masing!")
    add_body_p(doc,
        "Perbedaan esensial antara konflik produktif dan destruktif terletak pada fokus perdebatan, dampak emosional, "
        "serta kontribusinya terhadap pencapaian tujuan proyek:")

    headers_q9 = ["Indikator Perbedaan", "Konflik Produktif (Constructive / Functional)", "Konflik Destruktif (Destructive / Dysfunctional)"]
    data_q9 = [
        ["Fokus Perdebatan", "Berpusat pada IDE, DATA, SUBSTANSI TUGAS, dan METODE kerja (Task Conflict).", "Berpusat pada EGO, KEPRIBADIAN, MOTIF PRIBADI, dan MENYERANG INDIVIDU (Relationship Conflict)."],
        ["Iklim Komunikasi", "Debat terbuka, berbasis bukti ilmiah, saling mendengarkan argumen, dan berorientasi solusi.", "Sarkasme, saling menyalahkan (finger-pointing), manipulasi informasi, defensif, dan dendam pribadi."],
        ["Dampak Terhadap Tim", "Meningkatkan kualitas keputusan, memicu inovasi desain, mencegah groupthink, dan memperkuat komitmen.", "Menghancurkan kepercayaan tim, memicu stres, menurunkan moral kerja, membuang waktu, dan memicu penundaan proyek."],
    ]
    create_table(doc, headers_q9, data_q9)

    add_body_p(doc, "Contoh Konkret pada Proyek Perangkat Lunak AI (PRE-02):")
    add_bullet_p(doc, "Contoh Konflik Produktif: Perdebatan teknis antara Data Scientist dan ML Engineer mengenai pemilihan metode kalibrasi probabilitas antara Platt Scaling (Sigmoid) vs Isotonic Regression. Keduanya membawa data empiris Expected Calibration Error (ECE) dan kurva reliabilitas. Debat sengit ini menghasilkan keputusan matang untuk memilih Isotonic Regression karena karakteristik dataset proyek yang besar dan non-parametrik, sehingga kualitas sistem prediksi meningkat drastis.")
    add_bullet_p(doc, "Contoh Konflik Destruktif: Seorang developer Frontend merasa tersinggung dengan gaya berbicara Lead Backend Developer yang dianggap merendahkan saat code review, lalu membalas dengan sengaja menunda pembuatan antarmuka dashboard dan menolak menghadiri sesi stand-up meeting. Akibatnya, integrasi sistem lumpuh selama satu minggu penuh karena permusuhan personal.")
