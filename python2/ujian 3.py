# Program Menghitung Tarif Parkir Terminal

def hitung_biaya_terminal(durasi):
    biaya_awal = 3000  # Biaya 2 jam pertama
    tambahan_per_jam = 1000  # Biaya tambahan per jam
    denda = 5000  # Biaya denda jika melebihi 10 jam

    # Biaya 2 jam pertama
    total_biaya = biaya_awal

    # Tambahkan biaya jika lebih dari 2 jam
    if durasi > 2:
        tambahan_jam = durasi - 2
        total_biaya += tambahan_jam * tambahan_per_jam

    # Tambahkan denda jika durasi > 10 jam
    if durasi > 10:
        total_biaya += denda

    return total_biaya

# Program utama dengan perulangan
while True:
    print("\n=== Program Menghitung Tarif Parkir Terminal ===")
    try:
        durasi = int(input("Masukkan durasi parkir (jam): "))

        # Hitung biaya parkir
        total_biaya = hitung_biaya_terminal(durasi)
        print(f"Total biaya parkir selama {durasi} jam adalah: Rp{total_biaya}")

        # Tanya apakah ingin mengulang
        ulang = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
        if ulang.lower() != "ya":
            print("Terima kasih telah menggunakan program ini!")
            break

    except ValueError:
        print("Input tidak valid! Harap masukkan angka untuk durasi parkir.")



Soal 3
