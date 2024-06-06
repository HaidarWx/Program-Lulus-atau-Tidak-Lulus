print("☆☆PROGRAM LULUS/TIDAK LULUS SISWA/SISWI SMA ANNAJAH☆☆")
print("                   ☆☆☆☆☆☆☆☆☆☆                      ")
#mapel
nama = input("Masukan Nama Siswa : ")
pai = float(input("Masukan Nilai Akhir Pendidikan Agama Islam : "))
pkn = float(input("Masukan Nilai Akhir Pendidikan Pancasila dan Kewarganegaraan : "))
bindo = float(input("Masukan Nilai Akhir Bahasa Indonesia : "))
mtkmin = float(input("Masukan Nilai Akhir Matematika Minat : "))
mtkwib = float(input("Masukan Nilai Akhir Matematika Wajib : "))
fisika = float(input("Masukan Nilai Akhir Fisika"))
kimia = float(input("Masukan Nilai Akhir Kimia : "))
geografi = float(input("Masukan Nilai Akhir Geografi : "))
bing = float(input("Masukan Nilai Akhir Bahasa Inggris :"))
barb = float(input("Masukan Nilai Akhir Bahasa Arab:"))
pjok = float(input("Masukan Nilai Akhir Penjaskes : "))
it = float(input("Masukan Nilai Akhir Informatika : "))
sjh = float(input("Masukan Nilai Akhir Sejarah : "))
teater = float(input("Masukan Nilai Akhir Seni Teater:"))
fq = float(input("Masukan Nilai Akhir Fiqih : "))
tdt = float(input("Masukan Nilai Akhir Tahsin dan Tahfidz : "))

jNilaiMapel = pai + pkn + bindo + mtkmin + mtkwib + fisika + kimia + geografi + bing + barb + pjok + it + sjh + teater + fq + tdt

nRata = jNilaiMapel / 16

if nRata >= 93:
    
    print("Ananda " + nama + " Dengan Jumlah Nilai " + str(jNilaiMapel) + " dan Nilai Rata-Rata " + str(nRata) + " , Dengan Nilai Tersebut Ananda dinyatakan LULUS dengan Predikat A ")
    
elif nRata >= 85 and nRata < 93 :
        print("Ananda " + nama + " Dengan Jumlah Nilai " + str(jNilaiMapel) + " dan Nilai Rata-Rata " + str(nRata) + " , Dengan Nilai Tersebut Ananda dinyatakan LULUS dengan Predikat B ")
elif nRata >= 74 and nRata < 85 :
        print("Ananda " + nama + " Dengan Jumlah Nilai " + str(jNilaiMapel) + " dan Nilai Rata-Rata " + str(nRata) + " , Dengan Nilai Tersebut Ananda dinyatakan LULUS dengan Predikat C ")
else :
        print("Ananda " + nama + " Dengan Jumlah Nilai " + str(jNilaiMapel) + " dan Nilai Rata-Rata " + str(nRata) + " , Dengan Nilai Tersebut Ananda dinyatakan TIDAK LULUS dengan Predikat D ")


    
   
    

