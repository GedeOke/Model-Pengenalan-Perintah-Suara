# 🐍 Snake Game dengan Kontrol Suara 🎤

## Pendahuluan
Selamat datang di **Snake Game dengan Kontrol Suara**! Proyek ini menggabungkan permainan snake klasik dengan sistem kontrol suara yang inovatif, memungkinkan Anda untuk mengendalikan ular menggunakan perintah suara. Proyek ini menggunakan Python, TensorFlow, dan PyAudio untuk menciptakan pengalaman bermain yang menyenangkan dan interaktif.

## Fitur-Fitur Unggulan
- 🎮 **Permainan Snake Klasik**: Nikmati mekanisme permainan snake tradisional dengan grafis halus dan kontrol yang responsif.
- 🗣️ **Kontrol Suara**: Kendalikan ular menggunakan perintah suara sederhana: "up", "down", "left", dan "right".
- 🔊 **Pemrosesan Audio Real-Time**: Menggunakan pemrosesan audio real-time untuk menginterpretasikan perintah suara dan mengendalikan permainan.
- 🤖 **Integrasi Pembelajaran Mesin**: Mengintegrasikan model TensorFlow yang telah dilatih untuk mengenali perintah suara dengan akurasi tinggi.

## Instalasi

1. **Kloning repositori**:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. **Buat lingkungan virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Di Windows gunakan `venv\Scripts\activate`
    ```

3. **Instal dependensi yang diperlukan**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Unduh dan atur model TensorFlow**:
    - Pastikan Anda memiliki model TensorFlow untuk pengenalan suara yang terletak di `model/audioModel`.

## Penggunaan

1. **Jalankan permainan**:
    ```bash
    python main.py
    ```

2. **Kendalikan ular**:
    - Gunakan perintah suara untuk menggerakkan ular.
    - Perintah: "up", "down", "left", "right".

## Struktur Proyek
- **main.py**: Titik masuk utama untuk permainan. Menyiapkan layar permainan dan menangani loop utama permainan.
- **snake.py**: Berisi kelas `Snake` yang mendefinisikan perilaku dan properti ular.
- **voice_control.py**: Menangani logika kontrol suara, termasuk merekam audio, memprosesnya, dan memprediksi perintah menggunakan model TensorFlow.
- **audio_recorder.py**: Mengelola perekaman audio menggunakan PyAudio.
- **audio_precessor.py**: Memproses buffer audio dan mengonversinya ke dalam format yang sesuai untuk model TensorFlow.
- **audio_model.ipynb**: Notebook Jupyter yang digunakan untuk melatih dan mengevaluasi model TensorFlow untuk pengenalan perintah suara.

## Dependensi
- Python 3.x
- TensorFlow
- PyAudio
- NumPy

## Kontribusi
Kontribusi sangat diterima! Jika Anda memiliki ide atau perbaikan, jangan ragu untuk membuka isu atau mengirimkan pull request.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Lihat berkas [LICENSE](LICENSE) untuk detail lebih lanjut.

## Penghargaan
- Terinspirasi oleh permainan Snake klasik.
- Menggunakan TensorFlow untuk pembelajaran mesin.
- Menggunakan PyAudio untuk perekaman dan pemrosesan audio.

Selamat bermain dan semoga bersenang-senang mengendalikan ular dengan suara Anda! 🎉
