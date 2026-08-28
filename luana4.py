temperatura = 28
chovendo = False
print ("---exemplo 4: condicionais com operadores lógicos (and, or, not)---")
print (f"condições atuais -> temperatura: {temperatura} C, chovendo {chovendo}")
if temperatura > 25 and not chovendo:
     print ("sugestão: ótimo dia para ir à praia!")
elif temperatura <15 or chovendo:
     print ("sugestão: que tal um filme em casa?")
else:
     print ("sugestão: o tempo está agradável.")