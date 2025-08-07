import os
os.environ['PATH'] = "C:\\Users\\deyvid_barcelos\\AppData\\Roaming\\Python\\Python312\\Scripts"

from openpyxl import Workbook, load_workbook
from IPython.display import display
from datetime import datetime
import pandas as pd 
import requests 
from tqdm import tqdm
import io


pd.options.plotting.backend = 'plotly'
df = pd.read_csv("Contoso - Vendas - 2017.csv", sep=";")
df.head()

df.info()
print(df["ID Cliente"])

lista = ['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']
produtos_quantidade = df[lista]
produtos_quantidade

cPr = pd.read_csv("Contoso - Cadastro Produtos.csv", sep=";", encoding="latin1")
cLi = pd.read_csv("Contoso - Clientes.csv", sep=";", encoding="latin1")
cLo = pd.read_csv("Contoso - Lojas.csv", sep=";", encoding="latin1")
cPm = pd.read_csv("Contoso - Promocoes.csv", sep=";", encoding="latin1")
cVe = pd.read_csv("Contoso - Vendas - 2017.csv", sep=";", encoding="latin1")
display(cPr)

cliDf = cLi[['ID Cliente', 'E-mail']]
proDf = cPr[['ID Produto', 'Nome do Produto']]
lojDf = cLo[['ID Loja', 'Nome da Loja']]

cVe = cVe.merge(proDf, on='ID Produto')
cVe = cVe.merge(lojDf, on='ID Loja')
cVe = cVe.merge(cliDf, on='ID Cliente')
cVe = cVe.rename(columns={'E-mail': 'E-mail do Cliente'})
cVv = cVe
display(cVe)

freq = cVe["E-mail do Cliente"].value_counts()
display(freq)
freq[:5].plot()

cVe = cVe.groupby(by='Nome da Loja').sum()
display(cVe)
cVe = cVe[['Quantidade Vendida']]
display(cVe)


vLoj = cVe.sort_values('Quantidade Vendida', ascending = False)
display(vLoj)
cVe.to_csv('Teste.csv')

vLoj[:5].plot()

maiV = cVe['Quantidade Vendida'].max()
melL = cVe['Quantidade Vendida'].idxmax()
print(maiV, melL)

minV = cVe['Quantidade Vendida'].min()
pioL = cVe['Quantidade Vendida'].idxmin()
print(minV, melL)

print(cVv.columns)
qtd_vendida, qtd_devolvida = cVv['Quantidade Vendida'].sum(), cVv['Quantidade Devolvida'].sum(); print('{:.2%}'.format(qtd_devolvida / qtd_vendida))
loj = cVv[cVv["ID Loja"] == 306]
qtd_vendida, qtd_devolvida = loj['Quantidade Vendida'].sum(), loj['Quantidade Devolvida'].sum(); print('{:.2%}'.format(qtd_devolvida / qtd_vendida))
tab = loj[loj['Quantidade Devolvida'] == 0]
tab.to_csv('EuropeOnlineSemDev.csv')

cVv['Data da Venda'] = pd.to_datetime(cVv['Data da Venda'], format='%d/%m/%Y')
cVv['Ano da Venda'] = cVv['Data da Venda'].dt.year
cVv['Mes da Venda'] = cVv['Data da Venda'].dt.month
cVv['Dia da Venda'] = cVv['Data da Venda'].dt.day
display(cVv)
cVv.info()

nvDf = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
nvDf = nvDf.set_index('Nome do Produto')
nvDf.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black']
print(nvDf.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black', 'Preco Unitario'])
print(nvDf.iloc[2, 5])

nvDf.loc[nvDf['ID Produto'] == 873, 'Preco Unitario'] = 23
display(nvDf.head())

nvDf.to_csv('NovoCSV.csv')

url = 'https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download'
cotacao_df = pd.read_csv(url)
display(cotacao_df)

url = 'https://portalweb.cooxupe.com.br:9080/portal/precohistoricocafe_2.jsp?d-3496238-e=2&6578706f7274=1'
conteudo_url = requests.get(url).content
arquivo = io.StringIO(conteudo_url.decode('latin1'))
cafe_df = pd.read_csv(arquivo, sep=r'\t', engine='python')
display(cafe_df)

tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador Imposto"] = 1.5
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]
tabela.to_excel("ProdutosPandas.xlsx", index=False)

planilha = load_workbook("Produtos.xlsx")
aba_ativa = planilha.active
for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5
planilha.save("ProdutosOpenPy.xlsx")
pbar = tqdm(total=len(cVv['ID Loja']), position=0, leave=True)
for i, id_loja in enumerate(cVv['ID Loja']):
    pbar.update()
    if id_loja == 222:
        cVv.loc[i, 'Quantidade Devolvida'] += 1
display(cVv)

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
print('Faturamento foi de R${:,}'.format(sum(faturamento_df['Tempo Total de Contrato (Meses)'] * faturamento_df['Valor Contrato Mensal'])))

qtde_funcionarios_fecharam = len(servicos_df['ID Funcionário'].unique())
qtde_funcionarios_totais = len(funcionarios_df['ID Funcionário'])
print('Percentual foi de {:.2%}'.format(qtde_funcionarios_fecharam / qtde_funcionarios_totais))

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']])
qtde_contratos_area = contratos_area_df['Area'].value_counts()
print(qtde_contratos_area)
qtde_contratos_area.plot()

qtde_funcionarios_area = funcionarios_df['Area'].value_counts()
print(qtde_funcionarios_area)
qtde_funcionarios_area.plot()

ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio mensal é de R${:,.2f}'.format(ticket_medio))

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
condition = True

funcionarios_df = funcionarios_df.assign(Salario=funcionarios_df['Salario Base'] - funcionarios_df['Impostos'] - funcionarios_df['VT'] - funcionarios_df['VR'] - funcionarios_df['Beneficios'])

faturamento = clientes_df['Valor Contrato Mensal'].sum()

funcionariosContrato = servicos_df['ID Funcionário'].nunique()

servicosArea = servicos_df.merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário', how='left')

contratosArea = servicosArea.groupby('Area')['Codigo do Servico'].count()

funcionariosArea = funcionarios_df.groupby('Area')['ID Funcionário'].count()

ticket_medio = clientes_df['Valor Contrato Mensal'].mean()

if condition:
    display(funcionarios_df, faturamento, funcionariosContrato, servicosArea, contratosArea, funcionariosArea, ticket_medio)

#tabela = pd.read_csv("exportacao_full.csv")
#tabela = tabela.loc[tabela['Year']>=2016, :]
#tabela = tabela.loc[tabela['Country']=="France", :]
#display(tabela)

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

df2020 = (pd.read_csv("exportacoes_franca.csv").query("Year == 2020")[["City", "US$ FOB"]]
    .groupby("City", as_index=True).sum().sort_values("US$ FOB", ascending=False)
    .assign(**{"US$ FOB": lambda df: df["US$ FOB"].apply(lambda x: f"US$ {x:,.0f}")})
)
df2020 = df2020.reset_index()
cidade = df2020.index[0]

df = pd.read_csv("exportacoes_franca.csv")
df2020 = df.query("Year == 2020").groupby("City", as_index=True).sum()

cidade = df2020.reset_index().loc[0, "City"]

dfCity = (df[(df["Year"] == 2020) & (df["City"] == cidade)][["SH2 Description", "US$ FOB"]]
    .groupby("SH2 Description").sum().sort_values(by="US$ FOB", ascending=False)
    .assign(**{"US$ FOB": lambda df: df["US$ FOB"].apply(lambda x: f"US$ {x:,.0f}")})
)

print(f"Produtos mais exportados da cidade: {cidade}")
display(dfCity)