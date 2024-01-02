tempo_em_meses = 160 #meses
tempo_em_anos = int(tempo_em_meses / 12) # int significa mostrar apenas o numero inteiro do numero.

print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses") # % significa os numeros sobrados da divisão, por exemplo o 10 / 3, o % mostra apenas o número que sobrou, que é o 1.


numero = 123.60
print(round(numero)) # O round apenas arredonda um numero que não seja int.

numero_total = 192_898_709 # o underline serve para separar os numeros e letras, facilitando a visiblidade do código
