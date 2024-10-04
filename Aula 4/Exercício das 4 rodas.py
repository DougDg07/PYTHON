# Faça um programa que pergunte quantas rodas tem um veiculo, se tiver 4 diga que é um carro ou van. 
print("Carro ou Moto!")
rodas = int(input("Quantas rodas tem seu carro:"))

if (rodas == 4):
    print("Sim, é um carro ou van!")
elif (rodas == 2):
    print("O veiculo é uma moto ou bicicleta")
elif (rodas == 1):
    print("É a merda de um monociclo")
elif (rodas == 6):
    print("É um busão")
elif (rodas >= 8 and rodas <= 20):
    print("É um caminhão")
else:
    print("Não foi encontrado um veiculo que corresponde ao número de rodas!")
   
# Quando temos mais de uma condicional, , usaremos o "elif" sintaxe: 
    #If (condição): --> 1° condição
    
    #Elif(condição): --> 2° condição
    #Elif(condição): --> 3° condição
    #Elif(condição): --> 4° condição
    #por ai vai...

    #Else:  --> Ocorre quando nenhuma condição dos elif ou if for atendida  
