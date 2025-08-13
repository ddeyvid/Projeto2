# Questão 1
print(f"Olá, {input('Qual o seu nome? ')}!")

# %%
# Questão 2
print(f"Nome: {input('Qual o seu nome? ')}, Idade: {int(input('Qual a sua idade? '))}")

# %%
# Questão 3
print(f"Você está matriculado no curso {input('Qual o nome do curso? ')}.")

# %%
# Questão 4
print(f"Soma: {float(input('Número 1: ')) + float(input('Número 2: '))}")

# %%
# Questão 5
print(f"Subtração: {float(input('Número 1: ')) - float(input('Número 2: '))}")

# %%
# Questão 6
print(f"Multiplicação: {float(input('Número 1: ')) * float(input('Número 2: '))}")

# %%
# Questão 7
n1=float(input("Dividendo:")); n2=float(input("Divisor:")); print("Erro: Divisão por zero." if n2 == 0 else f"Divisão: {n1/n2}")

# %%
# Questão 8
print(f'Dobro: {float(input("Número: ")) * 2}')

# %%
# Questão 9
print(f'Quadrado: {float(input("Número: ")) ** 2}')

# %%
# Questão 10
print(f"Resto da divisão por 3: {float(input('Número: ')) % 3}")

# %%
# Questão 11
print("Maior de idade." if int(input("Qual a sua idade? ")) >= 18 else "Menor de idade.")

# %%
# Questão 12
n=float(input("Número: ")); print("Positivo" if n > 0 else "Negativo" if n < 0 else "Zero")

# %%
# Questão 13
n1=float(input("Nota 1: ")); n2=float(input("Nota 2: ")); print(f"Aprovado com média {(n1+n2)/2:.1f}" if (n1+n2)/2 >= 7 else f"Reprovado com média {(n1+n2)/2:.1f}")

# %%
# Questão 14
print("Par" if int(input("Número: ")) % 2 == 0 else "Ímpar")

# %%
# Questão 15
ano=int(input("Ano: ")); print("Bissexto" if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else "Não Bissexto")

# %%
# Questão 16
print("Acesso concedido." if input("Senha: ") == '1234' else "Acesso negado.")

# %%
# Questão 17
print("O nome é Carlos." if input("Nome: ").strip().lower() == 'carlos' else "O nome não é Carlos.")

# %%
# Questão 18
print(f"O maior é: {max(float(input('N1: ')), float(input('N2: ')), float(input('N3: ')))}")

# %%
# Questão 19
print(f"O menor é: {min(float(input('N1: ')), float(input('N2: ')), float(input('N3: ')))}")

# %%
# Questão 20
idade=int(input("Idade: ")); print("Infantil" if idade < 12 else "Juvenil" if idade < 18 else "Adulto")

# %%
# Questão 21
print(*range(1, 11), sep='\n')

# %%
# Questão 22
print(*range(0, 21, 2), sep='\n')

# %%
# Questão 23
print(*range(1, 21, 2), sep='\n')

# %%
# Questão 24
n=int(input("Tabuada do: ")); print([f'{n} x {i} = {n*i}' for i in range(1, 11)], sep='\n')

# %%
# Questão 25
print(f"Soma: {sum([float(input(f'N{i+1}: ')) for i in range(5)])}")

# %%
# Questão 26
numeros = [float(input(f'N{i+1}: ')) for i in range(5)]; print(f"Média: {sum(numeros)/len(numeros)}")

# %%
# Questão 27
import math; print(f"Fatorial: {math.factorial(int(input('Número: ')))}")

# %%
# Questão 28
print("Nomes digitados:\n" + "\n".join([input(f"Nome {i+1}: ") for i in range(5)]))

# %%
# Questão 29
print(f"Maior idade: {max([int(input(f'Idade {i+1}: ')) for i in range(5)])}")

# %%
# Questão 30
print(f"Soma: {sum(iter(lambda: int(input('N (0 para sair): ')), 0))}")

# %%
# Questão 31
print(*["Desenvolvimento de Sistemas", "Mecatrônica", "Eletrotécnica", "Automação", "Redes"], sep='\n')

# %%
# Questão 32
cursos = ["Mecatrônica", "Eletrotécnica"]; cursos.append("Segurança do Trabalho"); print(cursos)

# %%
# Questão 33
print([input(f"Nome {i+1}: ") for i in range(3)])

# %%
# Questão 34
print(f"Média: {sum([int(input(f'Idade {i+1}: ')) for i in range(3)])/3:.1f}")

# %%
# Questão 35
print({'nome': 'Ana Silva', 'idade': 22, 'curso': 'Sistemas'})

# %%
# Questão 36
aluno={'nome': 'Ana', 'idade': 22}; aluno.update({'nota': 9.5}); print(aluno)

# %%
# Questão 37
print(f"Palavras: {len(input('Frase: ').split())}")

# %%
# Questão 38
print(f"Vogais: {sum(1 for c in input('Frase: ').lower() if c in 'aeiou')}")

# %%
# Questão 39
print("Começa com 'A'" if input("Nome: ").strip().upper().startswith('A') else "Não começa com 'A'")

# %%
# Questão 40
print(input("Nome: ").upper())

# %%
# Questão 41
print(f"Dobro: {float(input('Número: ')) * 2}")

# %%
# Questão 42
print(f"Soma: {float(input('N1: ')) + float(input('N2: '))}")

# %%
# Questão 43
print(f"Média: {(lambda l: sum(l)/len(l) if l else 0)([10, 20, 30, 40, 50])}")

# %%
# Questão 44
print(f"Olá, {input('Nome: ')}! Bem-vindo(a).")

# %%
# Questão 45
print(f"Mais curto: {min(['Ana', 'Carlos', 'Bia', 'Alexandre'], key=len)}")

# %%
# Questão 46
print("Aprovado" if (float(input("N1: "))+float(input("N2: ")))/2 >= 7 else "Reprovado")

# %%
# Questão 47
print(f"É par? {int(input('Número: ')) % 2 == 0}")

# %%
# Questão 48
[print(f"{k.title()}: {v}") for k,v in {'nome':'Ricardo','idade':35,'curso':'Mecatrônica'}.items()]

# %%
# Questão 49
print([i for i in range(1, 11) if i % 2 == 0])

# %%
def q50():
    while (op := input("\n1-Média\n2-Aprovados\n3-Sair\nOpção: ")) != '3':
        if op == '1': print(">>> Média: 8.2")
        elif op == '2': print(">>> Aprovados: Ana, Carlos")
        else: print("Inválido.")
    print("Saindo...")
q50()