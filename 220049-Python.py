def diagnosis(daun_menguning, bercak_hitam, daun_berlubang, tanaman_layu):
    if daun_menguning and tanaman_layu and bercak_hitam:
        return "Jamur Antraknosa"
    elif daun_menguning and tanaman_layu:
        return "Hama Kutu Putih"
    elif bercak_hitam and daun_menguning:
        return "Penyakit Hawar Daun"
    elif daun_berlubang:
        return "Hama Ulat Grayak"
    else:
        return "Tidak terdeteksi"

def input_gejala(pertanyaan):
    while True:
        jawaban = input(pertanyaan + " (y/n): ").lower()
        if jawaban in ('y', 'n'):
            return jawaban == 'y'
        else:
            print("Input tidak valid, masukkan 'y' atau 'n' saja!")

def tampilkan_menu():
    print("="*40)
    print("     Sistem Diagnosa Hama Tanaman")
    print("="*40)
    print("\nDaftar Gejala:")
    print("1. Daun menguning")
    print("2. Terdapat bercak hitam")
    print("3. Daun berlubang")
    print("4. Tanaman layu")
    
    print("\nKemungkinan Hama/Penyakit:")
    print("- Hama Kutu Putih")
    print("- Penyakit Hawar Daun")
    print("- Hama Ulat Grayak")
    print("- Jamur Antraknosa")
    print("="*40)

def main():
    tampilkan_menu()

    print("\nSilakan jawab pertanyaan berikut:")
    daun_menguning = input_gejala("Apakah daun menguning?")
    bercak_hitam = input_gejala("Apakah terdapat bercak hitam?")
    daun_berlubang = input_gejala("Apakah daun berlubang?")
    tanaman_layu = input_gejala("Apakah tanaman layu?")

    hasil = diagnosis(daun_menguning, bercak_hitam, daun_berlubang, tanaman_layu)
    print("\nHasil Diagnosa:")
    print(f"--> {hasil}")

if __name__ == "__main__":
    main()
