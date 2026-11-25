
import time

def cek_prima(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def cari_bilangan_prima(batas):
    hasil = []

    for angka in range(2, batas + 1):
        if cek_prima(angka):
            hasil.append(angka)

    return hasil


if __name__ == "__main__":
    batas = 5000000

    mulai = time.time()

    hasil = cari_bilangan_prima(batas)

    selesai = time.time()

    print("=== PROGRAM BILANGAN PRIMA SERIAL ===")
    print("Batas pencarian:", batas)
    print("Jumlah bilangan prima:", len(hasil))
    print("Waktu eksekusi:", selesai - mulai, "detik")
