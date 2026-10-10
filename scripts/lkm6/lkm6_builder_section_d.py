# -*- coding: utf-8 -*-
"""
Section D Builder: Refleksi Mandiri
Pertemuan 6: Manajemen Jadwal Proyek (Bagian II)
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
        "Bagian ini memuat refleksi kritis dan introspeksi personal saya terhadap penguasaan materi Manajemen Jadwal Proyek (Bagian II) "
        "yang dipelajari pada Pertemuan 6, khususnya pengalaman praktis menyimulasikan jadwal menggunakan perangkat lunak, evaluasi perbandingan "
        "terhadap perhitungan manual, serta integrasinya dengan kepemimpinan riset kelompok berkode PRE-02 (Sistem Prediksi Probabilitas Keterlambatan "
        "Proyek Berbasis Machine Learning sebagai Early Warning System Manajemen Proyek).")

    # =========================================================================
    # REFLEKSI 1
    # =========================================================================
    add_heading_2(doc, "1. Bagaimana perasaan Anda saat menggunakan perangkat lunak manajemen proyek untuk pertama kalinya? Apa yang paling menyenangkan dan apa yang paling menantang?")
    
    add_body_p(doc,
        "Pengalaman pertama memodelkan jadwal proyek secara komprehensif menggunakan perangkat lunak manajemen proyek (Microsoft Project "
        "dan ProjectLibre) memberikan perpaduan rasa takjub intelektual sekaligus kehati-hatian teknis yang tinggi:")

    add_bullet_p(doc, "Aspek yang Paling Menyenangkan (The Rewarding Aspects):",
        "Hal yang paling memuaskan adalah menyaksikan representasi grafis dinamis (Gantt Chart dan Network Diagram) yang terbentuk secara instan "
        "hanya dalam hitungan detik setelah parameter durasi dan predecessor diinputkan. Hubungan dependensi yang sebelumnya hanya berupa "
        "deretan teks abstrak di atas kertas langsung bertransformasi menjadi garis panah penghubung yang elegan. Lebih dari itu, fitur penyorotan "
        "otomatis jalur kritis (critical path highlighting) dengan batang merah menyala memberikan kepuasan visual tersendiri, karena saya dapat "
        "langsung melihat rangkaian aktivitas mana yang mengendalikan nasib penyelesaian proyek secara keseluruhan.")

    add_bullet_p(doc, "Aspek yang Paling Menantang (The Challenging Aspects):",
        "Tantangan terbesar yang saya hadapi terletak pada manajemen kalender kerja (working calendar) dan pembatasan tugas (task constraints). "
        "Pada awal simulasi, saya sempat bingung mengapa tanggal selesai sebuah aktivitas berdurasi 5 hari melompat sejauh 7 hari kalender. "
        "Setelah menelaah konfigurasi internal, saya baru menyadari bahwa perangkat lunak secara otomatis mengunci hari Sabtu dan Minggu sebagai "
        "non-working days. Selain itu, memahami perbedaan antara tipe batasan jadwal 'As Soon As Possible' (ASAP) dengan 'Must Start On' menuntut "
        "kehati-hatian ekstra, karena salah memilih constraint akan mematikan otomatisasi perhitungan maju/mundur dan menghasilkan float negatif.")

    # =========================================================================
    # REFLEKSI 2
    # =========================================================================
    add_heading_2(doc, "2. Menurut Anda, apa manfaat terbesar menggunakan perangkat lunak dibandingkan dengan perhitungan manual dalam menyusun jadwal proyek?")
    
    add_body_p(doc,
        "Menurut analisis mendalam saya, manfaat terbesar perangkat lunak manajemen proyek bukan sekadar kecepatan komputasi aritmatika, "
        "melainkan **kemampuan pemeliharaan jadwal dinamis (Dynamic Schedule Maintenance)** dan **fasilitas simulasi skenario 'Bagaimana-Jika' "
        "(What-If Scenario Analysis) secara real-time**:")

    add_num_p(doc, "1.", "Ketahanan terhadap Perubahan (Agility in Schedule Dynamics):",
        "Dalam realitas pelaksanaan proyek, jadwal tidak pernah statis. Jika proyek terdiri atas 50 aktivitas dan terjadi penundaan 3 hari pada "
        "aktivitas ke-5, perhitungan manual mengharuskan kita menghapus dan menghitung ulang 45 aktivitas sisanya dari awal menggunakan lembaran kertas baru. "
        "Dengan perangkat lunak, kita cukup memperbarui progres aktual pada aktivitas ke-5, dan seluruh tanggal mulai/selesai ribuan tugas "
        "di hilir akan langsung diselaraskan kembali dalam tempo satu milidetik.")

    add_num_p(doc, "2.", "Manajemen Alokasi Sumber Daya Multi-Proyek (Resource Leveling):",
        "Perhitungan manual hampir mustahil memetakan apakah seorang Data Engineer sedang dibebani tugas 16 jam dalam satu hari yang sama "
        "(overallocation) di antara tiga modul yang berbeda. Perangkat lunak menyediakan indikator peringatan visual merah pada personel yang "
        "kelebihan beban serta menyediakan algoritma otomatis untuk meratakan jadwal tanpa merusak logika ketergantungan.")

    add_num_p(doc, "3.", "Pelacakan Kinerja Garis Dasar Objektif (Baseline vs Actual Variance):",
        "Perangkat lunak mampu menyimpan snapshot Schedule Baseline asli ke dalam memori permanen, lalu menyandingkannya dengan kurva progres "
        "aktual (tracking Gantt). Hal ini memungkinkan perhitungan Earned Value Management (EVM) seperti Schedule Variance (SV) dan SPI dilakukan "
        "secara otomatis untuk konsumsi rapat dewan direksi.")

    # =========================================================================
    # REFLEKSI 3
    # =========================================================================
    add_heading_2(doc, "3. Setelah melakukan praktik dengan perangkat lunak, apakah ada aktivitas dalam proyek kelompok Anda yang ternyata memiliki hubungan ketergantungan yang belum Anda perhatikan sebelumnya? Jelaskan!")
    
    add_body_p(doc,
        "Praktik pemodelan 21 aktivitas proyek PRE-02 menggunakan perangkat lunak membuka mata tim kami terhadap dua hubungan ketergantungan "
        "kritis yang sebelumnya terlewat dalam perencanaan konseptual awal:")

    add_num_p(doc, "1.", "Ketergantungan Konvergen Kalibrasi Probabilitas (ACT-15):",
        "Pada diskusi awal kelompok, kami mengira bahwa aktivitas kalibrasi probabilitas (Platt Scaling) dapat dimulai segera setelah salah satu "
        "model machine learning selesai dilatih (misal: selesai melatih Logistic Regression, langsung dikalibrasi secara mandiri). Namun, ketika "
        "kami memasukkan logika model ke dalam perangkat lunak, kami menyadari bahwa perbandingan kinerja Expected Calibration Error (ECE) dan "
        "Brier Score hanya valid jika seluruh arsitektur model (Logistic Regression, Random Forest, Gradient Boosting, dan MLP) telah selesai "
        "dilatih pada fold validasi yang identik. Perangkat lunak memaksa kami menetapkan ACT-15 sebagai simpul penggabungan mutlak (merge node) "
        "dengan 4 predecessor serentak (ACT-11, ACT-12, ACT-13, dan ACT-14).")

    add_num_p(doc, "2.", "Ketergantungan Ekstraksi Data Dokumen ERP (ACT-05) terhadap Project Charter (ACT-02):",
        "Awalnya kami berencana memulai ekstraksi data dari 8 dokumen PMP & SRS Super ERP Farm Nation Enterprise secara paralel sejak hari pertama. "
        "Namun simulasi perangkat lunak mengingatkan kami bahwa tanpa adanya Project Charter dan Schedule Plan yang disetujui (ACT-02), tim data "
        "tidak memiliki batasan ruang lingkup yang tegas mengenai kolom fitur mana yang harus diambil. Melakukan ekstraksi sebelum charter selesai "
        "berisiko memicu pengerjaan ulang (rework) data yang masif.")

    # =========================================================================
    # REFLEKSI 4
    # =========================================================================
    add_heading_2(doc, "4. Menurut Anda, sejauh mana perangkat lunak dapat menggantikan peran manajer proyek dalam penjadwalan? Aspek apa yang tetap memerlukan keputusan manusia?")
    
    add_body_p(doc,
        "Menurut pandangan saya, perangkat lunak manajemen proyek adalah sebuah **alat bantu komputasi dan visualisasi yang luar biasa (powerful tool)**, "
        "namun ia **SAMA SEKALI TIDAK DAPAT MENGGANTIKAN peran dan eksistensi Manajer Proyek**. Software hanyalah mesin pemroses data (execution engine) "
        "yang sepenuhnya tunduk pada aturan *Garbage In, Garbage Out*.")

    add_body_p(doc,
        "Ada empat dimensi fundamental dalam manajemen jadwal yang mutlak memerlukan pertimbangan dan keputusan manusia (human judgment):")

    add_num_p(doc, "1.", "Validasi Realisme Estimasi Durasi dan Produktivitas:",
        "Perangkat lunak tidak memiliki intuisi untuk menilai apakah estimasi durasi '3 hari' untuk pelatihan model deep learning itu realistis "
        "atau sekadar ilusi optimisme tim pengembang (optimism bias). Hanya manajer proyek yang berpengalaman yang mampu mengidentifikasi bias manusia, "
        "mengenali potensi hambatan teknis, dan memutuskan penerapan buffer waktu cadangan.")

    add_num_p(doc, "2.", "Penetapan Logika Ketergantungan dan Dekomposisi Ruang Lingkup:",
        "Software tidak dapat memutuskan secara mandiri tugas apa saja yang harus dikerjakan untuk membuat sistem Early Warning System PRE-02. "
        "Kemampuan mendekomposisi deliverable menjadi WBS dan menentukan apakah dua tugas harus terhubung secara Finish-to-Start atau Start-to-Start "
        "sepenuhnya bersumber dari kecerdasan arsitektural manusia.")

    add_num_p(doc, "3.", "Manajemen Konflik Interpersonal dan Negosiasi Pemangku Kepentingan:",
        "Ketika jadwal mengalami keterlambatan, software hanya bisa menandai tanggal dengan warna merah. Software tidak bisa menegosiasikan "
        "kompromi ruang lingkup dengan klien, menenangkan sponsor yang marah, atau memotivasi tim pengembang yang mengalami kelelahan mental (burnout). "
        "Kepemimpinan, empati, dan negosiasi adalah wilayah murni kecerdasan emosional manusia.")

    add_num_p(doc, "4.", "Keputusan Etis dan Kompromi Strategis (Trade-Off Decisions):",
        "Ketika terjadi krisis jadwal, apakah proyek harus melakukan Crashing (menambah anggaran lembur), Fast-Tracking (meningkatkan risiko bug), "
        "atau memotong fitur? Software dapat menyimulasikan angkanya, tetapi keputusan etis mengenai batas toleransi risiko kegagalan sistem "
        "adalah tanggung jawab moral manajer proyek.")

    # =========================================================================
    # REFLEKSI 5
    # =========================================================================
    add_heading_2(doc, "5. Jika Anda menjadi manajer proyek, bagaimana Anda akan menggunakan perangkat lunak untuk mengendalikan jadwal dan merespons keterlambatan yang terjadi?")
    
    add_body_p(doc,
        "Jika saya diamanahi peran sebagai Project Manager profesional, saya akan memanfaatkan perangkat lunak manajemen proyek melalui "
        "siklus pengendalian proaktif empat langkah:")

    add_num_p(doc, "1.", "Penguncian Schedule Baseline Resmi Sebelum Eksekusi Dimulai:",
        "Langkah pertama saya adalah memastikan seluruh dekomposisi WBS, dependensi, dan alokasi sumber daya telah disepakati seluruh tim, "
        "kemudian mengunci Schedule Baseline resmi di perangkat lunak. Saya tidak akan pernah mengizinkan baseline diubah secara informal "
        "tanpa melalui proses Change Control Board (CCB).")

    add_num_p(doc, "2.", "Pemantauan Varians Jadwal Mingguan Menggunakan Earned Value (EVA):",
        "Setiap akhir pekan, saya akan menginput persentase progres fisik aktual ke dalam software untuk memantau nilai Schedule Performance "
        "Index (SPI). Jika software menunjukkan nilai SPI < 0.95 pada aktivitas kritis, alarm peringatan dini internal saya langsung aktif "
        "untuk mencari akar masalah sebelum keterlambatan terakumulasi menjadi krisis besar.")

    add_num_p(doc, "3.", "Simulasi Skenario Kompresi Jadwal (What-If Analysis):",
        "Ketika keterlambatan pada jalur kritis tidak terhindarkan, saya akan membuat salinan (sandbox clone) dari file proyek di software untuk "
        "menguji berbagai alternatif pemulihan:\n"
        "– Opsi A: Menerapkan Crashing dengan menambah jam lembur pada aktivitas pengkodean pipeline.\n"
        "– Opsi B: Menerapkan Fast-Tracking dengan memparalelkan penulisan draf metodologi bab 3 saat eksperimen model sedang berjalan.\n"
        "Saya akan membandingkan kurva biaya dan profil risiko dari kedua skenario tersebut di dalam software sebelum membawa proposal tindakan "
        "korektif ke hadapan sponsor proyek.")

    add_num_p(doc, "4.", "Integrasi Data Varians Software ke Model Prediksi PRE-02:",
        "Secara khusus pada proyek riset kami, data varians jadwal (Schedule Variance dan Sisa Hari Deadline) yang diekspor dari software "
        "akan saya gunakan sebagai nilai input kontinu real-time ke dalam sistem Machine Learning Early Warning System PRE-02. Dengan demikian, "
        "sistem dapat secara otomatis menghasilkan skor probabilitas numerik keterlambatan [0.0 - 1.0]. Jika probabilitas melampaui ambang batas "
        "0.65, dashboard proyek akan memicu notifikasi peringatan dini kepada seluruh manajemen eksekutif.")
