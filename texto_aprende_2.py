email = "EmAIL.FALSO@gmail.com"

print(email.lower()) # O lower serve para deixar as letras da variavel minusculas.
print(email.find("@")) # o find encontra a posição do numero/letra da sua variavel, se a letra ou  numero não haver na variavel, ele reponderá como -1.
print(email[13]) # o [] mostra a letra/numero da sua variavel de acordo com a posição que voce coloca no [].

posicao = email.find("@")
print(posicao)
servidor = email[posicao:] # O : mostra o resto da variavel diante da posição
print(servidor)

servidor = email[posicao+1:] # O + seleciona uma letra/numero a menos no codigo