
import time
import multiprocessing
import os


def cek_prima(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def cari_prima_rentang(rentang):
    awal, akhir = rentang
    hasil = []

    for angka in range(awal, akhir + 1):
        if cek_prima(angka):
            hasil.append(angka)

    return hasil


if __name__ == "__main__":
    batas = 5000000

    jumlah_proses = os.cpu_count()
    jumlah_proses = min(jumlah_proses, 4)

    ukuran_bagian = batas // jumlah_proses

    rentang = []

    for i in range(jumlah_proses):
        awal = i * ukuran_bagian + 1

        if i == jumlah_proses - 1:
            akhir = batas
        else:
            akhir = (i + 1) * ukuran_bagian

        rentang.append((awal, akhir))

    mulai = time.time()

    with multiprocessing.Pool(processes=jumlah_proses) as pool:
        hasil_bagian = pool.map(cari_prima_rentang, rentang)

    hasil = []

    for bagian in hasil_bagian:
        hasil.extend(bagian)

    selesai = time.time()

    print("=== PROGRAM BILANGAN PRIMA PARALEL ===")
    print("Batas pencarian:", batas)
    print("Jumlah proses:", jumlah_proses)
    print("Jumlah bilangan prima:", len(hasil))
    print("Waktu eksekusi:", selesai - mulai, "detik")
