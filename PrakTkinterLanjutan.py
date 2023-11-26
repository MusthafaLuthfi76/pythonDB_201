# Import library tkinter: Library untuk membuat antarmuka grafis pengguna (GUI) di Python.
import tkinter as tk

# Import library sqlite3: Library untuk berinteraksi dengan database SQLite.
import sqlite3

# Membuat daftar untuk memberi label pada nilai setiap mata pelajaran.
mata_pelajaran = ["Komputer", "PAI", "Biologi", "Kimia", "Bahasa Indonesia",
                       "Bahasa Inggris", "Sejarah", "Geografi", "Ekonomi", "Seni"]

def hasil_prediksi():

    # Mendapatkan nilai setiap mata pelajaran dan nama siswa dari input
    nilai_pelajaran = [mata_pelajaran_var[i].get() for i in range(10)]
    nama_siswa = entry_nama.get()

    # Menentukan hasil prediksi prodi berdasarkan nilai tertinggi
    fakultas = prediksi_fakultas(nilai_pelajaran)

    # Menampilkan hasil prediksi
    luaran_hasil.config(text=f"Fakultas: {fakultas}")

    # Menyimpan data ke dalam database SQLite
    simpan_ke_database(nama_siswa, nilai_pelajaran, fakultas)

def prediksi_fakultas(nilai_pelajaran):

    # Mencari indeks nilai tertinggi pada daftar nilai mata pelajaran.
    indeks_tertinggi = nilai_pelajaran.index(max(nilai_pelajaran))
    fakultas_list = ["Teknik", "Agama Islam", "Kedokteran", "Teknik", "Bahasa", "Bahasa",
                  "Sejarah", "Geografi", "Ekonomi dan Bisnis", "Seni"]

    # Mengembalikan prodi berdasarkan indeks tertinggi.
    return fakultas_list[indeks_tertinggi]

def simpan_ke_database(nama, nilai_pelajaran, fakultas):

    # Membuat koneksi ke database SQLite (nilai_siswa.db).
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    # Membuat tabel nilai_siswa jika belum ada.
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                      (nama_siswa TEXT, matematika REAL, fisika REAL, biologi REAL, kimia REAL,
                       bahasa_indonesia REAL, bahasa_inggris REAL, sejarah REAL, geografi REAL,
                       ekonomi REAL, seni REAL, prediksi_fakultas TEXT)''')
    
    # Memasukkan data siswa dan hasil prediksi ke dalam tabel.
    data = tuple([nama] + nilai_pelajaran + [fakultas])
    cursor.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    # Melakukan commit untuk menyimpan perubahan dan menutup koneksi.
    conn.commit()
    conn.close()

# Membuat objek utama untuk aplikasi Tkinter.
root = tk.Tk()

# Membuat Judul aplikasi tkinter
root.title("Aplikasi Prediksi Fakultas")

# Membuat label yang ditaruh diatas sendiri dengan tulisan "Aplikasi Prediksi Fakultas"
judul_label = tk.Label(root, text="Aplikasi Prediksi Fakultas", bg="#f0f0f0", font=("Arial", 16, "bold"))
judul_label.pack()

# Membuat frame untuk nanti tempat ditaruh mata pelajaran dan juga nilai
frame_input = tk.Frame(root)
frame_input.pack()

# Membuat label nama di bawah tulisan "Aplikasi Prediksi Fakultas"
label_nama = tk.Label(frame_input, text="Nama Siswa:", font=("Arial", 10))
label_nama.grid(row=1, column=0)

# Membuat Entry kosong untuk nama, anda bisa menginputkan nama anda disini
entry_nama = tk.Entry(frame_input, font=("Arial", 10))
entry_nama.grid(row=1, column=1)

# Membuat sebuah list dan scale (mata_pelajaran) yang berisi 10 objek DoubleVar dari modul tkinter. DoubleVar digunakan untuk menyimpan nilai float (bilangan desimal) dari elemen GUI.
mata_pelajaran_var = [tk.DoubleVar() for _ in range(10)]
mata_pelajaran_entries = []

# Iterasi sebanyak 10 kali (sesuai dengan jumlah mata pelajaran).
for i in range(10):
    # Membuat label mata_pelajaran untuk setiap mata pelajaran dengan menggunakan tk.Label. Label ini menunjukkan nama mata pelajaran.
    label_mata_pelajaran = tk.Label(frame_input, text=f"Nilai {mata_pelajaran[i]}:", font=("Arial", 10))
    # Mengatur label tersebut di dalam frame menggunakan grid.
    label_mata_pelajaran.grid(row=i + 2, column=0)
    # Membuat Scale untuk nilai mata_pelajaran untuk setiap mata pelajaran. Berfungsi sebagai bar penggeser untuk memasukkan nilai antara 0 hingga 100.
    entry_mata_pelajaran = tk.Scale(frame_input, from_=0, to=100, variable=mata_pelajaran_var[i], orient=tk.HORIZONTAL, font=("Arial", 10))
    # Mengatur Scale tersebut di dalam frame menggunakan grid.
    entry_mata_pelajaran.grid(row=i + 2, column=1)
    # Menambahkan Scale ke dalam list mata_pelajaran_entries.
    mata_pelajaran_entries.append(entry_mata_pelajaran)

# Membuat tombol  dengan teks Submit Nilai. fungsi hasil_prediksi akan ditampilkan saat tombol ditekan.
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi, bg="green", fg="white", font=("Arial", 13, "bold"))
button_submit.pack()

# Membuat label dengan nama luaran_hasil tidak ada teks untuk menampilkan hasil prediksi.
luaran_hasil = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12, "italic"))
luaran_hasil.pack()

# Memulai loop utama Tkinter untuk menjalankan aplikasi.
root.mainloop()
