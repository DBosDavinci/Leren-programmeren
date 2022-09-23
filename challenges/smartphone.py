iphone = int(input("Hoe duur is de iPhone?\n"))
samsung = int(input("Hoe duur is de Samsung?\n"))

if samsung > iphone:
    print(f"De Samsung is het duurst, de telefoon kost {samsung} Euro")
    print(f"De iPhone is het goedkoopst, de telefoon kost {iphone} Euro")
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {samsung - iphone} goedkoper dan de Samsung")

elif iphone > samsung:
    print(f"De iPhone is het duurst, de telefoon kost {iphone} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost {samsung} Euro")
    print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {iphone - samsung} Euro goedkoper dan de iPhone")