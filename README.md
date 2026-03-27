# Business Understanding
Jaya Jaya Edutech adalah perusahaan yang sedang berkembang pesat, namun menghadapi tantangan berupa tingginya tingkat perputaran karyawan (attrition rate). Kehilangan karyawan secara terus-menerus berdampak negatif pada produktivitas perusahaan dan membengkaknya biaya rekrutmen.

# Tujuan Proyek:

Mengidentifikasi faktor-faktor utama yang memengaruhi keputusan karyawan untuk resign.

Membangun model Machine Learning untuk memprediksi karyawan mana yang memiliki risiko tinggi untuk keluar.

Memberikan rekomendasi strategis kepada departemen HR untuk meningkatkan retensi karyawan.

# Faktor Utama Penyebab Attrition (Feature Importance)

Model Random Forest yang telah dilatih menghasilkan akurasi sebesar 85%. Dari model tersebut, kita dapat mengekstrak fitur apa saja yang paling berpengaruh terhadap keputusan resign.
5 Faktor utamanya adalah:

1. Usia (Age): Karyawan dengan usia yang lebih muda (biasanya di awal karier) cenderung lebih sering berpindah pekerjaan untuk mencari pengalaman atau kompensasi yang lebih baik.

2. Pendapatan Bulanan (Monthly Income): Karyawan yang keluar cenderung memiliki rata-rata gaji yang lebih rendah. Ketidakpuasan terhadap kompensasi finansial menjadi pendorong kuat untuk resign.

3. Dampak Beban Kerja (Lembur / OverTime) : Dari visualisasi data, terlihat pola yang jelas bahwa karyawan yang sering bekerja lembur (OverTime = Yes) memiliki persentase attrition yang jauh lebih tinggi dibandingkan yang tidak lembur. Hal ini mengindikasikan bahwa work-life balance yang buruk memicu kelelahan (burnout) dan mendorong karyawan untuk mencari peluang di tempat lain.

4. Total Tahun Bekerja (Total Working Years): Karyawan dengan masa kerja total yang masih sebentar memiliki tingkat loyalitas yang lebih fluktuatif.

5. Monthly rate = Meskipun Monthly Rate mencerminkan biaya operasional perusahaan, tingginya attrition di kategori ini menunjukkan bahwa karyawan dengan profil tarif tinggi—yang biasanya merupakan tenaga ahli—merasa ada ketidaksesuaian antara beban tanggung jawab yang mereka pikul dengan imbalan nyata yang mereka terima (Monthly Income), sehingga mereka lebih memilih untuk mencari peluang di luar.

# Conclusion & Rekomendasi Action Items
Berdasarkan temuan di atas, permasalahan HR di Jaya Jaya Edutech dapat diselesaikan dengan pendekatan proaktif. Berikut adalah beberapa rekomendasi action items untuk departemen HR:

Evaluasi Kebijakan Lembur & Work-Life Balance:
HR perlu memonitor jam lembur karyawan secara ketat. Jika suatu departemen terus-menerus lembur, pertimbangkan untuk menambah jumlah staf (hiring) atau memberikan insentif/cuti ekstra untuk mencegah burnout.

Penyesuaian Standar Gaji (Salary Benchmarking):
Mengingat Monthly Income adalah faktor krusial, HR harus melakukan riset pasar untuk memastikan gaji yang ditawarkan kompetitif, terutama untuk karyawan yang memiliki performa tinggi namun bergaji di bawah rata-rata.

Program Mentorship untuk Karyawan Muda:
Karena faktor Age (karyawan muda) rentan keluar, HR dapat membuat program engagement atau jalur pengembangan karier yang lebih jelas agar mereka merasa memiliki masa depan jangka panjang di Jaya Jaya Edutech.

Melakukan salary benchmarking (perbandingan gaji pasar) secara berkala, terutama untuk posisi-posisi yang memiliki Monthly Rate tinggi namun Monthly Income rendah.

Tujuan: Memastikan kompensasi yang diberikan kompetitif dan adil agar karyawan merasa dihargai sesuai dengan nilai ekonomi mereka di perusahaan.
