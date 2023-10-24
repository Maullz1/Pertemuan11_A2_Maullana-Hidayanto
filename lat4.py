def hitung_jumlah_angka_dapat_dibagi_habis(daftar_angka, pemisah):
    jumlah = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            jumlah += angka
    return jumlah

# Contoh penggunaan fungsi dengan list angka dan angka pemisah yang berbeda
list_angka = [10, 15, 20, 25, 30, 35]
angka_pemisah = 5

hasil = hitung_jumlah_angka_dapat_dibagi_habis (list_angka, angka_pemisah)
print("Jumlah angka yang dapat dibagi habis oleh", angka_pemisah, "adalah", hasil)

list_angka = [5, 15, 20, 35, 60]
angka_pemisah = 10

hasil2 = hitung_jumlah_angka_dapat_dibagi_habis(list_angka, angka_pemisah)
print("Jumlah angka yang dapat dibagi habis oleh", angka_pemisah, "adalah", hasil2)
