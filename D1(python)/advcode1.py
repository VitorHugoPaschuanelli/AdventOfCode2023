#Função para procurar números
#Separa os elementos da linha em lista, verificando cada um se é um dígito. Caso sim, retorna para uma string.
def find_numbers(line):
    numbers = ""
    for letter in line:
        if letter.isdigit():
            numbers += letter
    return numbers

total_sum = 0 #Total


#Abre o arquivo onde se encontra o input, chamando a função para encontrar os números em cada linha, sendo retornado
#um vetor com todos os números, o primeiro e o último são escolhidos para o cálculo, verificando se são iguais ou não.
archive = open('ADVCODE23/D1/input.txt', 'r')
document = archive.readlines()
archive.close()

for line in document:
    nums = find_numbers(line)
    if nums:
        first = nums [0]
        last = nums[-1]
        if first != last:
            number = first + last
            print(number)
            total_sum += int(number) 
        else: 
            number = first + first
            print(number)
            total_sum += int(number)
print("Total sum:", total_sum)
