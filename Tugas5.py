# Aplikasi Prediksi Prodi Pilihan

import tkinter as tk
from tkinter import ttk


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