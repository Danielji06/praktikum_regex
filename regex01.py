import re

# fungsi membaca isi file
def baca_file(nama_file):
    handle = open(nama_file)
    artikel = handle.read() # langsung baca semua menjadi satu string
    handle.close()
    return artikel

# input nama file
nama_file = input("Masukkan nama file: ")
# baca berita dari file
artikel = baca_file(nama_file)
#print(artikel)

# lakukan operasi regex
# 1. tempilkan semua kata yang diawali huruf besar
pattern = r"[A-Z]\w+"
hasil = re.findall(pattern, artikel)
print(f"Ditemukan {len(hasil)}kata yang diawali oleh huruf besar")
print(hasil)
# 2. tampilkan informasi tanggal
pattern = r"\d\d?/\d\d?/\d\d\d\d"
hasil =re.findall(pattern, artikel)
print(f"Ditemukkan {len(hasil)} tanggal")
print(hasil)

# 3. tampilkan semua kata yang panjangnya 7
pattern = r"\b[A-Za-z]{7}\b"
hasil = re.findall(pattern, artikel)
print(f"Ditemukan {len(hasil)} kata yang jumlahnya ada 7")
print(hasil)

# 4. Ambil informasi uang
pattern = r"Rp .+ ribu|Rp .{3,9} juta"
hasil = re.findall(pattern, artikel)
print(f"Ditemukan {len(hasil)} kata yang jumlahnya ada 7")
print(hasil)

# 5. ganti semua kata tertentu dengan input user
kata_lama = input("Masukkan kata yang akan di ganti (casr sensitive): ")
kata_baru = input("Masukkan kata baru: ")

hasil = re.sub(kata_lama, kata_baru, artikel)


handle = open(nama_file, 'w')
handle.write(hasil)
handle.close()