akun = {'12345678' :{'sandi' : '123456', 'saldo' :100000} , #merupakan dictionary yang menyimpan no.rekening, sandi dan saldo
        '11111111' :{'sandi' : '121212', 'saldo':50000}}

def login(): #fungsi untuk melakukan login
    no_rekening = input("Masukkan nomor rekening :")
    if no_rekening in akun: #ngecek, apakah nomor rekening yang dimasukkan ada di dalam dictionary
        sandi = input("Masukkan sandi : ")
        if akun[no_rekening]['sandi'] == sandi: #ngecek, apakah sandi yang dimasukkan benar
            print("Anda berhasil login")
            return no_rekening
        else:
            print("Sandi salah!. Ulangi proses login!")
            return login() #jika sandi salah, mengembalikkan fungsi login
    else:
        print("Nomor rekening tidak ditemukan")
        return login() #jika nomor rekening tidak ada, akan mengembalikan fungsi login

def  tarik_tunai(no_rekening): #fungsi tarik tunai dengan memasukkan parameter nomor rekening
    tarik = int(input("Masukkan nominal: Rp."))
    if tarik > akun[no_rekening]['saldo']: 
        print("Saldo tidak cukup")
    else:
        akun[no_rekening]['saldo'] -= tarik
        print("Transaksi Sukses")
        print("Saldo Anda sekarang adalah: Rp.", akun[no_rekening]['saldo'])

def setor_tunai(no_rekening): #fungsi setor tunai
    setor = int(input("Masukkan nominal: Rp."))
    akun[no_rekening]['saldo'] += setor
    print("Transaksi Sukses")
    print("Saldo Anda sekarang adalah: Rp.", akun[no_rekening]['saldo'])


def main(): #fungsi utama dari program
    no_rekening = login() 
    if no_rekening: 
        while True:
            print ("Selamat datang di ATM")
            print ("Menu Yang Tersedia")
            print ("1. tarik tunai")
            print ("2. setor tunai")
            print ("3. cek saldo")

            pilihan = input("Silakan pilih menu: ")


        
            if pilihan == "1":
                tarik_tunai(no_rekening)
            elif pilihan == "2":
                setor_tunai(no_rekening)
            elif pilihan == "3":
                print("Transaksi Sukses")
                print("Saldo anda saat ini: Rp.", akun[no_rekening]['saldo'])
            else:
                print("Maaf, menu tidak tersedia")

            jawaban = input("Apakah ingin melakukan transaksi lagi?(y/n) ").lower()
            
            if jawaban == "y":
                login()
            else:
                break
        print("Terima Kasih atas kunjungannya")

main() #manggil fungsi utama agar program dapat dijalankan









    
