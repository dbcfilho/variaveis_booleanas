myCard = int(input("Enter your credit card number "))
cartãoLido = 1
foundMyCard = False

while cardRead !=0 and not foundMyCard:
    cardRead = int(input("Enter your next credit card number: "))
    if cardRead == myCard:
        foundMyCard = True

if foundMyCard:
    print("Card found")
else:
    print("Card not found")