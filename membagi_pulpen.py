# Bagi Pena untuk Siswa
# Mudah
# Deskripsi Masalah
# 
# Misalkan Anda harus membagi 14 pulpen di antara 3 siswa secara merata.
# 
# Berapa banyak pulpen yang akan diperoleh setiap siswa jika pulpen harus dibagi rata?
# 
# Dan, berapa banyak pulpen yang tersisa yang tidak dapat dibagi?
# 
# Tugas
# 
#     Buat variabel bernama pens_numberdan menetapkan 14 untuk itu.
#     Buat variabel bernama students_numberdan menetapkan 3 untuk itu.
#     Hitung jumlah pena yang akan diperoleh setiap siswa dan cetaklah.
#     Hitung jumlah pulpen yang tersisa dan cetak.
    
pens_number = 14
students_number = 3

pens_each_student = pens_number // students_number

pens_left = pens_number % students_number

print(pens_each_student)

print(pens_left)