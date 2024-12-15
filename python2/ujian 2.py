def hitung_biaya_parkir(jenis_kendaraan, durasi):
    if durasi <= 0:
        return "Error: Masukkan durasi yang valid (lebih dari 0)."
    tarif_awal = 3000
    biaya_per_jam = 1000 if jenis_kendaraan == "motor" else 1500 if jenis_kendaraan == "mobil" else None
    if biaya_per_jam is None:
        return "Error: Jenis kendaraan tidak valid."
    return tarif_awal if durasi <= 2 else tarif_awal + (durasi - 2) * biaya_per_jam


try:
    durasi = int(input("Berapa durasi parkir (jam)? "))
    if durasi <= 0:
        print("Error: Masukkan durasi yang valid (lebih dari 0).")
    else:
        jenis_kendaraan = input("Apakah Anda memakai sepeda motor atau mobil? ").strip().lower()
        total_biaya = hitung_biaya_parkir(jenis_kendaraan, durasi)
        print(f"Total biaya parkir: Rp {total_biaya}" if isinstance(total_biaya, int) else total_biaya)
except ValueError:
    print("Error: Masukkan durasi yang valid dalam angka.")