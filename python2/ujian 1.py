# Program Menghitung Biaya Ekspedisi
def hitung_biaya_pengiriman(berat, panjang, lebar, tinggi):
    biaya_awal = 5000  # Biaya dasar per kilogram
    biaya_tambahan_dimensi = 10000  # Biaya tambahan jika dimensi lebih besar
    biaya_per_kg_tambahan = 1500  # Biaya per kilogram jika dimensi besar

    # Cek dimensi paket
    if panjang <= 50 and lebar <= 50 and tinggi <= 50:
        total_biaya = berat * biaya_awal
    else:
        total_biaya = biaya_tambahan_dimensi + (berat * biaya_per_kg_tambahan)

    return total_biaya

# Program utama dengan perulangan
while True:
    print("\n=== Program Menghitung Biaya Ekspedisi ===")
    try:
        berat = float(input("Masukkan berat paket (kg): "))
        if berat < 1:
            berat = 1  # Minimal 1 kg

        panjang = float(input("Masukkan panjang paket (cm): "))
        lebar = float(input("Masukkan lebar paket (cm): "))
        tinggi = float(input("Masukkan tinggi paket (cm): "))
        # Hitung dan tampilkan biaya
        total_biaya = hitung_biaya_pengiriman(berat, panjang, lebar, tinggi)
        print(f"Total biaya pengiriman adalah: Rp{total_biaya}")
        # Tanya apakah ingin mengulang
        ulang = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
        if ulang.lower() != "ya":
            print("Terima kasih telah menggunakan program ini!")
            break

    except ValueError:
        print("Input tidak valid! Harap masukkan angka yang benar.")