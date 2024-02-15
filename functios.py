def salomlash():
    print("Assalomu alaykum!")

def salomlash_name(name):
    print(f'Assalomu alaykum! {name} aka')
#
# salomlash_name("Alijon")
# salomlash_name("Valijon")

def about(ism, fam, yosh):
    hyil = 2024
    tyil = hyil - yosh
    text = f"{fam} {ism} {tyil} - yilda tavallud topgan"
    print(text)

about("Alijon", "Valiyev", 15)
about("Karimjon", "Valiyev", 45, "Namangan")


