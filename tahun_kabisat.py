# Menghitung tahun kabisat
#
# Terdapat algoritme mudah untuk menentukan apakah suatu tahun termasuk tahun kabisat atau bukan sebagai berikut:
# 
#     Jika angka tahun itu habis dibagi 400, maka tahun itu sudah pasti tahun kabisat.
#     Jika angka tahun itu tidak habis dibagi 400 tetapi habis dibagi 100, maka tahun itu sudah pasti bukan merupakan tahun kabisat.
#     Jika angka tahun itu tidak habis dibagi 400, tidak habis dibagi 100 akan tetapi habis dibagi 4, maka tahun itu merupakan tahun kabisat.
#     Jika angka tahun tidak habis dibagi 400, tidak habis dibagi 100, dan tidak habis dibagi 4, maka tahun tersebut bukan merupakan tahun kabisat.
# 
# Tahun Kabisat menurut definisi ini ada sejak diluncurkannya kalender Gregorian (1582). 
#

tahun = int(input('Masukkan tahun : '))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print(tahun, 'adalah tahun kabisat')
        else:
            print(tahun,'adalah bukan tahun kabisat')
    else:
        print(tahun,'adalah tahun kabisat')
else:
    print(tahun,'adalah bukan tahun kabisat')