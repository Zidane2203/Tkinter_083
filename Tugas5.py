# Aplikasi Prediksi Prodi Pilihan

import tkinter as tk
from tkinter import ttk

def hasil_prediksi():
    label_hasil.config(
        text="Hasil Prediksi: Teknologi Informasi"
    )


# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("550x650")
root.resizable(False, False)

# Frame utama
main_frame = ttk.Frame(root, padding=25)
main_frame.pack(fill="both", expand=True)

# Judul aplikasi
judul = ttk.Label(
    main_frame,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold")
)
judul.pack(pady=(0, 20))

# Daftar mata pelajaran
mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Geografi",
    "Sejarah",
    "Informatika"
]

# Frame untuk input nilai
form_frame = ttk.Frame(main_frame)
form_frame.pack(fill="x", pady=5)

input_nilai = []

for i, pelajaran in enumerate(mata_pelajaran):
    label = ttk.Label(
        form_frame,
        text=pelajaran,
        width=20
    )
    label.grid(row=i, column=0, sticky="w", pady=5)

    entry = ttk.Entry(form_frame, width=25)
    entry.grid(row=i, column=1, sticky="ew", pady=5)

    input_nilai.append(entry)

form_frame.columnconfigure(1, weight=1)

# Tombol prediksi
tombol_prediksi = ttk.Button(
    main_frame,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol_prediksi.pack(pady=20)

# Label hasil prediksi
label_hasil = ttk.Label(
    main_frame,
    text="Hasil Prediksi: Belum tersedia",
    font=("Arial", 12, "bold"),
    foreground="blue"
)
label_hasil.pack(pady=5)