#tarif sewa mobil
tarifawal = 200000 #12jampertama
tarifselanjutnya = 10000 #per-jam
awalwakturental = 6.00
akhirwakturental = 23.50
#menghitung berapa lama rental
lamarental = int (akhirwakturental-awalwakturental)
#menghitung lama next rental
lamarentalselanjutnya = lamarental - 12
#menghitung tarif next rental
tarifrentalselanjutnya = lamarentalselanjutnya * tarifselanjutnya
totaltarif = tarifawal + tarifrentalselanjutnya
print(totaltarif)
