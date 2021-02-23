nama = ['Farhan','Joko']
telpon = ['08123456789','08987654321']

print('Selamat Datang!')
print(' ')
print('---Menu---')
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
print(' ')
menu_input = int(input("Pilih Menu : "))

def function(menu):
    if menu == 1:
        print("Daftar Kontak")
        print("")
        for daftar_kontak in range(len(nama)):
            print(f"Nama : {nama[daftar_kontak]}")
            print(f"No Telepon : {telpon[daftar_kontak]}")
            print(" ")
    if menu == 2:
        #Input Data
        nama_input = input('Masukkan Nama Anda : ')
        telpon_input = input('Masukkan Nomor Telpon Anda : ')
        #Tambah Data
        nama.append(nama_input)
        telpon.append(telpon_input)
        print('Kontak berhasil ditambahkan')
    if menu == 3:
        print('Program selesai, sampai jumpa!')
    if menu > 3:
        print("Menu Tidak Tersedia")
function(menu_input)