from abc import ABC, abstractmethod

class Spovishchuvach(ABC):
    @abstractmethod
    def spovistyty(self, povidomlennia: str):
        pass

class EmailSpovishchuvach(Spovishchuvach):
    def spovistyty(self, povidomlennia: str):
        print(f"Email: {povidomlennia}")

class SMSspovishchuvach(Spovishchuvach):
    def spovistyty(self, povidomlennia: str):
        print(f"SMS: {povidomlennia}")

class PushSpovishchuvach(Spovishchuvach):
    def spovistyty(self, povidomlennia: str):
        print(f"Push: {povidomlennia}")

class SluzhbaSpovishchen:
    def __init__(self, spovishchuvach: Spovishchuvach):
        self.spovishchuvach = spovishchuvach

    def spovistyty_pro_podiiu(self, povidomlennia: str):
        self.spovishchuvach.spovistyty(povidomlennia)

# Приклад використання
if __name__ == "__main__":
    sluzhba = SluzhbaSpovishchen(EmailSpovishchuvach())
    sluzhba.spovistyty_pro_podiiu("Сервер не відповідає!")

    sluzhba = SluzhbaSpovishchen(PushSpovishchuvach())
    sluzhba.spovistyty_pro_podiiu("Ви отримали нове повідомлення.")
