# 🎤 Pengenalan Perintah Suara

Selamat datang di proyek **Pengenalan Perintah Suara**! Proyek ini bertujuan untuk mengembangkan sistem pengenalan perintah suara yang menggunakan TensorFlow dan Keras. Sistem ini akan mendeteksi perintah dasar seperti "up", "down", "left", "right", dan "no".

## 🚀 Fitur Utama

- **Perekaman Audio**: Rekam audio dari mikrofon dengan mudah.
- **Pra-pemrosesan Audio**: Konversi buffer audio menjadi spektogram siap pakai.
- **Prediksi Real-time**: Deteksi perintah suara secara langsung dengan model terlatih.
- **Pelatihan Model**: Latih model pengenalan suara Anda sendiri menggunakan dataset Mini Speech Commands.

## 🗂️ Struktur Proyek

Proyek ini terdiri dari beberapa komponen utama:

1. **`recording_helper.py`**: Script untuk merekam audio dari mikrofon.
2. **`tf_helper.py`**: Script untuk memproses buffer audio menjadi spektogram.
3. **`audio_system.py`**: Script utama untuk memuat model, merekam audio, dan memprediksi perintah suara.
4. **`audio_model.ipynb`**: Notebook Jupyter yang digunakan untuk melatih dan mengevaluasi model.

## 📋 Panduan Penggunaan

### Prasyarat

Pastikan Anda telah menginstal semua ketergantungan yang diperlukan dengan menjalankan:

```bash
pip install -r requirements.txt
