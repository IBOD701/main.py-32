class Mototsikl:
    def __init__(self, brend, model, ot_kuchi):
        self.brend = brend
        self.model = model
        self.ot_kuchi = ot_kuchi

    def malumot_ber(self):
        print(f"Moto: {self.brend} {self.model}, Quvvati: {self.ot_kuchi} ot kuchi.")

    def gazini_bos(self):
        print(f"Vrumm! {self.brend} {self.model} shiddat bilan tezlashmoqda!")


moto1 = Mototsikl("Kawasaki", "Ninja H2R", 310)
moto2 = Mototsikl("Kawasaki", "Ninja 400", 45)

moto1.malumot_ber()
moto1.gazini_bos()

print("-" * 35)

moto2.malumot_ber()
moto2.gazini_bos()