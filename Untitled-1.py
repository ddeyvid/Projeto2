e, fl, rg, pr = input, float, range, print
def q1():
    nome = e("Qual o Seu Nome?: ")
    pr(f"Olá {nome}!")
def q2():
    pr(f"Nome: {e('Qual o seu nome? ')}, Idade: {int(e('Qual a sua idade? '))}")
def q3():
    pr(f"Você está matriculado no curso {e('Qual o nome do curso? ')}.")
def q4():
    pr(f"Soma: {fl(e('Número 1: ')) + fl(e('Número 2: '))}")
def q5():
    pr(f"Subtração: {fl(e('Número 1: ')) - fl(e('Número 2: '))}")
def q6():
    pr(f"Multiplicação: {fl(e('Número 1: ')) * fl(e('Número 2: '))}")
def q7():
    n1=fl(e("Dividendo:")); n2=fl(e("Divisor:")); pr("Erro: Divisão por zero." if n2 == 0 else f"Divisão: {n1/n2}")
def q8():
    pr(f'Dobro: {fl(e("Número: ")) * 2}')
def q9():
    pr(f'Quadrado: {fl(e("Número: ")) ** 2}')
def q10():
    pr(f"Resto da divisão por 3: {fl(e('Número: ')) % 3}")
def q11():
    pr("Maior de idade." if int(e("Qual a sua idade? ")) >= 18 else "Menor de idade.")
def q12():
    n=fl(e("Número: ")); pr("Positivo" if n > 0 else "Negativo" if n < 0 else "Zero")
def q13():
    n1=fl(e("Nota 1: ")); n2=fl(e("Nota 2: ")); pr(f"Aprovado com média {(n1+n2)/2:.1f}" if (n1+n2)/2 >= 7 else f"Reprovado com média {(n1+n2)/2:.1f}")
def q14():
    pr("Par" if int(e("Número: ")) % 2 == 0 else "Ímpar")
def q15():
    ano=int(e("Ano: ")); pr("Bissexto" if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else "Não Bissexto")
def q16():
    pr("Acesso concedido." if e("Senha: ") == '1234' else "Acesso negado.")
def q17():
    pr("O nome é Carlos." if e("Nome: ").strip().lower() == 'carlos' else "O nome não é Carlos.")
def q18():
    pr(f"O maior é: {max(fl(e('N1: ')), fl(e('N2: ')), fl(e('N3: ')))}")
def q19():
    pr(f"O menor é: {min(fl(e('N1: ')), fl(e('N2: ')), fl(e('N3: ')))}")
def q20():
    idade=int(e("Idade: ")); pr("Infantil" if idade < 12 else "Juvenil" if idade < 18 else "Adulto")
def q21():
    pr(*rg(1, 11), sep='\n')
def q22():
    pr(*rg(0, 21, 2), sep='\n')
def q23():
    pr(*rg(1, 21, 2), sep='\n')
def q24():
    n=int(e("Tabuada do: ")); pr([f'{n} x {i} = {n*i}' for i in rg(1, 11)], sep='\n')
def q25():
    pr(f"Soma: {sum([fl(e(f'N{i+1}: ')) for i in rg(5)])}")
def q26():
    numeros = [fl(e(f'N{i+1}: ')) for i in rg(5)]; pr(f"Média: {sum(numeros)/len(numeros)}")
def q27():
    factorial = (lambda f: (lambda x: f(f, x)))(lambda f, x: x * f(f, x - 1) if x > 1 else 1); pr(f"Fatorial: {factorial(int(e('Número: ')))}")
def q28():
    pr("Nomes digitados:\n" + "\n".join([e(f"Nome {i+1}: ") for i in rg(5)]))
def q29():
    pr(f"Maior idade: {max([int(e(f'Idade {i+1}: ')) for i in rg(5)])}")
def q30():
    pr(f"Soma: {sum(iter(lambda: int(e('N (0 para sair): ')), 0))}")
def q31():
    pr(*["Desenvolvimento de Sistemas", "Mecatrônica", "Eletrotécnica", "Automação", "Redes"], sep='\n')
def q32():
    cursos = ["Mecatrônica", "Eletrotécnica"]; cursos.append("Segurança do Trabalho"); pr(cursos)
def q33():
    pr([e(f"Nome {i+1}: ") for i in rg(3)])
def q34():
    pr(f"Média: {sum([int(e(f'Idade {i+1}: ')) for i in rg(3)])/3:.1f}")
def q35():
    pr({'nome': 'Ana Silva', 'idade': 22, 'curso': 'Sistemas'})
def q36():
    aluno={'nome': 'Ana', 'idade': 22}; aluno.update({'nota': 9.5}); pr(aluno)
def q37(f=e('Frase: ')):
    pr(f"Palavras: {len(f.split())}")
def q38(f=e('Frase: ')):
    pr(f"Vogais: {sum(1 for c in f.lower() if c in 'aeiou')}")
def q39(nome=e("Nome: ")):
    pr("Começa com 'A'" if nome.strip().upper().startswith('A') else "Não começa com 'A'")
def q40(nome=e("Nome: ")):
    pr(nome.upper())
def q41(n=fl(e('Número: '))):
    pr(f"Dobro: {n * 2}")
def q42(a=fl(e('N1: ')), b=fl(e('N2: '))):
    pr(f"Soma: {a + b}")
def q43(li=[10, 20, 30, 40, 50]):
    pr(f"Média: {(lambda l: sum(l)/len(l) if l else 0)(li)}")
def q44(nome=e('Nome: ')):
    pr(f"Olá, {nome}! Bem-vindo(a).")
def q45(li=['Ana', 'Carlos', 'Bia', 'Alexandre']):
    pr(f"Mais curto: {min(li, key=len)}")
def q46(n1=fl(e("N1: ")), n2=fl(e("N2: "))):
    pr("Aprovado" if (n1+n2)/2 >= 7 else "Reprovado")
def q47(i=int(e("Número: "))):
    pr(f"É par? {i % 2 == 0}")
def q48(dic={'nome':'Ricardo Milos','idade':35,'curso':'Mecatrônica'}):
    [pr(f"{k.title()}: {v}") for k,v in dic.items()]
def q49(li=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    pr([i for i in li if i % 2 == 0])
def q50():
    while (op := e("\n1-Média\n2-Aprovados\n3-Sair\nOpção: ")) != '3':
        if op == '1': pr(">>> Média: 8.2")
        elif op == '2': pr(">>> Aprovados: Ana, Carlos")
        else: pr("Inválido.")
    pr("Saindo...")

if __name__ == "__main__":
    questoes = {
        '1': q1, '2': q2, '3': q3, '4': q4, '5': q5, '6': q6, '7': q7, '8': q8, '9': q9, '10': q10,
        '11': q11, '12': q12, '13': q13, '14': q14, '15': q15, '16': q16, '17': q17, '18': q18, '19': q19, '20': q20,
        '21': q21, '22': q22, '23': q23, '24': q24, '25': q25, '26': q26, '27': q27, '28': q28, '29': q29, '30': q30,
        '31': q31, '32': q32, '33': q33, '34': q34, '35': q35, '36': q36, '37': q37, '38': q38, '39': q39, '40': q40,
        '41': q41, '42': q42, '43': q43, '44': q44, '45': q45, '46': q46, '47': q47, '48': q48, '49': q49, '50': q50}
    while True:
        pr("\n" + "="*50)
        num_questao = e("Digite o número da questão que deseja executar (1-50) ou 'sair': ")
        pr("="*50 + "\n")
        if num_questao.lower() in ['sair', 'exit', 'q', '0']:
            pr("Programa finalizado.")
            break
        funcao_para_executar = questoes.get(num_questao)
        if funcao_para_executar:
            pr(f"--- Executando Questão {num_questao} ---")
            funcao_para_executar()
            pr(f"--- Fim da Questão {num_questao} ---")
        else:
            pr("Questão inválida. Por favor, digite um número entre 1 e 50.")