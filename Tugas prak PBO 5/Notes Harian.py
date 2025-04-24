import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

class AplikasiCatatan:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Harian")
        self.root.geometry("800x600")
        
        # Struktur data untuk menyimpan catatan
        self.catatan = []
        
        # Membuat menu bar
        self.buat_menu()
        
        # Membuat frame utama
        self.buat_widget()
        
    def buat_menu(self):
        # Membuat menu bar
        menubar = tk.Menu(self.root)
        
        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Keluar", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Menu Bantuan
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Tentang", command=self.tampilkan_tentang)
        menubar.add_cascade(label="Bantuan", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def buat_widget(self):
    # Warna tema
        bg_color = '#D2E0FB'  # sky blue
        widget_bg = '#C4D9FF'  # Putih
        text_bg = '#8EACCD'   # Putih sedikit abu
        button_bg = '#e1e1e1' # Abu muda
        
        # Configure root window background
        self.root.configure(bg=bg_color)
        
        # Frame untuk input catatan
        input_frame = tk.Frame(self.root, bg=bg_color)
        input_frame.pack(pady=10, padx=10, fill=tk.X)
        
        # Label dan Entry untuk judul
        tk.Label(input_frame, text="Judul:", bg=bg_color).grid(row=0, column=0, sticky=tk.W)
        self.judul_entry = tk.Entry(input_frame, width=50, bg=widget_bg)
        self.judul_entry.grid(row=0, column=1, padx=5)
        
        # Label dan Text untuk isi catatan
        tk.Label(input_frame, text="Isi Catatan:", bg=bg_color).grid(row=1, column=0, sticky=tk.NW, pady=5)
        self.isi_text = scrolledtext.ScrolledText(input_frame, width=50, height=10, wrap=tk.WORD, bg=widget_bg)
        self.isi_text.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame untuk tombol
        button_frame = tk.Frame(self.root, bg=bg_color)
        button_frame.pack(pady=5)
        
        # Tombol dengan warna
        self.tambah_btn = tk.Button(button_frame, text="Tambah Catatan", 
                                command=self.tambah_catatan, bg=button_bg)
        self.tambah_btn.pack(side=tk.LEFT, padx=5)
        
        self.hapus_btn = tk.Button(button_frame, text="Hapus Catatan", 
                                command=self.hapus_catatan, bg=button_bg)
        self.hapus_btn.pack(side=tk.LEFT, padx=5)
        
        # Frame untuk menampilkan catatan
        display_frame = tk.Frame(self.root, bg=bg_color)
        display_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Listbox dengan warna
        self.daftar_listbox = tk.Listbox(display_frame, width=30, bg=widget_bg)
        self.daftar_listbox.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
        
        # Text widget dengan warna
        self.tampil_text = scrolledtext.ScrolledText(
            display_frame, 
            width=50, 
            height=20, 
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg=text_bg
        )
        self.tampil_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Event binding untuk Listbox
        self.daftar_listbox.bind('<<ListboxSelect>>', self.tampilkan_catatan)
    
    def tambah_catatan(self):
        # Mendapatkan input dari pengguna
        judul = self.judul_entry.get().strip()
        isi = self.isi_text.get("1.0", tk.END).strip()
        
        # Validasi input
        if not judul or not isi:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong! Isi dulu yaa sebelum tambah notes")
            return
        
        # Menambahkan timestamp
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        # Menyimpan catatan
        catatan_baru = {
            'judul': judul,
            'isi': isi,
            'waktu': waktu
        }
        self.catatan.append(catatan_baru)
        
        # Menambahkan judul ke Listbox
        self.daftar_listbox.insert(tk.END, f"{judul} ({waktu})")
        
        # Mengosongkan input fields
        self.judul_entry.delete(0, tk.END)
        self.isi_text.delete("1.0", tk.END)
        
        messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan!")
    
    def tampilkan_catatan(self, event):
        # Mendapatkan indeks catatan yang dipilih
        selection = self.daftar_listbox.curselection()
        
        if selection:
            index = selection[0]
            
            # Mengaktifkan text widget sementara untuk mengedit
            self.tampil_text.config(state=tk.NORMAL)
            self.tampil_text.delete("1.0", tk.END)
            
            # Menampilkan isi catatan
            catatan = self.catatan[index]
            self.tampil_text.insert(tk.END, f"Judul: {catatan['judul']}\n")
            self.tampil_text.insert(tk.END, f"Waktu: {catatan['waktu']}\n")
            self.tampil_text.insert(tk.END, "\n" + catatan['isi'])
            
            # Mengembalikan ke mode read-only
            self.tampil_text.config(state=tk.DISABLED)
    
    def hapus_catatan(self):
        # Mendapatkan indeks catatan yang dipilih
        selection = self.daftar_listbox.curselection()
        
        if not selection:
            messagebox.showerror("Error", "Mau hapus apa nih? Pilih dulu catatan yang mau dihapus!")
            return
        
        # Konfirmasi penghapusan
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus catatan ini?"):
            index = selection[0]
            
            # Menghapus dari Listbox dan daftar catatan
            self.daftar_listbox.delete(index)
            self.catatan.pop(index)
            
            # Mengosongkan tampilan isi catatan
            self.tampil_text.config(state=tk.NORMAL)
            self.tampil_text.delete("1.0", tk.END)
            self.tampil_text.config(state=tk.DISABLED)
    
    def tampilkan_tentang(self):
        about_text = "Aplikasi Catatan Harian\nVersi 1.0\n\nAplikasi sederhana untuk mencatat kegiatan harian."
        messagebox.showinfo("Tentang", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiCatatan(root)
    root.mainloop()
    