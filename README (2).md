# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
**Nama:** Aryo Dwi Haryanto

**Email:** aryodwi122@gmail.com

**ID Dicoding:** aryo_dwi_h

## Business Understanding
Perusahaan Edutech saat ini menghadapi tantangan terkait tingginya tingkat *attrition* (karyawan yang mengundurkan diri). Kehilangan karyawan yang terus-menerus dapat berdampak negatif pada operasional perusahaan, menurunkan produktivitas tim, serta meningkatkan biaya rekrutmen dan pelatihan karyawan baru. Oleh karena itu, perusahaan perlu memahami faktor-faktor pendorong mengapa karyawan memilih untuk *resign* agar manajemen dapat merancang strategi retensi sumber daya manusia (SDM) yang efektif dan berbasis data.

### Permasalahan Bisnis
- Apa saja faktor utama yang paling memengaruhi tingkat *attrition* karyawan di perusahaan?
- Bagaimana cara memprediksi karyawan yang memiliki risiko tinggi untuk mengundurkan diri di masa depan?
- Langkah dan strategi apa yang dapat diterapkan perusahaan untuk menekan angka *attrition*?

### Cakupan Proyek
- Melakukan *Exploratory Data Analysis* (EDA) untuk menganalisis secara mendalam dan memvisualisasikan data terkait karyawan.
- Membangun dan menyajikan *Business Dashboard* interaktif untuk mempermudah manajemen dalam memantau tren metrik *Human Resources*.
- Membangun model prediktif berbasis *Machine Learning* menggunakan algoritma *Random Forest Classifier* untuk mendeteksi dini potensi *attrition* pada karyawan.
- Merumuskan kesimpulan dan rekomendasi *action items* berbasis data bagi perusahaan.
### Persiapan

Sumber data: Data historis karyawan berupa file CSV (biasanya bernama `employee_data.csv`).

Setup environment:

```python
# Install library yang dibutuhkan (jika belum ada)
# !pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn joblib

# Import library untuk manipulasi data dan visualisasi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import library untuk Machine Learning (Scikit-Learn)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Import library untuk handling data imbalance
from imblearn.over_sampling import SMOTE

# Import library untuk menyimpan model
import joblib

# Mengabaikan warnings agar output lebih rapi
import warnings
warnings.filterwarnings('ignore') 

```

## Business Dashboard

Business dashboard yang telah dibuat menyajikan visualisasi data komprehensif terkait kondisi sumber daya manusia di perusahaan. Berdasarkan dashboard, terdapat total karyawan sebanyak 1.058 orang, dengan rincian 179 karyawan resign dan 879 karyawan bertahan (stay). Hal ini menunjukkan attrition rate perusahaan berada di angka 16,9%.

Visualisasi yang disajikan mencakup perbandingan attrition berdasarkan parameter demografi dan jabatan, seperti: Gender, tingkat waktu lembur (OverTime), peran pekerjaan (Job Role), pendapatan bulanan, dan lama bekerja di perusahaan (Years at Company). Dashboard ini membantu manajemen secara cepat melihat bahwa departemen atau kelompok karyawan tertentu memiliki rasio perputaran tenaga kerja (turnover) yang lebih tinggi.

LINK DASHBOARD : https://lookerstudio.google.com/s/lO5Frb8er7E 

## Conclusion

Berdasarkan analisis yang telah dilakukan, dapat disimpulkan bahwa tingkat attrition sangat dipengaruhi oleh beban kerja yang berlebih dan masa kerja. Karyawan yang sering mengambil lembur (OverTime) memiliki proporsi resign yang sangat tinggi dibandingkan yang tidak. Dari sisi demografi dan pekerjaan, karyawan dengan posisi Sales Representative dan karyawan dengan lama kerja di masa-masa awal (0 hingga 5 tahun) adalah kelompok rentan yang banyak meninggalkan perusahaan.

Selain itu, model prediktif klasifikasi berbasis algoritma Random Forest juga berhasil dibangun untuk memprediksi karyawan baru mana yang sekiranya rentan akan resign di kemudian hari.
### Rekomendasi Action Items (Optional)
Atur Kebijakan Lembur (OverTime): Evaluasi kembali distribusi pekerjaan di setiap divisi, terapkan manajemen workload yang lebih seimbang, dan tambahkan tenaga kerja (rekrutmen spesifik) jika diperlukan untuk mencegah karyawan mengalami burnout.

Tingkatkan Keterlibatan Karyawan (Engagement): Terapkan program penghargaan dan apresiasi untuk prestasi, libatkan karyawan lebih banyak dalam pengambilan keputusan, serta bangun budaya kerja yang positif dan kolaboratif.

Perkuat Hubungan Atasan–Bawahan: Selenggarakan program training leadership untuk jajaran manajer, adakan monitoring hubungan kerja yang sehat, serta jadwalkan evaluasi feedback rutin antara karyawan dan atasan secara one-on-one.

Fokus pada Retensi Karyawan Baru: Mengingat tingginya persentase resign di masa awal (0-5 tahun), optimalkan program onboarding, adakan sistem pendampingan (mentoring), dan berikan peta jalan (career path) yang jelas sejak awal karyawan bergabung.

Gunakan Model Prediktif untuk Deteksi Dini: Manfaatkan model machine learning Random Forest yang telah dibuat ke dalam sistem perusahaan untuk secara dini mengidentifikasi karyawan dengan risiko attrition tinggi, sehingga langkah intervensi dapat dilakukan sebelum mereka benar-benar mengundurkan diri.
