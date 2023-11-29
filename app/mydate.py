import datetime

# Inisialisasi list untuk menyimpan tanggal pada hari Senin, Rabu, dan Jumat


def fetchday(tanggal, hari):
    pilih_hari =  [0, 2, 4] if hari == 0 else  [1, 3, 5] if hari == 1 else [4, 5, 6]
    tanggal_hari_tertentu = []
    i = 1
    # Loop dari tanggal sekarang sampai tanggal 1 bulan ke depan
    while i <= 30:
        # Periksa apakah tanggal adalah hari Senin, Rabu, atau Jumat
        if tanggal.weekday() in pilih_hari:  # Senin=0, Rabu=2, Jumat=4
            tanggal_hari_tertentu.append(tanggal)
            i = i+1
        # Tambahkan 1 hari ke tanggal
        tanggal += datetime.timedelta(days=1)

    return tanggal_hari_tertentu
