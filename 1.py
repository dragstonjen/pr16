class Knyha:
    def __init__(self, nazva, avtor):
        self.nazva = nazva
        self.avtor = avtor

class VyvidKnyhy:
    def pokazaty(self, knyha: Knyha):
        print(f"{knyha.nazva} — {knyha.avtor}")

class ZberigachKnyhy:
    def zberehty_u_făl(self, knyha: Knyha, imya_fajlu):
        with open(imya_fajlu, "w") as f:
            f.write(f"{knyha.nazva},{knyha.avtor}")

# Приклад використання
if __name__ == "__main__":
    knyha = Knyha("1984", "Джордж Орвелл")
    VyvidKnyhy().pokazaty(knyha)
    ZberigachKnyhy().zberehty_u_făl(knyha, "knyha.txt")
