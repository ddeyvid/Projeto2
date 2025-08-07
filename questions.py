# %% [markdown]
# # O que é o Pandas e para que serve
# 
# - Análise de Dados (seja para DataScience, seja para trabalhar de forma integrada com arquivos em Excel e Banco de Dados)
# - Melhor biblioteca/módulo para trabalhar com quantidades enormes de informações
# - Uma mistura de listas e dicionários de forma muito eficiente
# 
# ## Resumo
# 
# Se você trabalha com muitos dados, você vai precisar usar o pandas
# 
# ## Forma de usar

# %%
from openpyxl import Workbook, load_workbook # type: ignore
from IPython.display import display
from datetime import datetime
import pandas as pd # type: ignore
import requests # type: ignore
import io
from tqdm import tqdm # type: ignore
df = pd.read_csv("Contoso - Vendas - 2017.csv", sep=";")
df.head()

# %%
df.info()
print(df["ID Cliente"])

# %%
lista = ['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']
produtos_quantidade = df[lista]
produtos_quantidade

# %%
cPr = pd.read_csv("Contoso - Cadastro Produtos.csv", sep=";", encoding="latin1")
cLi = pd.read_csv("Contoso - Clientes.csv", sep=";", encoding="latin1")
cLo = pd.read_csv("Contoso - Lojas.csv", sep=";", encoding="latin1")
cPm = pd.read_csv("Contoso - Promocoes.csv", sep=";", encoding="latin1")
cVe = pd.read_csv("Contoso - Vendas - 2017.csv", sep=";", encoding="latin1")
display(cPr)

# %%
cliDf = cLi[['ID Cliente', 'E-mail']]
proDf = cPr[['ID Produto', 'Nome do Produto']]
lojDf = cLo[['ID Loja', 'Nome da Loja']]

# %%
cVe = cVe.merge(proDf, on='ID Produto')
cVe = cVe.merge(lojDf, on='ID Loja')
cVe = cVe.merge(cliDf, on='ID Cliente')
cVe = cVe.rename(columns={'E-mail': 'E-mail do Cliente'})
display(cVe)

# %%
freq = cVe["E-mail do Cliente"].value_counts()
display(freq)
freq[:5].plot(figsize=(15, 5))

# %%
cVe = cVe.groupby(by='Nome da Loja').sum()
display(cVe)
cVe = cVe[['Quantidade Vendida']]
display(cVe)


# %%
#ordenando o dataframe
vLoj = cVe.sort_values('Quantidade Vendida', ascending = False)
display(vLoj)
cVe.to_csv('Teste.csv')
#podemos plotar em um gráfico
vLoj[:5].plot(figsize=(15, 5), kind='bar')

# %%
maiV = cVe['Quantidade Vendida'].max()
melL = cVe['Quantidade Vendida'].idxmax()
print(maiV, melL)

# %%
minV = cVe['Quantidade Vendida'].min()
pioL = cVe['Quantidade Vendida'].idxmin()
print(minV, melL)

# %%
qtd_vendida, qtd_devolvida = cVe['Quantidade Vendida'].sum(), cVe['Quantidade Devolvida'].sum(); print('{:.2%}'.format(qtd_devolvida / qtd_vendida))

# %%
loj = cVe[cVe["ID Loja"] == 306]
qtd_vendida, qtd_devolvida = loj['Quantidade Vendida'].sum(), loj['Quantidade Devolvida'].sum(); print('{:.2%}'.format(qtd_devolvida / qtd_vendida))

# %% [markdown]
# ### Desafio: e se eu quisesse criar uma tabela apenas com as vendas da Loja Contoso Europe Online e que não tiveram nenhuma devolução. Quero criar essa tabela e saber quantas vendas são.

# %%
tab = loj[loj['Quantidade Devolvida'] == 0]
tab.to_csv('EuropeOnlineSemDev.csv')

# %% [markdown]
# ### Agora, e se quisermos acrescentar uma coluna com o mês, o dia e o ano de cada venda (e não só a data completa)

# %%
cVe['Data da Venda'] = pd.to_datetime(cVe['Data da Venda'], format='%d/%m/%Y')
cVe['Ano da Venda'] = cVe['Data da Venda'].dt.year
cVe['Mes da Venda'] = cVe['Data da Venda'].dt.month
cVe['Dia da Venda'] = cVe['Data da Venda'].dt.day
display(cVe)
cVe.info()

# %%
nvDf = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
nvDf = nvDf.set_index('Nome do Produto')
nvDf.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black']
print(nvDf.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black', 'Preco Unitario'])
print(nvDf.iloc[2, 5])

# %%
nvDf.loc[nvDf['ID Produto'] == 873, 'Preco Unitario'] = 23
display(nvDf.head())

# %%
nvDf.to_csv('NovoCSV.csv')

# %%
url = 'https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download'
cotacao_df = pd.read_csv(url)
display(cotacao_df)

# %%
url = 'https://portalweb.cooxupe.com.br:9080/portal/precohistoricocafe_2.jsp?d-3496238-e=2&6578706f7274=1'
conteudo_url = requests.get(url).content
arquivo = io.StringIO(conteudo_url.decode('latin1'))
cafe_df = pd.read_csv(arquivo, sep=r'\t', engine='python')
display(cafe_df)

# %%
tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

# %%
tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador Imposto"] = 1.5

tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

tabela.to_excel("ProdutosPandas.xlsx", index=False)

# %%
planilha = load_workbook("Produtos.xlsx")

aba_ativa = planilha.active

for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5
        
planilha.save("ProdutosOpenPy.xlsx")

# %%
pbar = tqdm(total=len(cVe['ID Loja']), position=0, leave=True)

for i, id_loja in enumerate(cVe['ID Loja']):
    pbar.update()
    if id_loja == 222:
        cVe.loc[i, 'Quantidade Devolvida'] += 1
        
display(cVe)

# %%
#15
funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
display(funcionarios_df)
display(clientes_df)
display(servicos_df)

funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print('Total de folha salarial é de R${:,}'.format(sum(funcionarios_df['Salario Total'])))

faturamento_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']])
#display(faturamento_df)
print('Faturamento foi de R${:,}'.format(sum(faturamento_df['Tempo Total de Contrato (Meses)'] * faturamento_df['Valor Contrato Mensal'])))

qtde_funcionarios_fecharam = len(servicos_df['ID Funcionário'].unique())
qtde_funcionarios_totais = len(funcionarios_df['ID Funcionário'])
print('Percentual foi de {:.2%}'.format(qtde_funcionarios_fecharam / qtde_funcionarios_totais))

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']])
#display(contratos_area_df)
qtde_contratos_area = contratos_area_df['Area'].value_counts()
print(qtde_contratos_area)
qtde_contratos_area.plot(kind='bar')

qtde_funcionarios_area = funcionarios_df['Area'].value_counts()
print(qtde_funcionarios_area)
qtde_funcionarios_area.plot(kind='bar')

ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio mensal é de R${:,.2f}'.format(ticket_medio))

# %%
#16

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
condition = True

# Folha Salarial
funcionarios_df = funcionarios_df.assign(Salario=funcionarios_df['Salario Base'] - funcionarios_df['Impostos'] - funcionarios_df['VT'] - funcionarios_df['VR'] - funcionarios_df['Beneficios'])

#Faturamento da Empresa
faturamento = clientes_df['Valor Contrato Mensal'].sum()

#% Funcionários Fecharam Contrato
funcionariosContrato = servicos_df['ID Funcionário'].nunique()

servicosArea = servicos_df.merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário', how='left')

#Qtde Contratos por Área
contratosArea = servicosArea.groupby('Area')['Codigo do Servico'].count()

#Funcionários por Área
funcionariosArea = funcionarios_df.groupby('Area')['ID Funcionário'].count()

#Ticket Médio Mensal
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()


if condition:
    display(funcionarios_df, faturamento, funcionariosContrato, servicosArea, contratosArea, funcionariosArea, ticket_medio)


# %%
tabela = pd.read_csv("exportacao_full.csv")
tabela = tabela.loc[tabela['Year']>=2016, :]
tabela = tabela.loc[tabela['Country']=="France", :]
display(tabela)

# %%
dfAExport = (
    pd.read_csv('exportacoes_franca.csv')
    .groupby("Year", as_index=True)["US$ FOB"]
    .sum()
    .apply(lambda x: f"US$ {x:,.0f}")
    .to_frame()
)
dfPE = (
    pd.read_csv("exportacoes_franca.csv")
    .groupby("SH2 Description", as_index=True)["US$ FOB"]
    .sum()
    .sort_values(ascending=False)
    .apply(lambda x: f"US$ {x:,.0f}")
    .to_frame()
)

df2020 = (
    pd.read_csv("exportacoes_franca.csv")
    .query("Year == 2020")[["City", "US$ FOB"]]
    .groupby("City", as_index=True)
    .sum()
    .sort_values("US$ FOB", ascending=False)
    .assign(**{"US$ FOB": lambda df: df["US$ FOB"].apply(lambda x: f"US$ {x:,.0f}")})
)
df2020 = df2020.reset_index()
cidade = df2020.index[0]

df = pd.read_csv("exportacoes_franca.csv")
df2020 = df.query("Year == 2020").groupby("City", as_index=True).sum()

cidade = df2020.reset_index().loc[0, "City"]

dfCity = (
    df[(df["Year"] == 2020) & (df["City"] == cidade)][["SH2 Description", "US$ FOB"]]
    .groupby("SH2 Description")
    .sum()
    .sort_values(by="US$ FOB", ascending=False)
    .assign(**{"US$ FOB": lambda df: df["US$ FOB"].apply(lambda x: f"US$ {x:,.0f}")})
)

print(f"Produtos mais exportados da cidade: {cidade}")
display(dfCity)




