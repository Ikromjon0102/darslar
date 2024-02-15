class Shaxs:
    def __init__(self, ism, fam, manzil, yosh):
        self.name = ism
        self.sname = fam
        self.adress = manzil
        self.age = yosh

    def get_name(self):
        return self.name
    def get_tyil(self):
        hy = 2024
        ty = hy - self.age
        return f"Bu shaxs {ty}-yilda tavallud topgan"

person1 = Shaxs('Alijon', 'Valiyev', 'Namanan', 14)
# print(person1.name)
shaxs = Shaxs('Hakimjon','Salimov','Andijon', 16)
# print(shaxs.name)

print(shaxs.get_tyil())
print(person1.get_tyil())










