from time import sleep
sala = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    sala.append([nome, [nota1, nota2], media])
    perg = str(input('Quer continuar? [s/n]: ')).strip().lower()[0]
    if perg in 'Nn':
        break
print('*\033[31m*\033[m' * 12)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-\033[34m-\033[m'*12)
for i, p in enumerate(sala):
    print(f'{i:<4}{p[0]:<10}{p[2]:>8}')
print('-\033[34m-\033[m'*12)
sleep(1.5)
while True:
    esc = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    if esc <= len(sala) - 1:
        print(f'As notas de {sala[esc][0]} são {sala[esc][1]}')
    if esc == 999:
        print('FINALIZANDO...')
        break
print('ESTAMOS A DISPOSIÇÃO')