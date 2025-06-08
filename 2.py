from abc import ABC, abstractmethod

class SposibOplaty(ABC):
    @abstractmethod
    def splatyty(self, suma):
        pass

class KreditnaKarta(SposibOplaty):
    def splatyty(self, suma):
        print(f"Сплачено {suma} за допомогою кредитної картки")

class PayPal(SposibOplaty):
    def splatyty(self, suma):
        print(f"Сплачено {suma} через PayPal")

class Kryptovaliuta(SposibOplaty):
    def splatyty(self, suma):
        print(f"Сплачено {suma} криптовалютою")

class ApplePay(SposibOplaty):
    def splatyty(self, suma):
        print(f"Сплачено {suma} через Apple Pay")

def obrobyty_platu(sposib: SposibOplaty, suma):
    sposib.splatyty(suma)

# Приклад використання
if __name__ == "__main__":
    obrobyty_platu(PayPal(), 100)
    obrobyty_platu(Kryptovaliuta(), 50)
    obrobyty_platu(ApplePay(), 75)
