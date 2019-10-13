from PIL import Image


def deteksi_tepi(citra_A, citra_hasil):
    batas_intensitas = 22
    penjelasan_tepi = 0

    citra = Image.open(citra_A)
    pixel = citra.load()

    ukuran_horizontal = citra.size[0]
    ukuran_vertikal = citra.size[1]

    citra_baru = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    pixel_baru = citra_baru.load()

    for x in range(ukuran_horizontal-1):
        for y in range(ukuran_vertikal-1):
            print(round((x+1) * 100 / (ukuran_horizontal-1)))
            grayscale = False

            # kiri-kanan
            if beda_jauh(pixel[x, y], pixel[x+1, y], batas_intensitas):
                R = pixel[x, y][0]
                G = pixel[x, y][1]
                B = pixel[x, y][2]

                if grayscale:
                    rata_rata = round((R + G + B) / 3)
                    R = rata_rata
                    G = rata_rata
                    B = rata_rata

                pixel_baru[x+1, y] = (R+penjelasan_tepi, G+penjelasan_tepi,
                                      B+penjelasan_tepi)
            # atas-bawah
            if beda_jauh(pixel[x, y], pixel[x, y+1], batas_intensitas):
                R = pixel[x, y][0]
                G = pixel[x, y][1]
                B = pixel[x, y][2]

                if grayscale:
                    rata_rata = round((R + G + B) / 3)
                    R = rata_rata
                    G = rata_rata
                    B = rata_rata

                pixel_baru[x, y+1] = (R+penjelasan_tepi, G+penjelasan_tepi,
                                      B+penjelasan_tepi)
            # serong kiri
            if beda_jauh(pixel[x, y], pixel[x+1, y+1], batas_intensitas):
                R = pixel[x, y][0]
                G = pixel[x, y][1]
                B = pixel[x, y][2]

                if grayscale:
                    rata_rata = round((R + G + B) / 3)
                    R = rata_rata
                    G = rata_rata
                    B = rata_rata

                pixel_baru[x+1, y+1] = (R+penjelasan_tepi, G+penjelasan_tepi,
                                        B+penjelasan_tepi)
            # serong kanan
            if x > 0 and beda_jauh(pixel[x, y], pixel[x+1, y+1], batas_intensitas):
                R = pixel[x, y][0]
                G = pixel[x, y][1]
                B = pixel[x, y][2]

                if grayscale:
                    rata_rata = round((R + G + B) / 3)
                    R = rata_rata
                    G = rata_rata
                    B = rata_rata

                pixel_baru[x+1, y+1] = (R+penjelasan_tepi, G+penjelasan_tepi,
                                        B+penjelasan_tepi)

    citra_baru.save(citra_hasil)


def beda_jauh(titik_a, titik_b, batas_intensitas):
    beda_r = abs(titik_a[0] - titik_b[0])
    beda_g = abs(titik_a[1] - titik_b[1])
    beda_b = abs(titik_a[2] - titik_b[2])
    rata_rata_beda = (beda_r + beda_g + beda_b) / 3

    if rata_rata_beda > batas_intensitas:
        return True
    return False


def clipping(intensitas):
    if intensitas > 255:
        return 255


deteksi_tepi('gambar.jpg', 'gambar_hasil_deteksi_tepi.jpg')
