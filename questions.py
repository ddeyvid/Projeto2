import pandas as pd
from openpyxl import Workbook, load_workbook
from IPython.display import display
import requests
import io
from tqdm import tqdm

# Load and display sales data
df_vendas = pd.read_csv("Contoso - Vendas - 2017.csv", sep=";")
display(df_vendas.head())
df_vendas.info()

# Select specific columns
produtos_quantidade = df_vendas[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]
display(produtos_quantidade)

# Load other dataframes
df_produtos = pd.read_csv("Contoso - Cadastro Produtos.csv", sep=";", encoding="latin1")
df_clientes = pd.read_csv("Contoso - Clientes.csv", sep=";", encoding="latin1")
df_lojas = pd.read_csv("Contoso - Lojas.csv", sep=";", encoding="latin1")
df_promocoes = pd.read_csv("Contoso - Promocoes.csv", sep=";", encoding="latin1")

# Select and merge relevant columns
df_clientes_info = df_clientes[['ID Cliente', 'E-mail']]
df_produtos_info = df_produtos[['ID Produto', 'Nome do Produto']]
df_lojas_info = df_lojas[['ID Loja', 'Nome da Loja']]

# Perform merges in a more pythonic way
df_vendas_merged = (
    df_vendas.merge(df_produtos_info, on='ID Produto')
    .merge(df_lojas_info, on='ID Loja')
    .merge(df_clientes_info, on='ID Cliente')
    .rename(columns={'E-mail': 'E-mail do Cliente'})
)
display(df_vendas_merged)

# Analyze and plot email frequency
freq_emails = df_vendas_merged["E-mail do Cliente"].value_counts()
display(freq_emails)
freq_emails[:5].plot(figsize=(15, 5))

# Group by store and analyze sales
df_vendas_loja = df_vendas_merged.groupby('Nome da Loja')[['Quantidade Vendida', 'Quantidade Devolvida']].sum()
display(df_vendas_loja)

# Sort and plot sales
df_vendas_loja_sorted = df_vendas_loja.sort_values('Quantidade Vendida', ascending=False)
display(df_vendas_loja_sorted)
df_vendas_loja_sorted.to_csv('Teste.csv')
df_vendas_loja_sorted[:5].plot(figsize=(15, 5), kind='bar')

# Find best and worst performing stores
melhor_loja = df_vendas_loja['Quantidade Vendida'].idxmax()
maior_venda = df_vendas_loja['Quantidade Vendida'].max()
print(f"Loja com maior venda: {melhor_loja}, Quantidade: {maior_venda}")

pior_loja = df_vendas_loja['Quantidade Vendida'].idxmin()
menor_venda = df_vendas_loja['Quantidade Vendida'].min()
print(f"Loja com menor venda: {pior_loja}, Quantidade: {menor_venda}")

# Calculate return rates
total_vendido = df_vendas_loja['Quantidade Vendida'].sum()
total_devolvido = df_vendas_loja['Quantidade Devolvida'].sum()
taxa_devolucao_geral = total_devolvido / total_vendido
print(f'Taxa de devolução geral: {taxa_devolucao_geral:.2%}')

# Filter and analyze a specific store
df_europe_online = df_vendas_merged.loc[df_vendas_merged['Nome da Loja'] == 'Contoso Europe Online']
vendido_europe_online = df_europe_online['Quantidade Vendida'].sum()
devolvido_europe_online = df_europe_online['Quantidade Devolvida'].sum()
taxa_devolucao_europe_online = devolvido_europe_online / vendido_europe_online
print(f'Taxa de devolução da Contoso Europe Online: {taxa_devolucao_europe_online:.2%}')

# Challenge 1: Create a table for Contoso Europe Online sales with no returns
df_europe_online_sem_devolucao = df_europe_online[df_europe_online['Quantidade Devolvida'] == 0]
df_europe_online_sem_devolucao.to_csv('EuropeOnlineSemDev.csv', index=False)
print(f"Total de vendas sem devolução para Contoso Europe Online: {len(df_europe_online_sem_devolucao)}")

# Challenge 2: Add date components
df_vendas_merged['Data da Venda'] = pd.to_datetime(df_vendas_merged['Data da Venda'], format='%d/%m/%Y')
df_vendas_merged['Ano da Venda'] = df_vendas_merged['Data da Venda'].dt.year
df_vendas_merged['Mes da Venda'] = df_vendas_merged['Data da Venda'].dt.month
df_vendas_merged['Dia da Venda'] = df_vendas_merged['Data da Venda'].dt.day
display(df_vendas_merged.info())

# Indexing and modifying DataFrames
df_produtos_indexed = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';', index_col='Nome do Produto')
display(df_produtos_indexed.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Black', 'Preco Unitario'])
df_produtos_indexed.loc[df_produtos_indexed['ID Produto'] == 873, 'Preco Unitario'] = 23
display(df_produtos_indexed.head())
df_produtos_indexed.to_csv('NovoCSV.csv')

# Load data from URL
cotacao_url = 'https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download'
df_cotacao = pd.read_csv(cotacao_url)
display(df_cotacao)

# Load data from a different URL with specific encoding and separator
cooxupe_url = 'https://portalweb.cooxupe.com.br:9080/portal/precohistoricocafe_2.jsp?d-3496238-e=2&6578706f7274=1'
conteudo_url = requests.get(cooxupe_url).content
df_cafe = pd.read_csv(io.StringIO(conteudo_url.decode('latin1')), sep=r'\t', engine='python')
display(df_cafe)

# Modify and save an Excel file using Pandas
df_excel = pd.read_excel("Produtos.xlsx")
df_excel.loc[df_excel["Tipo"] == "Serviço", "Multiplicador Imposto"] = 1.5
df_excel["Preço Base Reais"] = df_excel["Multiplicador Imposto"] * df_excel["Preço Base Original"]
df_excel.to_excel("ProdutosPandas.xlsx", index=False)
display(df_excel)

# Modify and save an Excel file using openpyxl
planilha_openpyxl = load_workbook("Produtos.xlsx")
aba_ativa = planilha_openpyxl.active
for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5
planilha_openpyxl.save("ProdutosOpenPy.xlsx")

# Update DataFrame with a progress bar
df_vendas_copy = df_vendas_merged.copy()
pbar = tqdm(total=len(df_vendas_copy), position=0, leave=True)
for i in range(len(df_vendas_copy)):
    pbar.update(1)
    if df_vendas_copy.loc[i, 'ID Loja'] == 222:
        df_vendas_copy.loc[i, 'Quantidade Devolvida'] += 1
pbar.close()
display(df_vendas_copy)

# Problem 15: Corporate data analysis
funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
display(funcionarios_df)
display(clientes_df)
display(servicos_df)

# Calculate total payroll
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
folha_salarial_total = funcionarios_df['Salario Total'].sum()
print(f'Total de folha salarial é de R${folha_salarial_total:,.2f}')

# Calculate total revenue
faturamento_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamento_total = (faturamento_df['Tempo Total de Contrato (Meses)'] * faturamento_df['Valor Contrato Mensal']).sum()
print(f'Faturamento total foi de R${faturamento_total:,.2f}')

# Calculate percentage of employees who closed a contract
funcionarios_com_contrato = servicos_df['ID Funcionário'].nunique()
funcionarios_totais = funcionarios_df['ID Funcionário'].nunique()
percentual_funcionarios_com_contrato = funcionarios_com_contrato / funcionarios_totais
print(f'Percentual de funcionários que fecharam contrato: {percentual_funcionarios_com_contrato:.2%}')

# Analyze contracts and employees by area
contratos_por_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
qtde_contratos_por_area = contratos_por_area_df['Area'].value_counts()
print("\nQuantidade de Contratos por Área:")
print(qtde_contratos_por_area)
qtde_contratos_por_area.plot(kind='bar', title='Contratos por Área')

qtde_funcionarios_por_area = funcionarios_df['Area'].value_counts()
print("\nQuantidade de Funcionários por Área:")
print(qtde_funcionarios_por_area)
qtde_funcionarios_por_area.plot(kind='bar', title='Funcionários por Área')

# Calculate average ticket price
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print(f'\nO ticket médio mensal é de R${ticket_medio:,.2f}')

# Problem 16: Refined Corporate data analysis
funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)

# Recalculate net salary
funcionarios_df['Salario Liquido'] = funcionarios_df['Salario Base'] - funcionarios_df['Impostos'] - funcionarios_df['VT'] - funcionarios_df['VR'] - funcionarios_df['Beneficios']
display(funcionarios_df)

# Calculate total revenue
faturamento = (clientes_df['Valor Contrato Mensal'] * clientes_df['Tempo de Contrato (Meses)']).sum() # Assuming Tempo de Contrato exists in clientes_df based on context
print(f"Faturamento da empresa: R${faturamento:,.2f}")

# Calculate unique employees who closed contracts
funcionarios_com_contrato_unico = servicos_df['ID Funcionário'].nunique()
print(f"Número de funcionários que fecharam contrato: {funcionarios_com_contrato_unico}")

# Merge and group services by area
servicos_area_df = servicos_df.merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário', how='left')
contratos_area = servicos_area_df.groupby('Area')['Codigo do Servico'].count()
print("\nContratos por área:")
display(contratos_area)

# Count employees by area
funcionarios_area = funcionarios_df.groupby('Area')['ID Funcionário'].count()
print("\nFuncionários por área:")
display(funcionarios_area)

# Calculate average monthly contract value
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print(f"\nTicket médio mensal: R${ticket_medio:,.2f}")

# Problem 17: Export data analysis
df_exportacao_full = pd.read_csv("exportacao_full.csv")

# Filter data for France from 2016 onwards
df_exportacao_franca = df_exportacao_full.query('Year >= 2016 and Country == "France"')
display(df_exportacao_franca)
df_exportacao_franca.to_csv('exportacoes_franca.csv', index=False)

# Analyze exports by year and product type
df_export_ano = (
    df_exportacao_franca.groupby("Year")["US$ FOB"]
    .sum()
    .map("US$ {:,.0f}".format)
    .to_frame()
)
display(df_export_ano)

df_export_produto = (
    df_exportacao_franca.groupby("SH2 Description")["US$ FOB"]
    .sum()
    .sort_values(ascending=False)
    .map("US$ {:,.0f}".format)
    .to_frame()
)
display(df_export_produto)

# Analyze 2020 exports by city
df_export_2020_cidade = (
    df_exportacao_franca.query("Year == 2020")
    .groupby("City")["US$ FOB"]
    .sum()
    .sort_values(ascending=False)
)
display(df_export_2020_cidade.to_frame().map("US$ {:,.0f}".format))

cidade_mais_exportou = df_export_2020_cidade.index[0]
print(f"Produtos mais exportados da cidade: {cidade_mais_exportou}")

# Analyze top products from the city that exported the most in 2020
df_cidade_top_produtos = (
    df_exportacao_franca.query("Year == 2020 and City == @cidade_mais_exportou")
    .groupby("SH2 Description")["US$ FOB"]
    .sum()
    .sort_values(ascending=False)
    .to_frame()
    .map("US$ {:,.0f}".format)
)
display(df_cidade_top_produtos)