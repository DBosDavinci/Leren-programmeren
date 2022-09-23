iphone = int(input("Hoe duur is de iPhone?\n"))
samsung = int(input("Hoe duur is de Samsung?\n"))
teduur = "Het advies is dus geen telefoon te kopen, ze zijn te duur."

if (iphone - samsung - 50) > 0:
    print(f"De Samsung is het goedkoopst, de telefoon kost {samsung} Euro")
    print(f"De iPhone is het duurst, de telefoon kost {iphone} Euro")
    if iphone and samsung > 900:
        print(teduur)
    else:
        print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {iphone - samsung} Euro goedkoper dan de iPhone")
    

elif (iphone - samsung - 50) < 0:
    if (iphone - samsung) > 0:
        print(f"De Samsung is het goedkoopst, de telefoon kost {samsung} Euro")
        print(f"De iPhone is het duurst, de telefoon kost {iphone} Euro")

        if iphone and samsung > 900:
            print(teduur)
        else:
            print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {iphone - samsung} Euro duurder dan de Samsung")
    
    elif (iphone - samsung) < 0:
        print(f"De iPhone is het goedkoopst, de telefoon kost {iphone} Euro")
        print(f"De Samsung is het duurst, de telefoon kost {samsung} Euro")

        if iphone and samsung > 900:
            print(teduur)
        else:
            print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {samsung - iphone} Euro goedkoper dan de Samsung")
    