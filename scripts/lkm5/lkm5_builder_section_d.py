# -*- coding: utf-8 -*-
"""
Section D Builder: Refleksi Mandiri
Pertemuan 5: Manajemen Jadwal Proyek (Bagian I)
Author: Muhammad Nailul Ghufron Majid (240605110160)
Course: Teori Manajemen Proyek - 2026
"""

from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_section_d(doc, helpers):
    add_heading_1 = helpers['add_heading_1']
    add_heading_2 = helpers['add_heading_2']
    add_heading_3 = helpers['add_heading_3']
    add_body_p = helpers['add_body_p']
    add_num_p = helpers['add_num_p']
    add_bullet_p = helpers['add_bullet_p']
    add_subbullet_p = helpers['add_subbullet_p']
    create_table = helpers['create_table']

    add_heading_1(doc, "C. REFLEKSI MANDIRI")
    
    add_body_p(doc,
        "Bagian ini memuat refleksi kritis dan introspeksi personal saya terhadap penguasaan konsep Manajemen Jadwal Proyek (Bagian I) "
        "yang dipelajari pada Pertemuan 5, serta penerapannya secara nyata dalam dinamika kepemimpinan dan eksekusi riset proyek kelompok "
        "berkode PRE-02 (Sistem Prediksi Probabilitas Keterlambatan Proyek Berbasis Machine Learning sebagai Early Warning System Manajemen Proyek).")

    # =========================================================================
    # REFLEKSI 1
    # =========================================================================
    add_heading_2(doc, "1. Menurut pemahaman Anda, mengapa penentuan ketergantungan (dependency) antar aktivitas merupakan langkah yang sangat penting dalam penjadwalan proyek?")
    
    add_body_p(doc,
        "Berdasarkan pemahaman konseptual yang saya telaah dari PMBOK Guide (PMI, 2017) dan Larson & Gray (2021), saya memandang bahwa "
        "penentuan ketergantungan (dependency determination) adalah 'otak logika' yang mengubah daftar pekerjaan statis menjadi sistem "
        "jaringan yang dinamis dan hidup. Sebuah jadwal proyek tidak akan memiliki nilai operasional jika aktivitas-aktivitas di dalamnya "
        "hanya dicantumkan sebagai deretan tanggal tanpa menghubungkan hubungan kausalitas (sebab-akibat) yang mengikatnya.")

    add_body_p(doc,
        "Ada empat alasan fundamental mengapa penentuan ketergantungan menempati posisi yang sangat krusial:")

    add_num_p(doc, "1.", "Menghindari Kesalahan Logika Pelaksanaan (Prevention of Logical Deadlocks):",
        "Dalam rekayasa sistem perangkat lunak, pekerjaan fisik tidak dapat berlangsung secara acak. Ada hukum alam rekayasa (Hard Logic / "
        "Mandatory Dependency) yang tidak dapat dilanggar. Jika seorang manajer proyek gagal mendefinisikan ketergantungan Finish-to-Start "
        "antara pembersihan dataset dengan pelatihan model machine learning, maka tim pengembang akan terjebak dalam eksekusi prematur. "
        "Melatih algoritma pada data mentah yang masih mengandung anomali dan missing values hanya akan membuang waktu komputasi dan menghasilkan "
        "model yang cacat (garbage in, garbage out).")

    add_num_p(doc, "2.", "Fondasi Algoritmik Penentuan Jalur Kritis (Prerequisite for CPM):",
        "Perhitungan lintasan jalur kritis, Early Start, Early Finish, Late Start, Late Finish, dan float secara matematis mustahil dilakukan "
        "tanpa struktur graf jaringan ketergantungan yang valid. Tanpa dependensi yang jelas, perangkat lunak penjadwalan tidak dapat "
        "menghitung aktivitas mana yang mengendalikan tanggal penyelesaian akhir proyek.")

    add_num_p(doc, "3.", "Mencegah Kemacetan Sumber Daya (Resource Bottleneck Mitigation):",
        "Mengetahui relasi ketergantungan memungkinkan kita memetakan kapan suatu keahlian khusus dibutuhkan. Pada proyek PRE-02, peran Data "
        "Engineer dibutuhkan secara intensif pada fase awal ekstraksi data, sedangkan peran Machine Learning Engineer baru dapat bekerja "
        "optimal setelah data bersih diserahkan. Dependensi yang transparan mencegah tenaga ahli menunggu tanpa kepastian (idle time) "
        "atau sebaliknya mengalami beban kerja berlebih (burnout) akibat tumpang tindih tugas yang tak terkontrol.")

    add_num_p(doc, "4.", "Refleksi Riil pada Proyek PRE-02:",
        "Pada riset kami, ketika kami memodelkan ketergantungan antara modul kalibrasi probabilitas (Platt Scaling dan Isotonic Regression) "
        "dengan evaluasi Brier Score, kami menyadari bahwa kalibrasi merupakan simpul penggabungan mutlak (merge node). Kami tidak dapat "
        "mengklaim bahwa model kami berfungsi sebagai Early Warning System yang andal sebelum seluruh probabilitas keluaran model terkalibrasi "
        "dengan frekuensi empiris aktual. Penentuan dependensi yang presisi menyelamatkan kelompok kami dari kesalahan metodologis yang fatal.")

    # =========================================================================
    # REFLEKSI 2
    # =========================================================================
    add_heading_2(doc, "2. Dari berbagai teknik estimasi durasi yang dipelajari (Analogous, Parametric, Three-Point, Bottom-Up), teknik mana yang menurut Anda paling sesuai untuk proyek kelompok Anda, dan mengapa?")
    
    add_body_p(doc,
        "Setelah mengevaluasi keempat teknik estimasi durasi—Analogous, Parametric, Three-Point (PERT), dan Bottom-Up—saya menyimpulkan "
        "bahwa teknik yang **paling sesuai dan paling realistis** untuk proyek kelompok PRE-02 adalah kombinasi sinergis antara "
        "**Three-Point Estimating (PERT)** sebagai teknik utama untuk aktivitas eksperimen komputasi, dipadukan dengan **Bottom-Up Estimating** "
        "untuk aktivitas deliverable pelaporan ilmiah.")

    add_body_p(doc,
        "Alasan mendalam mengapa Three-Point Estimating (PERT) menjadi pilihan paling unggul bagi proyek PRE-02 adalah:")

    add_num_p(doc, "1.", "Tingginya Derajat Ketidakpastian Eksperimen Machine Learning:",
        "Pengembangan model kecerdasan buatan bukanlah proses manufaktur linier yang deterministik. Aktivitas seperti pelatihan arsitektur "
        "Multi-Layer Perceptron (MLP), konvergensi algoritma optimasi Adam, atau penanganan imbalanced class pada portofolio modul ERP FNE "
        "memiliki variabilitas hasil yang sangat tinggi. Estimasi titik tunggal (single-point estimate) hampir pasti akan meleset. Dengan "
        "Three-Point Estimating, tim kami dapat memodelkan ketidakpastian secara probabilistik menggunakan tiga skenario waktu:\n"
        "– Durasi Optimis (t_O): Jika hyperparameter langsung konvergen tanpa kendala overfitting (misal: 3 hari).\n"
        "– Durasi Paling Mungkin (t_M): Waktu normal eksperimen dengan 5-fold cross validation standar (misal: 4 hari).\n"
        "– Durasi Pesimis (t_P): Jika terjadi instabilitas gradien atau data leakage yang menuntut retraining ulang (misal: 8 hari).\n"
        "Dengan formula Beta PERT t_e = (t_O + 4*t_M + t_P)/6, kami memperoleh estimasi durasi terbobot sebesar 4.5 hari yang memiliki "
        "landasan matematika risiko yang kokoh.")

    add_num_p(doc, "2.", "Keterbatasan Data Historis yang Relevan (Kelemahan Analogous & Parametric):",
        "Riset PRE-02 berfokus pada prediksi probabilitas numerik kontinu [0.0 - 1.0] yang terkalibrasi pada multiproyek ERP—sebuah topik "
        "spesifik yang belum memiliki basis data metrik produktivitas historis di lingkungan perkuliahan kami. Oleh karena itu, teknik "
        "Analogous terlalu spekulatif dan dangkal, sedangkan teknik Parametric murni tidak dapat diterapkan karena tidak ada rumus matematis "
        "baku yang menyatakan '100 baris kode machine learning memerlukan X jam kerja'.")

    add_num_p(doc, "3.", "Pelengkap Bottom-Up pada Deliverable Naskah Publikasi:",
        "Untuk aktivitas penulisan paper IMRAD (Bab 1 Pendahuluan, Bab 2 Studi Literatur, Bab 3 Metodologi, Bab 4 Hasil dan Pembahasan, "
        "serta Bab 5 Kesimpulan), kami menerapkan Bottom-Up Estimating. Kami mengestimasi durasi penulisan setiap sub-bab secara terpisah "
        "berdasarkan beban literatur dan analisis tabel hasil, lalu mengagregasikannya menjadi total durasi 5 hari kerja.")

    # =========================================================================
    # REFLEKSI 3
    # =========================================================================
    add_heading_2(doc, "3. Apa tantangan terbesar yang Anda hadapi saat mengidentifikasi aktivitas dan menentukan predecessor untuk proyek kelompok Anda?")
    
    add_body_p(doc,
        "Dalam kapasitas saya sebagai Lead Author dan penanggung jawab paper riset PRE-02, tantangan terbesar yang saya hadapi saat "
        "mengidentifikasi aktivitas dan menentukan urutan predecessor bermuara pada tiga aspek struktural:")

    add_num_p(doc, "1.", "Paradoks Penyelarasan Alur Kerja Iteratif Data Science ke dalam Model Sekuensial Jadwal:",
        "Metodologi riset Machine Learning secara alami bersifat eksploratif dan iteratif (trial-and-error). Sering kali, hasil evaluasi "
        "metrik pada tahap akhir (misal: nilai Brier Score masih di atas target 0.18) menuntut tim untuk kembali ke tahap preprocessing "
        "guna merekayasa ulang fitur (feature re-engineering). Namun, teknik penjadwalan jaringan klasik seperti PDM dan CPM mengasumsikan "
        "alur graf berarah asiklik (Directed Acyclic Graph / DAG) yang bergerak maju searah tanpa perulangan siklus tertutup. Menentukan "
        "titik potong kapan suatu eksperimen dianggap 'selesai' dan membatasi iterasi agar tidak mengacaukan predecessor jadwal merupakan "
        "dilema manajerial terberat yang kami alami.")

    add_num_p(doc, "2.", "Menentukan Tingkat Granularitas Dekomposisi Aktivitas:",
        "Tantangan berikutnya adalah menentukan seberapa dalam paket kerja WBS harus didekomposisi. Jika aktivitas dipecah terlalu mikro "
        "(misal: 'menulis fungsi sigmoid', 'mengimpor library numpy', 'membuat loop training'), jadwal menjadi terlalu birokratis dan "
        "melelahkan untuk diawasi. Sebaliknya, jika dipecah terlalu makro (misal: 'mengerjakan bab Machine Learning = 15 hari'), jadwal "
        "kehilangan fungsinya sebagai alat kendali karena tim tidak dapat melacak progress harian secara objektif. Kami harus berdiskusi "
        "intensif untuk menyepakati level granularitas aktivitas pada rentang durasi 1 hingga 5 hari kerja.")

    add_num_p(doc, "3.", "Ketergantungan Data Multi-Dokumen Portofolio ERP FNE:",
        "Dataset PRE-02 bersumber dari 8 dokumen Project Management Plan (PMP) dan Software Requirements Specification (SRS) modul Super ERP "
        "Farm Nation Enterprise. Masing-masing modul memiliki karakteristik dan tingkat kelengkapan metrik yang berbeda-beda. Menentukan "
        "predecessor ekstraksi data—apakah harus mengekstraksi kedelapan modul sekaligus secara serial atau memproses modul yang telah siap "
        "secara paralel—membutuhkan pemetaan ketergantungan yang cermat agar tidak menimbulkan idle time pada anggota tim data.")

    # =========================================================================
    # REFLEKSI 4
    # =========================================================================
    add_heading_2(doc, "4. Menurut Anda, apa yang terjadi jika estimasi durasi aktivitas terlalu optimis atau terlalu pesimis? Bagaimana dampaknya terhadap keseluruhan proyek?")
    
    add_body_p(doc,
        "Estimasi durasi yang bias—baik yang condong ke arah optimisme berlebihan (over-optimism) maupun pesimisme ekstrem (over-conservatism)—"
        "keduanya membawa dampak destruktif yang sama berbahayanya bagi kesehatan ekosistem proyek:")

    add_heading_3(doc, "A. Dampak Jika Estimasi Terlalu Optimis (Wishful Thinking):")
    add_bullet_p(doc, "Efek Domino Keterlambatan Berantai:",
        "Ketika estimasi durasi ditetapkan terlalu singkat tanpa mempertimbangkan potensi hambatan teknis, keterlambatan pada satu aktivitas "
        "kritis akan langsung memicu efek domino pada seluruh aktivitas penerusnya. Hal ini menghancurkan kredibilitas Schedule Baseline "
        "sejak minggu-minggu pertama proyek.")
    add_bullet_p(doc, "Tekanan Psikologis dan Burnout Tim:",
        "Target tenggat waktu yang tidak realistis memaksa anggota tim bekerja lembur di bawah tekanan stres yang kronis. Dalam rekayasa "
        "perangkat lunak, kelelahan tim pengembang terbukti secara empiris meningkatkan angka kesalahan logika (bug rate) dan menghasilkan "
        "kode program yang rapuh.")
    add_bullet_p(doc, "Pengorbanan Kualitas (Quality Compromise) dan Pengerjaan Ulang (Rework):",
        "Demi mengejar deadline yang mustahil, tim kerap tergoda mengambil jalan pintas (cutting corners)—seperti meniadakan pengujian "
        "validasi silang, mengabaikan kalibrasi probabilitas, atau menulis laporan secara dangkal. Akibatnya, produk perangkat lunak atau "
        "paper ilmiah yang dihasilkan cacat substansi dan ditolak saat review pengujian dosen/klien.")

    add_heading_3(doc, "B. Dampak Jika Estimasi Terlalu Pesimis (Sandbagging / Excessive Buffering):")
    add_bullet_p(doc, "Berlakunya Hukum Parkinson (Parkinson's Law):",
        "Hukum manajemen terkenal menyatakan bahwa 'pekerjaan akan membesar dan meluas untuk memenuhi seluruh waktu yang dialokasikan "
        "bagi penyelesaiannya' (Larson & Gray, 2021). Jika sebuah tugas yang sebenarnya dapat tuntas dalam 2 hari diberi estimasi pesimis "
        "selama 7 hari, tim cenderung memperlambat tempo kerja atau menambahkan kompleksitas yang tidak perlu, sehingga waktu kerja benar-benar "
        "habis dalam 7 hari tanpa adanya peningkatan kualitas yang berarti.")
    add_bullet_p(doc, "Berlakunya Sindrom Mahasiswa (Student Syndrome):",
        "Kelonggaran waktu yang terlalu berlebihan memicu penundaan pengerjaan (prokrastinasi). Tim baru akan mulai serius mengerjakan "
        "tugas pada saat-saat terakhir menjelang batas akhir kalender, sehingga pada akhirnya proyek tetap berada di bawah risiko kepanikan "
        "dan keterlambatan yang sama.")
    add_bullet_p(doc, "Hilangnya Efisiensi Biaya dan Biaya Peluang (Opportunity Cost):",
        "Dalam konteks korporat, durasi proyek yang membengkak secara buatan menahan alokasi anggaran, server cloud, dan sumber daya manusia "
        "berketerampilan tinggi sehingga tidak dapat ditugaskan pada proyek strategis lainnya. Perusahaan kehilangan momentum pasar (time-to-market).")

    # =========================================================================
    # REFLEKSI 5
    # =========================================================================
    add_heading_2(doc, "5. Bagaimana Anda akan menggunakan pemahaman tentang jalur kritis untuk memprioritaskan pengelolaan proyek kelompok Anda?")
    
    add_body_p(doc,
        "Sebagai Lead Author yang memegang tanggung jawab orkestrasi riset dan penulisan paper kelompok PRE-02, pemahaman matematis "
        "dan operasional mengenai Jalur Kritis (Critical Path Method) akan saya terjemahkan menjadi empat kebijakan manajerial konkret:")

    add_num_p(doc, "1.", "Penerapan Manajemen Berdasarkan Pengecualian (Management by Exception):",
        "Saya tidak akan membebani rapat koordinasi berkala kelompok dengan mengawasi seluruh aktivitas dengan intensitas yang sama. "
        "Fokus pemantauan progres harian (daily check-in) akan kami dedikasikan 80% pada aktivitas-aktivitas yang berada di jalur kritis PRE-02 "
        "—yaitu pembersihan dataset FNE (ACT-06), normalisasi fitur (ACT-07), pelatihan model deep learning MLP (ACT-12), kalibrasi probabilitas "
        "(ACT-13), dan perumusan ambang batas EWS (ACT-15). Kami memastikan bahwa setiap rintangan (blocker) pada jalur kritis ini harus "
        "diselesaikan dalam hitungan jam sebelum merembet menjadi keterlambatan proyek.")

    add_num_p(doc, "2.", "Prioritas Alokasi Sumber Daya Komputasi dan Tenaga Ahli (Resource Protection):",
        "Aktivitas di jalur kritis akan mendapatkan hak prioritas tertinggi atas sumber daya kelompok kami. Komputasi GPU performa tinggi, "
        "lingkungan eksekusi terisolasi, serta pendampingan diskusi intensif akan dialokasikan penuh untuk tugas-tugas kritis tersebut. "
        "Anggota tim tidak diperkenankan dialihkan ke pekerjaan dokumentasi sampingan apabila tugas pada jalur kritis yang menjadi tanggung "
        "jawabnya belum tuntas 100%.")

    add_num_p(doc, "3.", "Pemanfaatan Strategis Float pada Aktivitas Non-Kritis:",
        "Mengetahui bahwa aktivitas telaah literatur (ACT-03 dan ACT-04) memiliki Total Float yang panjang (TF = 22 hari), saya dapat "
        "mengelola beban kerja anggota tim secara lebih fleksibel dan manusiawi (Resource Smoothing). Anggota tim dapat mencicil penulisan "
        "matriks literatur secara bertahap tanpa merasa tertekan, atau bahkan dapat diperbantukan sementara untuk mempercepat pembersihan data "
        "jika aktivitas kritis ACT-06 mengalami kendala volume baris data.")

    add_num_p(doc, "4.", "Jalur Kritis sebagai Validasi Inti Model Early Warning System PRE-02:",
        "Yang paling menarik, pemahaman mengenai jalur kritis ini menjadi validasi konseptual langsung bagi topik penelitian kami sendiri. "
        "Salah satu variabel bebas utama dalam model PRE-02 adalah 'Progres Aktual vs Rencana' dan 'Sisa Waktu Deadline'. Model machine learning "
        "yang kami bangun pada dasarnya belajar bahwa keterlambatan pada aktivitas jalur kritis memiliki bobot dampak eksponensial terhadap "
        "lonjakan probabilitas keterlambatan akhir proyek (P(Delay) >= 0.65). Dengan menguasai CPM secara teori dan hitungan matematis, "
        "kami dapat menjustifikasi fitur-fitur model kami dengan argumentasi ilmiah yang sangat kuat di hadapan dosen penguji.")
