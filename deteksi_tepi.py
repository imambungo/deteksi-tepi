from PIL import Image


def deteksi_tepi(citra_A, citra_hasil, abuabu):
    batas_perbedaan = 3
    penjelasan_tepi = 0
    temp = 25

    citra = Image.open(citra_A)
    pixel = citra.load()

    ukuran_horizontal = citra.size[0]
    ukuran_vertikal = citra.size[1]

    citra_baru = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
    pixel_baru = citra_baru.load()

    progress = 0
    for x in range(ukuran_horizontal-1):
        for y in range(ukuran_vertikal-1):
            new_progress = round((x+1) * 100 / (ukuran_horizontal-1))
            if progress != new_progress:
                progress = new_progress
                print(progress, '%', sep='')
                print
            # print(round((x+1) * 100 / (ukuran_horizontal-1)), '%', sep='')
            # print
            grayscale = abuabu
            terapkan_signifikansi = True

            # kiri-kanan

            perbedaan = beda(pixel[x, y], pixel[x+1, y], batas_perbedaan)
            if perbedaan > batas_perbedaan:
                if terapkan_signifikansi:
                    signifikansi = perbedaan - batas_perbedaan
                    R = round(pixel[x, y][0] * signifikansi / temp)
                    G = round(pixel[x, y][1] * signifikansi / temp)
                    B = round(pixel[x, y][2] * signifikansi / temp)
                else:
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
            perbedaan = beda(pixel[x, y], pixel[x, y+1], batas_perbedaan)
            if perbedaan > batas_perbedaan:
                if terapkan_signifikansi:
                    signifikansi = perbedaan - batas_perbedaan
                    R = round(pixel[x, y][0] * signifikansi / temp)
                    G = round(pixel[x, y][1] * signifikansi / temp)
                    B = round(pixel[x, y][2] * signifikansi / temp)
                else:
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
            perbedaan = beda(pixel[x, y], pixel[x+1, y+1], batas_perbedaan)
            if perbedaan > batas_perbedaan:
                if terapkan_signifikansi:
                    signifikansi = perbedaan - batas_perbedaan
                    R = round(pixel[x, y][0] * signifikansi / temp)
                    G = round(pixel[x, y][1] * signifikansi / temp)
                    B = round(pixel[x, y][2] * signifikansi / temp)
                else:
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
            if x > 0:
                perbedaan = beda(pixel[x, y], pixel[x-1, y+1], batas_perbedaan)
                if perbedaan > batas_perbedaan:
                    if terapkan_signifikansi:
                        signifikansi = perbedaan - batas_perbedaan
                        R = round(pixel[x, y][0] * signifikansi / temp)
                        G = round(pixel[x, y][1] * signifikansi / temp)
                        B = round(pixel[x, y][2] * signifikansi / temp)
                    else:
                        R = pixel[x, y][0]
                        G = pixel[x, y][1]
                        B = pixel[x, y][2]

                    if grayscale:
                        rata_rata = round((R + G + B) / 3)
                        R = rata_rata
                        G = rata_rata
                        B = rata_rata

                    pixel_baru[x-1, y+1] = (R+penjelasan_tepi,
                                            G+penjelasan_tepi,
                                            B+penjelasan_tepi)

    citra_baru.save(citra_hasil)


def beda(titik_a, titik_b, batas_perbedaan):
    beda_r = abs(titik_a[0] - titik_b[0])
    beda_g = abs(titik_a[1] - titik_b[1])
    beda_b = abs(titik_a[2] - titik_b[2])
    # rata_rata_beda = (beda_r + beda_g + beda_b) / 3
    beda_terbesar = max(beda_r, beda_g, beda_b)

    # return round(rata_rata_beda)
    return round(beda_terbesar)


def clipping(intensitas):
    if intensitas > 255:
        return 255


deteksi_tepi('burger.jpg', 'burger_tepi_grayscale.jpg', True)
deteksi_tepi('burger.jpg', 'burger_tepi.jpg', False)
deteksi_tepi('cafe.jpg', 'cafe_tepi_grayscale.jpg', True)
deteksi_tepi('cafe.jpg', 'cafe_tepi.jpg', False)
