#Função para procurar números
#Percorre cada índice da linha procurando pela inicial do número ou pelo mesmo, adicionando-o ao final de um vetor. 
#caso a inicial for encontrada, verifica se o restante da palavra está presente. Incrementado o índice corretamente.
    #vitor.py contém uma variante para a função, feita pelo Fabio.
def find_numbers(line):
    numbers = []
    i = 0
    while i < len(line):
        if line[i] == "o" or line[i] == "1":
            if line[i] == "1":
                numbers.append(1)
            if line[i:i+3] == "one":
                numbers.append(1)
                i += 1
            else:
                i += 1
        elif line[i] == "t" or line[i] == "2":
            if line[i] == "2":
                numbers.append(2)
            if line[i:i+3] == "two":
                numbers.append(2)
                i += 1
            elif line[i:i+5] == "three":
                numbers.append(3)
                i += 1
            else:
                i += 1
        elif line[i] == "t" or line[i] == "3":
            if line[i] == "3":
                numbers.append(3)
                i += 1
        elif line[i] == "f" or line[i] == "4":
            if line[i] == "4":
                numbers.append(4)
            if line[i:i+4] == "four":
                numbers.append(4)
                i += 1
            elif line[i:i+4] == "five":
                numbers.append(5)
                i += 1
            else:
                i += 1
        elif line[i] == "f" or line[i] == "5":
            if line[i] == "5":
                numbers.append(5)
                i += 1
        elif line[i] == "s" or line[i] == "6":
            if line[i] == "6":
                numbers.append(6)
            if line[i:i+3] == "six":
                numbers.append(6)
                i += 1
            elif line[i:i+5] == "seven":
                numbers.append(7)
                i += 1
            else:
                i += 1
        elif line[i] == "s" or line[i] == "7":
            if line[i] == "7":
                numbers.append(7)
                i += 1
        elif line[i] == "e" or line[i] == "8":
            if line[i] == "8":
                numbers.append(8)
            if line[i:i+5] == "eight":
                numbers.append(8)
                i += 1
            else:
                i += 1
        elif line[i] == "n" or line[i] == "9":
            if line[i] == "9":
                numbers.append(9)
            if line[i:i+4] == "nine":
                numbers.append(9)
                i += 1
            else:
                i += 1
        else:
            i += 1
    return numbers

total_sum = 0 #Total

#Abre o arquivo onde se encontra o input, chamando a função para encontrar os números em cada linha, sendo retornado
#um vetor com todos os números, o primeiro e o último são escolhidos para o cálculo, verificando se são iguais ou não.
with open('ADVCODE23/D1/input.txt', 'r') as document:
    for line in document:
        nums = find_numbers(line)
        if nums:
            first = nums[0]
            last = nums[-1]
            if first != last:
                number = first * 10 + last
                print(number)
                total_sum += number
            else: 
                number = first * 11
                print(number)
                total_sum += number
print("Total sum:", total_sum)

