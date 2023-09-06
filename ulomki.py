from fractions import Fraction

def sestej_ulomke():
    print("Program za seštevanje ulomkov")
    stevilo_ulomkov = int(input("Vnesite število ulomkov, ki jih želite sešteti: "))
    
    ulomki = []
    
    for i in range(stevilo_ulomkov):
        while True:
            ulomek = input(f"Vnesite ulomek {i + 1} (števec/imenovalec): ")
            
            try:
                sestavni_delci = ulomek.split('/')
                stevec = int(sestavni_delci[0])
                imenovalec = int(sestavni_delci[1])
                ulomek = Fraction(stevec, imenovalec)
                ulomki.append(ulomek)
                break
            except ValueError:
                print("Napaka: Vnesite veljaven ulomek (števec/imenovalec).")
            except ZeroDivisionError:
                print("Napaka: Imenovalec ne sme biti enak nič.")
    
    if not ulomki:
        print("Niste vnesli nobenih ulomkov.")
        return
    
    vsota = sum(ulomki)
    
    print("\nSeštevek ulomkov:")
    for ulomek in ulomki:
        print(f"{ulomek} +", end=" ")
    print(f"= {vsota}")

if __name__ == "__main__":
    sestej_ulomke()
