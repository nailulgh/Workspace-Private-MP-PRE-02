# -*- coding: utf-8 -*-
"""
Section A Builder: Tugas Tertulis Individu
Pertemuan 6: Manajemen Jadwal Proyek (Bagian II)
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
    add_heading_2(doc, "1. Apa yang dimaksud dengan proses Develop Schedule dalam manajemen proyek dan apa saja input yang diperlukan untuk proses ini?")
    
    add_body_p(doc,
        "Proses Develop Schedule (Mengembangkan Jadwal) adalah proses mengintegrasikan dan menganalisis urutan aktivitas, durasi kerja, "
        "kebutuhan sumber daya manusia dan material, serta berbagai batasan jadwal untuk menciptakan model jadwal proyek (project schedule model) "
        "yang siap dieksekusi, dimonitor, dan dikendalikan (Project Management Institute [PMI], 2017, hal. 205). Proses ini merupakan 'jantung' "
        "dari kelompok proses perencanaan manajemen jadwal karena menyatukan seluruh estimasi parsial menjadi sebuah kerangka waktu komprehensif "
        "yang menetapkan tanggal mulai yang direncanakan (planned start dates) dan tanggal selesai yang direncanakan (planned finish dates) "
        "untuk seluruh aktivitas dan deliverable proyek.")

    add_body_p(doc,
        "Berdasarkan standar PMBOK Guide 6th Edition (PMI, 2017, hal. 206-209), proses Develop Schedule memerlukan serangkaian dokumen input kunci:")

    add_num_p(doc, "1.", "Schedule Management Plan (Rencana Manajemen Jadwal):",
        "Menetapkan metodologi penjadwalan yang digunakan, piranti lunak yang diadopsi, tingkat presisi satuan waktu, serta aturan pemutakhiran jadwal.")

    add_num_p(doc, "2.", "Scope Baseline (Garis Dasar Ruang Lingkup):",
        "Terdiri atas Project Scope Statement, Work Breakdown Structure (WBS), dan WBS Dictionary. Scope baseline memastikan bahwa model jadwal "
        "mencakup 100% pekerjaan deliverable tanpa ada yang terlewat (100% Rule).")

    add_num_p(doc, "3.", "Activity List & Activity Attributes (Daftar & Atribut Aktivitas):",
        "Memuat deskripsi operasional aktivitas, kode identifikasi unik, serta batasan-batasan teknis awal.")

    add_num_p(doc, "4.", "Project Schedule Network Diagrams (Diagram Jaringan Jadwal Proyek):",
        "Menyediakan struktur graf berarah yang memetakan hubungan logis (Finish-to-Start, Start-to-Start, Finish-to-Finish, Start-to-Finish) "
        "serta penyesuaian percepatan (Lead) dan jeda waktu (Lag) antartugas.")

    add_num_p(doc, "5.", "Activity Duration Estimates & Basis of Estimates (Estimasi Durasi & Basis Estimasi):",
        "Perkiraan kuantitatif jumlah periode kerja yang diperlukan untuk menyelesaikan masing-masing tugas beserta dokumentasi asumsi risikonya.")

    add_num_p(doc, "6.", "Resource Requirements & Resource Calendars (Kebutuhan & Kalender Sumber Daya):",
        "Mengidentifikasi jenis dan kuantitas tenaga ahli, server komputasi, atau lisensi yang dialokasikan, serta hari kerja aktif dan hari libur "
        "dari masing-masing sumber daya tersebut.")

    add_num_p(doc, "7.", "Project Assumptions Log & Risk Register (Log Asumsi & Daftar Risiko):",
        "Memberikan wawasan mengenai potensi kendala waktu, risiko kontinjensi, dan faktor eksternal yang membatasi fleksibilitas eksekusi jadwal.")

    # =========================================================================
    # SOAL 2
    # =========================================================================
    add_heading_2(doc, "2. Jelaskan perbedaan antara Critical Path Method (CPM) dan Critical Chain Method! Dalam situasi apa masing-masing metode lebih sesuai digunakan?")
    
    add_body_p(doc,
        "Critical Path Method (CPM) dan Critical Chain Method (CCM) adalah dua paradigma metodologi penjadwalan yang memiliki landasan filosofis, "
        "asumsi dasar, dan penanganan ketidakpastian yang berbeda secara fundamental (Goldratt, 1997; Kerzner, 2017; Leach, 2014):")

    add_bullet_p(doc, "Critical Path Method (CPM):",
        "Merupakan pendekatan deterministik berbasis dependensi tugas murni (task-dependency driven). CPM mengasumsikan ketersediaan sumber daya "
        "tak terbatas pada tahap awal pemodelan jaringan. Jalur kritis ditentukan semata-mata oleh rangkaian tugas terpanjang dengan total float "
        "sama dengan nol. Cadangan keselamatan (safety buffer) umumnya disisipkan secara tersembunyi di dalam masing-masing aktivitas individu "
        "oleh estimator tugas (local padding).")

    add_bullet_p(doc, "Critical Chain Method (CCM):",
        "Merupakan pendekatan probabilistik berbasis kendala sumber daya (resource-constrained driven) yang dikembangkan dari Theory of Constraints "
        "(Goldratt, 1997). CCM mengakui bahwa ketersediaan sumber daya manusia dan peralatan di dunia nyata sangat terbatas. Dalam CCM, "
        "seluruh cadangan keselamatan tersembunyi dipangkas dari aktivitas individu (menghasilkan estimasi durasi agresif 50% kemungkinan tercapai). "
        "Cadangan waktu tersebut kemudian dikumpulkan dan dikelola secara terpusat dalam bentuk Project Buffer di akhir proyek serta Feeding Buffer "
        "pada titik temu rantai non-kritis menuju rantai kritis.")

    add_body_p(doc,
        "Perbandingan matriks komparatif antara CPM dan CCM diuraikan dalam tabel berikut:")

    table_data_p2 = [
        ["Dimensi Analisis", "Critical Path Method (CPM)", "Critical Chain Method (CCM)"],
        ["Fokus Penggerak Utama", "Ketergantungan Logis Tugas (Task Logic Driven)", "Ketergantungan Tugas & Keterbatasan Sumber Daya (Resource Constraints)"],
        ["Penempatan Cadangan Waktu", "Tersebar di masing-masing aktivitas (Local safety padding)", "Terpusat di akhir proyek (Project Buffer) dan jalur pengumpan (Feeding Buffer)"],
        ["Pendekatan Perilaku Manusia", "Mengabaikan fenomena perilaku (rentan Parkinson's Law & Student Syndrome)", "Secara aktif memitigasi Parkinson's Law dan Student Syndrome dengan durasi agresif"],
        ["Penentu Jalur Terpanjang", "Lintasan terpanjang berbasis durasi tanpa kendala sumber daya", "Rantai kritis terpanjang yang memadukan logika tugas dan bottleneck sumber daya"],
        ["Metrik Kontrol Pemantauan", "Varians Jadwal (SV), Earned Value (SPI), dan Total Float", "Tingkat Konsumsi Buffer (Buffer Burn Rate) vs Kemajuan Rantai Kritis"],
        ["Kondisi Terbaik Penerapan", "Proyek prediktif dengan ketersediaan SDM melimpah, multi-kontraktor independen, atau konstruksi fisik", "Proyek rekayasa perangkat lunak, riset R&D, dan proyek dengan sumber daya langka (shared resources)"]
    ]
    create_table(doc, [3.2, 6.9, 6.9],
                 ["Dimensi Analisis", "Critical Path Method (CPM)", "Critical Chain Method (CCM)"],
                 table_data_p2[1:])

    # =========================================================================
    # SOAL 3
    # =========================================================================
    add_heading_2(doc, "3. Apa perbedaan antara resource leveling dan resource smoothing? Kapan masing-masing teknik digunakan?")
    
    add_body_p(doc,
        "Resource Optimization (Optimasi Sumber Daya) digunakan untuk menyesuaikan model jadwal ketika terjadi kelebihan beban kerja (overallocation) "
        "atau fluktuasi tajam pada pemanfaatan tenaga kerja. Terdapat dua teknik utama yang memiliki dampak kontraktual dan geometris berbeda:")

    add_bullet_p(doc, "Resource Leveling (Penyeimbangan Sumber Daya):",
        "Teknik di mana tanggal mulai dan selesai aktivitas disesuaikan berdasarkan batasan ketersediaan sumber daya dengan tujuan utama "
        "menyeimbangkan permintaan sumber daya agar tidak melebihi kapasitas batas maksimum yang tersedia. Karakteristik utama dari resource leveling "
        "adalah **dapat mengubah jalur kritis dan memperpanjang total durasi proyek**. Jika seorang arsitek sistem yang menangani dua tugas kritis "
        "mengalami overallocation, salah satu tugas harus diundur secara sekuensial sehingga tanggal selesai proyek otomatis bergeser mundur (PMI, 2017).\n"
        "– Kapan Digunakan: Diterapkan ketika sumber daya bersama yang kritis mengalami alokasi berlebih parah, jumlah personel tidak dapat ditambah "
        "(resource limit constraint mutlak), atau ketika ketersediaan peralatan/server sangat terbatas pada jam kerja tertentu.")

    add_bullet_p(doc, "Resource Smoothing (Perataan Sumber Daya):",
        "Teknik penyesuaian aktivitas yang mengoptimalkan alokasi sumber daya **hanya di dalam batas kelonggaran waktu (float / slack)** "
        "yang telah tersedia untuk setiap aktivitas. Karakteristik fundamental dari resource smoothing adalah **TIDAK PERNAH mengubah jalur kritis "
        "dan TIDAK PERNAH menunda tanggal penyelesaian proyek**. Tanggal target penyelesaian proyek diperlakukan sebagai batas kaku yang tidak boleh dilanggar.\n"
        "– Kapan Digunakan: Diterapkan ketika tanggal akhir proyek telah dikunci secara kontraktual oleh sponsor atau pasar, namun manajer proyek "
        "ingin meratakan beban puncak (peak demand) tim pengembang agar tidak terjadi pergantian drastis antara periode lembur ekstrem dan periode menganggur.")

    table_data_p3 = [
        ["Parameter", "Resource Leveling", "Resource Smoothing"],
        ["Tujuan Primer", "Menyelesaikan masalah alokasi berlebih (overallocation) hingga tuntas", "Mengurangi fluktuasi pemanfaatan sumber daya tanpa melanggar batas waktu"],
        ["Dampak pada Jalur Kritis", "Dapat mengubah konfigurasi jalur kritis proyek", "Jalur kritis TIDAK berubah sama sekali"],
        ["Dampak pada Durasi Proyek", "Sering kali memperpanjang total durasi proyek (tenggat waktu mundur)", "Total durasi proyek tetap konstan (tenggat waktu terkunci)"],
        ["Batasan Penyesuaian", "Dibatasi oleh kapasitas maksimum sumber daya yang tersedia", "Dibatasi oleh nilai Free Float dan Total Float dari aktivitas non-kritis"]
    ]
    create_table(doc, [3.2, 6.9, 6.9],
                 ["Parameter", "Resource Leveling", "Resource Smoothing"],
                 table_data_p3[1:])

    # =========================================================================
    # SOAL 4
    # =========================================================================
    add_heading_2(doc, "4. Sebutkan dan jelaskan dua teknik schedule compression beserta kelebihan dan kekurangan masing-masing!")
    
    add_body_p(doc,
        "Schedule Compression (Kompresi Jadwal) adalah teknik yang digunakan untuk mempersingkat durasi operasional jadwal proyek tanpa "
        "mengurangi ruang lingkup pekerjaan yang telah disepakati (PMI, 2017, hal. 215). Dua teknik utama kompresi jadwal adalah:")

    add_num_p(doc, "1.", "Crashing (Penambahan Sumber Daya Berbayar):",
        "Teknik mempercepat durasi jadwal dengan menambahkan sumber daya tambahan pada aktivitas yang berada di **jalur kritis** dengan biaya "
        "tambahan seminimal mungkin. Contoh tindakan crashing mencakup persetujuan jam kerja lembur (overtime), penambahan tenaga pengembang "
        "kontrak berpengalaman, atau penyewaan kapasitas komputasi cloud berkecepatan tinggi.\n"
        "• Kelebihan: Menjaga urutan logika dependensi asli proyek tetap utuh, sehingga tidak menimbulkan risiko pengerjaan ulang (rework) "
        "akibat ketidakpastian desain.\n"
        "• Kekurangan: Meningkatkan biaya langsung proyek secara signifikan (cost trade-off). Selain itu, berlakunya Hukum Brooks (The Mythical "
        "Man-Month) memperingatkan bahwa 'menambahkan tenaga kerja pada proyek perangkat lunak yang terlambat justru dapat membuatnya semakin lambat' "
        "akibat beban overhead komunikasi dan transfer pengetahuan.")

    add_num_p(doc, "2.", "Fast-Tracking (Eksekusi Paralel Tumpang Tindih):",
        "Teknik mempercepat jadwal di mana aktivitas atau fase pekerjaan yang biasanya dilakukan secara berurutan (sekuensial), diubah untuk "
        "dilaksanakan secara bersamaan (paralel) atau tumpang tindih dengan memanfaatkan lead time.\n"
        "• Kelebihan: Mampu memotong durasi jadwal proyek secara signifikan tanpa memerlukan penambahan anggaran keuangan langsung.\n"
        "• Kekurangan: Meningkatkan risiko proyek secara drastis (risk trade-off) dan berpotensi memicu pengerjaan ulang (rework) skala besar. "
        "Sebagai contoh, jika tim pengembang mulai mengkodekan backend sistem sebelum spesifikasi arsitektur basis data difinalisasi, setiap "
        "perubahan pada skema basis data akan memaksa tim membuang dan menulis ulang kode yang telah dibuat.")

    table_data_p4 = [
        ["Teknik Kompresi", "Mekanisme Operasional", "Dampak Biaya", "Dampak Risiko & Rework", "Kapan Paling Tepat Digunakan?"],
        ["Crashing", "Menambah sumber daya pada aktivitas kritis (lembur, vendor, server)", "Meningkat Signifikan (Anggaran bertambah)", "Risiko relatif rendah, potensi kelelahan tim pengembang", "Ketika sponsor bersedia menambah dana darurat demi mengejar target pasar"],
        ["Fast-Tracking", "Memparalelkan aktivitas kritis yang semula sekuensial (overlap)", "Tidak bertambah secara langsung", "Meningkat Drastis (Risiko pengerjaan ulang sangat tinggi)", "Ketika anggaran finansial terkunci mati namun aktivitas dapat ditoleransi tumpang tindih"]
    ]
    create_table(doc, [2.5, 3.5, 3.2, 3.8, 4.0],
                 ["Teknik Kompresi", "Mekanisme Operasional", "Dampak Biaya", "Dampak Risiko & Rework", "Kapan Paling Tepat Digunakan?"],
                 table_data_p4)

    # =========================================================================
    # SOAL 5
    # =========================================================================
    add_heading_2(doc, "5. Apa yang dimaksud dengan schedule baseline dan mengapa dokumen ini penting dalam pengendalian proyek?")
    
    add_body_p(doc,
        "Schedule Baseline (Garis Dasar Jadwal) adalah versi model jadwal proyek yang telah ditelaah secara mendalam, disepakati oleh tim proyek, "
        "dan disetujui secara formal oleh Project Sponsor atau Change Control Board (CCB) (PMI, 2017, hal. 217). Schedule baseline memuat "
        "tanggal mulai baseline (baseline start dates) dan tanggal selesai baseline (baseline finish dates) untuk seluruh deliverable dan milestone. "
        "Setelah disahkan, schedule baseline menjadi dokumen beku yang **hanya dapat diubah melalui prosedur formal Pengendalian Perubahan Terintegrasi "
        "(Perform Integrated Change Control)**.")

    add_body_p(doc,
        "Schedule baseline memegang peranan krusial yang tak tergantikan dalam tata kelola dan pengendalian proyek karena empat alasan esensial:")

    add_num_p(doc, "1.", "Tolok Ukur Tunggal Evaluasi Kinerja Waktu (The Yardstick of Performance):",
        "Tanpa adanya baseline yang terkunci, konsep 'keterlambatan' atau 'kecepatan' menjadi tidak bermakna. Baseline menyediakan titik jangkar "
        "objektif untuk membandingkan posisi progres fisik aktual terhadap rencana teoritis yang disepakati.")

    add_num_p(doc, "2.", "Fondasi Analisis Nilai Hasil (Earned Value Management / EVM):",
        "Dokumen baseline adalah input wajib untuk menghitung Planned Value (PV), Schedule Variance (SV = EV - PV), dan Schedule Performance "
        "Index (SPI = EV / PV). Jika baseline bergeser sembarangan setiap kali terjadi keterlambatan, metrik EVM akan termanipulasi dan "
        "menghilangkan visibilitas kegagalan manajemen proyek.")

    add_num_p(doc, "3.", "Mencegah Normalisasi Keterlambatan (Combating Schedule Creep):",
        "Dalam proyek perangkat lunak, tim pengembang sering kali secara alami menggeser tanggal target setiap kali tugas mengalami hambatan. "
        "Schedule baseline mengunci komitmen awal sehingga setiap pergeseran tanggal harus dicatat sebagai deviasi varians yang menuntut justifikasi "
        "dan tindakan korektif (corrective actions).")

    add_num_p(doc, "4.", "Kaitan Langsung dengan Ground Truth Riset PRE-02:",
        "Bagi sistem kecerdasan buatan PRE-02, Schedule Baseline adalah sumber penentu label target keterlambatan. Variabel bebas 'Progres Aktual "
        "vs Rencana' dihitung dengan membandingkan persentase penyelesaian riil terhadap jadwal baseline. Tanpa baseline yang valid, model prediksi "
        "probabilitas keterlambatan tidak akan memiliki ground truth yang reliabel untuk dilatih.")

    # =========================================================================
    # SOAL 6
    # =========================================================================
    add_heading_2(doc, "6. Jelaskan perbedaan antara perhitungan maju (forward pass) dan perhitungan mundur (backward pass) dalam CPM! Informasi apa yang dihasilkan dari masing-masing perhitungan?")
    
    add_body_p(doc,
        "Dalam Critical Path Method (CPM), perhitungan maju (forward pass) dan perhitungan mundur (backward pass) adalah dua proses komputasi "
        "matematis yang saling melengkapi pada struktur graf berarah jaringan jadwal (Larson & Gray, 2021; PMI, 2017):")

    add_bullet_p(doc, "Perhitungan Maju (Forward Pass):",
        "Komputasi yang bergerak searah jarum jam dari simpul awal proyek (Start Node) menuju simpul akhir (Finish Node). Algoritma ini menjumlahkan "
        "durasi aktivitas secara kumulatif untuk mencari batas waktu paling dini suatu pekerjaan dapat dimulai dan diselesaikan.\n"
        "– Formula Matematis: Early Finish (EF) = Early Start (ES) + Durasi; Untuk simpul penggabungan (merge): ES_successor = max(EF seluruh predecessor).\n"
        "– Informasi Kunci yang Dihasilkan: Nilai Early Start (ES) per aktivitas, nilai Early Finish (EF) per aktivitas, serta **Total Durasi Minimum "
        "Penyelesaian Proyek** secara keseluruhan.")

    add_bullet_p(doc, "Perhitungan Mundur (Backward Pass):",
        "Komputasi yang bergerak berlawanan arah dari simpul akhir proyek (Finish Node) mundur menuju simpul awal (Start Node). Algoritma ini "
        "mengurangkan durasi aktivitas untuk mencari batas waktu paling lambat pekerjaan diizinkan mulai dan selesai tanpa menggeser total durasi proyek.\n"
        "– Formula Matematis: Late Start (LS) = Late Finish (LF) - Durasi; Untuk simpul percabangan mundur (burst): LF_predecessor = min(LS seluruh successor).\n"
        "– Informasi Kunci yang Dihasilkan: Nilai Late Finish (LF) per aktivitas, nilai Late Start (LS) per aktivitas, **Total Float (TF = LS - ES)**, "
        "**Free Float (FF)**, serta **Identifikasi Presisi Rangkaian Jalur Kritis (Critical Path)** di mana TF = 0.")

    table_data_p6 = [
        ["Dimensi Perbandingan", "Perhitungan Maju (Forward Pass)", "Perhitungan Mundur (Backward Pass)"],
        ["Arah Pergerakan Alur", "Maju dari awal proyek ke akhir proyek (Start → Finish)", "Mundur dari akhir proyek ke awal proyek (Finish → Start)"],
        ["Aturan Simpul Majemuk", "Menggunakan nilai MAKSIMUM (max EF) pada simpul merge", "Menggunakan nilai MINIMUM (min LS) pada simpul burst"],
        ["Operasi Aritmatika", "Penjumlahan durasi: EF = ES + Durasi", "Pengurangan durasi: LS = LF - Durasi"],
        ["Parameter Primer", "Early Start (ES) dan Early Finish (EF)", "Late Start (LS) dan Late Finish (LF)"],
        ["Output Strategis Utama", "Total Durasi Proyek & Tanggal Penyelesaian Tercepat", "Total Float, Free Float, dan Penetapan Jalur Kritis (CPM)"]
    ]
    create_table(doc, [3.2, 6.9, 6.9],
                 ["Dimensi Perbandingan", "Perhitungan Maju (Forward Pass)", "Perhitungan Mundur (Backward Pass)"],
                 table_data_p6[1:])

    # =========================================================================
    # SOAL 7
    # =========================================================================
    add_heading_2(doc, "7. Apa fungsi perangkat lunak manajemen proyek dalam pengembangan jadwal? Sebutkan minimal tiga fitur utama yang ditawarkan!")
    
    add_body_p(doc,
        "Perangkat lunak manajemen proyek (seperti Microsoft Project, ProjectLibre, Oracle Primavera P6, dan OpenProj) berfungsi sebagai mesin "
        "komputasi dan platform visualisasi jadwal terotomatisasi yang menghilangkan kerentanan kesalahan hitung manual pada proyek dengan puluhan "
        "hingga ribuan aktivitas (Schwalbe, 2019). Fungsinya bukan sekadar menggambar bagan, melainkan memelihara keterpaduan model jadwal matematis "
        "secara real-time setiap kali terjadi perubahan parameter durasi, dependensi, atau kalender kerja.")

    add_body_p(doc,
        "Empat fitur utama yang ditawarkan oleh perangkat lunak manajemen proyek modern mencakup:")

    add_num_p(doc, "1.", "Mesin Komputasi Jalur Kritis & Kalender Kerja Otomatis (Dynamic Scheduling Engine):",
        "Perangkat lunak secara instan melakukan forward pass dan backward pass secara otomatis. Ketika seorang pengguna mengubah durasi satu "
        "aktivitas, software secara instan merefleksikan dampaknya pada tanggal selesai seluruh successor, menghitung ulang float, dan menyorot "
        "apakah terjadi pergeseran jalur kritis baru dengan mempertimbangkan hari libur nasional serta jam kerja efektif.")

    add_num_p(doc, "2.", "Visualisasi Terpadu Gantt Chart & PDM Network Diagram:",
        "Menyajikan dua sudut pandang visual komplementer: Gantt Chart untuk presentasi garis waktu kalender kronologis beserta milestone, "
        "serta Network Diagram (AON) untuk menelusuri hubungan logika dependensi teknis antartugas.")

    add_num_p(doc, "3.", "Manajemen Alokasi & Pemerataan Sumber Daya (Resource Leveling Engine):",
        "Mendeteksi secara visual ketika seorang tenaga ahli atau modul server dialokasikan melebihi 100% kapasitas kerja hariannya (overallocation), "
        "serta menyediakan fitur penyeimbangan otomatis (leveling) berdasarkan prioritas tugas dan nilai float.")

    add_num_p(doc, "4.", "Pelacakan Garis Dasar & Analisis Nilai Hasil (Baseline Tracking & EVM Reporting):",
        "Menyimpan snapshot Schedule Baseline resmi dan menyandingkannya dengan progres aktual harian. Software secara otomatis menghitung "
        "Schedule Variance (SV), SPI, dan memproyeksikan perkiraan tanggal penyelesaian akhir (Estimate at Completion / EAC).")

    # =========================================================================
    # SOAL 8
    # =========================================================================
    add_heading_2(doc, "8. Jelaskan apa yang dimaksud dengan proses Control Schedule! Apa saja teknik yang digunakan dan output yang dihasilkan?")
    
    add_body_p(doc,
        "Proses Control Schedule (Mengendalikan Jadwal) adalah proses memantau status aktivitas proyek secara berkala untuk memperbarui progres "
        "pekerjaan aktual, mengukur deviasi kinerja terhadap Schedule Baseline, serta mengelola perubahan pada garis dasar jadwal secara proaktif "
        "sepanjang siklus hidup proyek (PMI, 2017, hal. 222). Tujuan utamanya bukan untuk menghukum tim ketika terjadi keterlambatan, melainkan "
        "mendeteksi varians jadwal sedini mungkin sehingga tindakan korektif (corrective actions) atau preventif dapat segera diimplementasikan.")

    add_heading_3(doc, "A. Teknik-Teknik Utama dalam Control Schedule:")
    add_bullet_p(doc, "Earned Value Analysis (EVA):",
        "Menghitung varians jadwal secara kuantitatif melalui Schedule Variance (SV = EV - PV) dan Schedule Performance Index (SPI = EV / PV). "
        "Nilai SPI < 1.0 mengindikasikan bahwa proyek berjalan lebih lambat dari jadwal yang direncanakan.")
    add_bullet_p(doc, "Critical Path Method Review:",
        "Memeriksa apakah keterlambatan terjadi pada aktivitas di jalur kritis atau aktivitas yang memiliki float. Keterlambatan pada aktivitas non-kritis "
        "yang melebihi total float-nya akan secara otomatis menciptakan jalur kritis baru (critical path migration).")
    add_bullet_p(doc, "Analisis Tren dan Peramalan (Trend Analysis & Forecasting):",
        "Mengevaluasi kinerja jadwal dari waktu ke waktu untuk melihat apakah tren produktivitas tim sedang membaik atau memburuk.")
    add_bullet_p(doc, "Analisis Skenario Bagaimana-Jika (What-If Scenario Analysis):",
        "Menyimulasikan berbagai opsi mitigasi jadwal menggunakan perangkat lunak (misal: bagaimana jika modul kalibrasi dilakukan crashing dengan "
        "lembur 2 hari, apakah proyek dapat mengejar tanggal target?).")

    add_heading_3(doc, "B. Output Utama yang Dihasilkan dari Control Schedule:")
    add_num_p(doc, "1.", "Work Performance Information (Informasi Kinerja Pekerjaan):",
        "Dokumentasi metrik kinerja komparatif terhitung, seperti nilai SV, SPI, serta analisis akar penyebab keterlambatan bagi pemangku kepentingan.")
    add_num_p(doc, "2.", "Schedule Forecasts (Perkiraan Jadwal):",
        "Estimasi tanggal penyelesaian proyek yang baru berdasarkan laju produktivitas aktual tim saat ini.")
    add_num_p(doc, "3.", "Change Requests (Permintaan Perubahan):",
        "Pengajuan formal tindakan korektif (misal: penambahan personel / crashing) atau re-baselining jika perubahan jadwal disetujui sponsor.")
    add_num_p(doc, "4.", "Project Management Plan Updates (Pembaruan Rencana Manajemen Proyek):",
        "Pembaruan resmi pada dokumen Schedule Baseline dan Schedule Management Plan yang disahkan melalui mekanisme CCB.")
