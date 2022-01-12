producten = {}


def load_list():
    lijst = open('producten.txt', 'r')
    for line in lijst:
       key, val = line.split()
       producten[key] = val
    lijst.close()
    return producten


def update_list():
    to_print = ''''''
    lijst = open('producten.txt', 'w+')
    for key, value in producten.items():
        to_print = to_print + key + " " + value + "\n"
    lijst.write(to_print)
    lijst.close()


def menu():
    print('''Boodschappen
Opties:
1: Bekijk alle producten,
2: Voeg een product toe,
3: Verwijder een product,
4: Wijzig een product,
5: Boodschappen doen,
6: Sla producten op.
quit: om te eindigen''')


def program(producten):
    running = True
    menu()

    while running:
        optie = input("Kies een optie: ")
        if optie == "1":
            for product, prijs in producten.items():
                print(product + " " + str(prijs))

        elif optie == "2":
            nieuw_product = input("Nieuw product: ")
            nieuw_product_prijs = input("Prijs: ")
            producten[nieuw_product] = nieuw_product_prijs

        elif optie == "3":
            verwijder_product = input("Wat wilt u verwijderen? ")
            del producten[verwijder_product]

        elif optie == "4":
            wijzig_product = input("Welke product wilt u wijzigen: ")
            gewijzigde_product = input("Nieuwe versie: ")
            nieuw_prijs = input("Nieuwe prijs: ")
            del producten[wijzig_product]
            producten[gewijzigde_product] = nieuw_prijs

        elif optie == "5":
            koop_lijst = []

            stop = False
            print("Wat wilt u kopen? (stop als u klaar bent)")

            while not stop:

                product_lijst = input()

                if product_lijst.lower() == "stop":
                    stop = True
                else:
                    koop_lijst.append(product_lijst)

            te_betalen = 0

            for i in koop_lijst:
                te_betalen += int(producten[i])
            print("Te betalen: ", te_betalen)

        elif optie == "6":
            update_list()
            print("Gedaan")

        elif optie.lower() == "quit":
            running = False


program(load_list())
