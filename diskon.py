# Masalah Diskon
# Mudah
# Deskripsi Masalah
# 
# Misalkan Anda seorang mahasiswa dan Anda perlu membayar 1536 dolar sebagai biaya kuliah.
# 
# Perguruan tinggi menawarkan diskon 10% untuk pembayaran lebih awal. Berapa uang yang harus Anda bayarkan jika Anda melakukan pembayaran lebih awal?
# 
# Tugas
# 
#     Buat variabel bernama fee dan menetapkan 1536 untuk itu.
#     Buat variabel lain discount_percentdan menetapkan 10 untuk itu.
#     Hitung diskon dengan menggunakan rumus discount_percent/100 *fee dan menetapkannya ke discountvariabel.
#     Hitung dan cetak biaya yang harus Anda bayar dengan mengurangkan discount dari fee.

fee = 1536
discount_percent = 10

discount = discount_percent/100*fee

fee2 = fee - discount

print(fee2)