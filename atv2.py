nome = input("Digite o nome da pessoa")
sexo = input("Digite o sexo da pessoa")
estadocivil = input("Digite o estado civil da pessoa")

if sexo == "F" and estadocivil == "CASADA":
 tempocasamento = int(input("Digite o tempo de casamento em anos: "))
print (f"{nome} está casada há {tempocasamento} anos.")