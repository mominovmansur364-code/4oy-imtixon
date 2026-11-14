xizmatlar = {
    "diagnostika": 50000,
    "tozalash": 80000,
    "sozlash": 40000,
    "almashtirish": 120000,
}


def hisobla(*args, **kwargs):
    mijoz = kwargs.get("mijoz", "Noma'lum")
    chegirma_foiz = kwargs.get("chegirma", 0)

    jami = 0
    for xizmat in args:
        if xizmat in xizmatlar:
            jami += xizmatlar[xizmat]
        else:
            print(f"Ogohlantirish: {'xizmat'} xizmati ro'yxatda mavjud emas!")


    chegirma_summa = jami * chegirma_foiz / 100
    tolov = jami - chegirma_summa

    print(f"Mijoz: {mijoz}")
    print(f"Xizmatlar jami: {int(jami)} so'm")
    print(f"Chegirma: {int(chegirma_summa)} so'm")
    print(f"To'lov: {int(tolov)} so'm")

hisobla("diagnostika", "tozalash", "sozlash", mijoz="Nodira", chegirma=10)