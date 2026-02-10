print ("PARTE 1")

resistencia = float (input ("\nDigite a Resistência (Ohms): "))
corrente = float (input ("Digite a Corrente (Ampéres): "))

tensao = resistencia * corrente

print ("\n----------------------------------------")
print (f"\nA Tensão necessária é: {tensao:.1f} Volts")
print ("\n----------------------------------------")





print ("\n\n\nPARTE 2")

resistencia = float (input ("\nDigite a Resistência (Ohms): "))
corrente = float (input ("Digite a Corrente (Ampéres): "))

tensao = resistencia * corrente
potencia = corrente * tensao

print ("\n----------------------------------------")
print (f"\nTensão:  {tensao:.1f} Volts")
print (f"\nPotência:  {potencia:.1f} Watts")
print ("\n----------------------------------------")





print ("\n\n\nPARTE 3")

potencia = float (input ("\nPotência do Equipamento (Watts): "))
tensao = float (input ("Tensão da Rede (Volts): "))

corrente = potencia / tensao
corrente_seguranca = corrente * 1.25

print ("\n----------------------------------------")
print (f"\nCorrente Nominal:  {corrente:.2f} Amperes")
print (f"\nCorrente com Segurança (+25%):  {corrente_seguranca:.2f} Amperes")
print ("\nDICA: Use um disjuntor próximo desse valor.")
print ("\n----------------------------------------")