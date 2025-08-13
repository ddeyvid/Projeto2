#%%
def q1():
    nome = input("Qual o Seu Nome?: ")
    print(f"Olá {nome}!")
# %%
# Questão 2
def q2():
    print(f"Nome: {input('Qual o seu nome? ')}, Idade: {int(input('Qual a sua idade? '))}")

# %%
# Questão 3
def q3():
    print(f"Você está matriculado no curso {input('Qual o nome do curso? ')}.")

# %%
# Questão 4
def q4():
    print(f"Soma: {float(input('Número 1: ')) + float(input('Número 2: '))}")

# %%
# Questão 5
def q5():
    print(f"Subtração: {float(input('Número 1: ')) - float(input('Número 2: '))}")

# %%
# Questão 6
def q6():
    print(f"Multiplicação: {float(input('Número 1: ')) * float(input('Número 2: '))}")

# %%
# Questão 7
def q7():
    n1=float(input("Dividendo:")); n2=float(input("Divisor:")); print("Erro: Divisão por zero." if n2 == 0 else f"Divisão: {n1/n2}")

# %%
# Questão 8
def q8():
    print(f'Dobro: {float(input("Número: ")) * 2}')

# %%
# Questão 9
def q9():
    print(f'Quadrado: {float(input("Número: ")) ** 2}')

# %%
# Questão 10
def q10():
    print(f"Resto da divisão por 3: {float(input('Número: ')) % 3}")

# %%
# Questão 11
def q11():
    print("Maior de idade." if int(input("Qual a sua idade? ")) >= 18 else "Menor de idade.")

# %%
# Questão 12
def q12():
    n=float(input("Número: ")); print("Positivo" if n > 0 else "Negativo" if n < 0 else "Zero")

# %%
# Questão 13
def q13():
    n1=float(input("Nota 1: ")); n2=float(input("Nota 2: ")); print(f"Aprovado com média {(n1+n2)/2:.1f}" if (n1+n2)/2 >= 7 else f"Reprovado com média {(n1+n2)/2:.1f}")

# %%
# Questão 14
def q14():
    print("Par" if int(input("Número: ")) % 2 == 0 else "Ímpar")

# %%
# Questão 15
def q15():
    ano=int(input("Ano: ")); print("Bissexto" if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else "Não Bissexto")

# %%
# Questão 16
def q16():
    print("Acesso concedido." if input("Senha: ") == '1234' else "Acesso negado.")

# %%
# Questão 17
def q17():
    print("O nome é Carlos." if input("Nome: ").strip().lower() == 'carlos' else "O nome não é Carlos.")

# %%
# Questão 18
def q18():
    print(f"O maior é: {max(float(input('N1: ')), float(input('N2: ')), float(input('N3: ')))}")

# %%
# Questão 19
def q19():
    print(f"O menor é: {min(float(input('N1: ')), float(input('N2: ')), float(input('N3: ')))}")

# %%
# Questão 20
def q20():
    idade=int(input("Idade: ")); print("Infantil" if idade < 12 else "Juvenil" if idade < 18 else "Adulto")

# %%
# Questão 21
def q21():
    print(*range(1, 11), sep='\n')

# %%
# Questão 22
def q22():
    print(*range(0, 21, 2), sep='\n')

# %%
# Questão 23
def q23():
    print(*range(1, 21, 2), sep='\n')

# %%
# Questão 24
def q24():
    n=int(input("Tabuada do: ")); print([f'{n} x {i} = {n*i}' for i in range(1, 11)], sep='\n')

# %%
# Questão 25
def q25():
    print(f"Soma: {sum([float(input(f'N{i+1}: ')) for i in range(5)])}")

# %%
# Questão 26
def q26():
    numeros = [float(input(f'N{i+1}: ')) for i in range(5)]; print(f"Média: {sum(numeros)/len(numeros)}")

# %%
# Questão 27
def q27():
    factorial = (lambda f: (lambda x: f(f, x)))(lambda f, x: x * f(f, x - 1) if x > 1 else 1); print(f"Fatorial: {factorial(int(input('Número: ')))}")

# %%
# Questão 28
def q28():
    print("Nomes digitados:\n" + "\n".join([input(f"Nome {i+1}: ") for i in range(5)]))

# %%
# Questão 29
def q29():
    print(f"Maior idade: {max([int(input(f'Idade {i+1}: ')) for i in range(5)])}")

# %%
# Questão 30
def q30():
    print(f"Soma: {sum(iter(lambda: int(input('N (0 para sair): ')), 0))}")

# %%
# Questão 31
def q31():
    print(*["Desenvolvimento de Sistemas", "Mecatrônica", "Eletrotécnica", "Automação", "Redes"], sep='\n')

# %%
# Questão 32
def q32():
    cursos = ["Mecatrônica", "Eletrotécnica"]; cursos.append("Segurança do Trabalho"); print(cursos)

# %%
# Questão 33
def q33():
    print([input(f"Nome {i+1}: ") for i in range(3)])

# %%
# Questão 34
def q34():
    print(f"Média: {sum([int(input(f'Idade {i+1}: ')) for i in range(3)])/3:.1f}")

# %%
# Questão 35
def q35():
    print({'nome': 'Ana Silva', 'idade': 22, 'curso': 'Sistemas'})

# %%
# Questão 36
def q36():
    aluno={'nome': 'Ana', 'idade': 22}; aluno.update({'nota': 9.5}); print(aluno)

# %%
# Questão 37
def q37():
    print(f"Palavras: {len(input('Frase: ').split())}")

# %%
# Questão 38
def q38():
    print(f"Vogais: {sum(1 for c in input('Frase: ').lower() if c in 'aeiou')}")

# %%
# Questão 39
def q39():
    print("Começa com 'A'" if input("Nome: ").strip().upper().startswith('A') else "Não começa com 'A'")

# %%
# Questão 40
def q40():
    print(input("Nome: ").upper())

# %%
# Questão 41
def q41():
    print(f"Dobro: {float(input('Número: ')) * 2}")

# %%
# Questão 42
def q42():
    print(f"Soma: {float(input('N1: ')) + float(input('N2: '))}")

# %%
# Questão 43
def q43():
    print(f"Média: {(lambda l: sum(l)/len(l) if l else 0)([10, 20, 30, 40, 50])}")

# %%
# Questão 44
def q44():
    print(f"Olá, {input('Nome: ')}! Bem-vindo(a).")

# %%
# Questão 45
def q45():
    print(f"Mais curto: {min(['Ana', 'Carlos', 'Bia', 'Alexandre'], key=len)}")

# %%
# Questão 46
def q46():
    print("Aprovado" if (float(input("N1: "))+float(input("N2: ")))/2 >= 7 else "Reprovado")

# %%
# Questão 47
def q47():
    print(f"É par? {int(input('Número: ')) % 2 == 0}")

# %%
# Questão 48
def q48():
    [print(f"{k.title()}: {v}") for k,v in {'nome':'Ricardo','idade':35,'curso':'Mecatrônica'}.items()]

# %%
# Questão 49
def q49():
    print([i for i in range(1, 11) if i % 2 == 0])

# %%
def q50():
    while (op := input("\n1-Média\n2-Aprovados\n3-Sair\nOpção: ")) != '3':
        if op == '1': print(">>> Média: 8.2")
        elif op == '2': print(">>> Aprovados: Ana, Carlos")
        else: print("Inválido.")
    print("Saindo...")
q50()

# %%

if __name__ == "__main__":
    # Dicionário que mapeia o número da questão para a função correspondente
    questoes = {
        '1': q1, '2': q2, '3': q3, '4': q4, '5': q5, '6': q6, '7': q7, '8': q8, '9': q9, '10': q10,
        '11': q11, '12': q12, '13': q13, '14': q14, '15': q15, '16': q16, '17': q17, '18': q18, '19': q19, '20': q20,
        '21': q21, '22': q22, '23': q23, '24': q24, '25': q25, '26': q26, '27': q27, '28': q28, '29': q29, '30': q30,
        '31': q31, '32': q32, '33': q33, '34': q34, '35': q35, '36': q36, '37': q37, '38': q38, '39': q39, '40': q40,
        '41': q41, '42': q42, '43': q43, '44': q44, '45': q45, '46': q46, '47': q47, '48': q48, '49': q49, '50': q50,
    }

    while True:
        print("\n" + "="*50)
        num_questao = input("Digite o número da questão que deseja executar (1-50) ou 'sair': ")
        print("="*50 + "\n")

        if num_questao.lower() in ['sair', 'exit', 'q', '0']:
            print("Programa finalizado.")
            break
        
        # Busca a função no dicionário
        funcao_para_executar = questoes.get(num_questao)
        
        if funcao_para_executar:
            print(f"--- Executando Questão {num_questao} ---")
            funcao_para_executar()
            print(f"--- Fim da Questão {num_questao} ---")
        else:
            print("Questão inválida. Por favor, digite um número entre 1 e 50.")