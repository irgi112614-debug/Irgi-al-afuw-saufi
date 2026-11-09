nama = input("Masukkan nama mahasiswa: ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama tidak ditemukan!")
    target = None

if target is not None:
    print("Target nilai:", target)

    percobaan = 1
    lulus = False

    while percobaan <= 3:
        nilai = int(input("Masukkan nilai ujian ke-" + str(percobaan) + ": "))

        if nilai >= target:
            lulus = True
            break
        else:
            print("Nilai belum mencapai target, silakan coba lagi.")
            percobaan += 1

    if lulus:
        print(nama, "berhasil lulus setelah", percobaan, "percobaan.")
    else:
        print(nama, "tidak lulus setelah 3 percobaan.")