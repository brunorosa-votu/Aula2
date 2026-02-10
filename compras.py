produtos = ["Arroz", "Macarrão", "Tomate"]

valores = [10, 7, 4.5]

total = valores[0] + valores[1] + valores[2]

print ("\nVocê comprou 3 produtos:")
print ("--------------------------")
print ("Nome              Valor")

i = 0
while i < 3:
    print (f"{produtos[i]}            R${valores[i]:.2f}")
    i += 1

print ("--------------------------")
print (f"Total: R${total:.2f}\n")