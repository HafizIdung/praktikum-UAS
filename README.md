NAMA: hafiz abdurohman
kelas: TI.24.A4

ShoppingCart: Class yang menangani logika pengelolaan keranjang belanja (seperti menambah barang, menghitung total harga).
View: Class yang bertanggung jawab menampilkan data ke pengguna (seperti keranjang dan struk).


Digunakan untuk meminta input dari pengguna.
Parameter:
prompt: Teks yang ditampilkan ke pengguna untuk meminta input.
type_: Tipe data yang diinginkan (default: str).
condition: Fungsi untuk memvalidasi input (default: selalu benar).
error_message: Pesan yang ditampilkan jika input tidak valid.
Menggunakan mekanisme pengecualian (try-except) untuk menangani input yang tidak sesuai dengan type_.


Menyediakan daftar barang yang tersedia untuk ditambahkan ke keranjang.
Barang ditampilkan dalam format daftar dengan indeks, nama, dan harga.
Mengembalikan daftar barang dalam bentuk tuple (name, price).


Logika utama program:
Membuat instance keranjang belanja (cart = ShoppingCart()).
Menampilkan menu utama dengan 4 opsi:
Tambah barang.
Tampilkan keranjang.
Cetak struk.
Keluar.
Berdasarkan input pengguna (choice), fungsi memanggil logika yang sesuai:
Opsi 1 (Tambah Barang):
Menampilkan daftar barang.
Meminta pengguna memilih barang dan jumlahnya.
Menambahkan barang ke keranjang menggunakan cart.add_item.
Opsi 2 (Tampilkan Keranjang):
Memanggil View.show_items untuk menampilkan daftar barang di keranjang.
Opsi 3 (Cetak Struk):
Menghitung total harga dan jumlah barang di keranjang.
Memanggil View.show_receipt untuk menampilkan struk belanja.
Opsi 4 (Keluar):
Menghentikan program dengan pesan perpisahan.
