import lotteri
import os
lotteriet = lotteri.Lotteri()

looping = True

while looping:

    os.system('cls' if os.name == "nt" else "clear")
    antal_lotter = input("\n\t\thur många lotter vill du ha? max 3!")

    try:
        int_antal_lotter = int(antal_lotter)
        i = 0
        print("Kör")

        if (int_antal_lotter < 4):
            print("kör")
            os.system('cls' if os.name == "nt" else "clear")
            print("\n\t\tgrattis du van")

            while i < int_antal_lotter:
                vinst = lotteriet.get_vinst()
                print("\t\t" + vinst)
                i +=1

        elif(int_antal_lotter > 3):
            print("\n\t\tdu har valt för många lotter!")
        
    except ValueError:
        print("\n\t\terror")


    print("------------------------")
    spela_igen = input("\n\t\tvill du spela igen? j/n ")
    if (spela_igen == "n"):
        break