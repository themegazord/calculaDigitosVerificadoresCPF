def dataCalcCPF(s):
    return 11 - (s % 11)


cpf = str(input('Insira o seu CPF sem os números verificadores: '))
validateCpf = ''
somaTotalVerDig2 = 0
somaTotalVerDig1 = 0
c1 = 10
c2 = 11

for i in cpf[0:9]:
    somaTotalVerDig1 += int(i) * c1
    c1-=1

if dataCalcCPF(somaTotalVerDig1) > 9:
    validateCpf += f'{cpf[0:9]}0'
elif dataCalcCPF(somaTotalVerDig1) <= 9:
    validateCpf += f'{cpf[0:9]}{dataCalcCPF(somaTotalVerDig1)}'


for i in validateCpf:
    somaTotalVerDig2 += int(i) * c2
    c2-=1

if dataCalcCPF(somaTotalVerDig2) > 9:
    validateCpf += f'0'
elif dataCalcCPF(somaTotalVerDig2) <= 9:
    validateCpf += f'{dataCalcCPF(somaTotalVerDig2)}'

print(validateCpf)

