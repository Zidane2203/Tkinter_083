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