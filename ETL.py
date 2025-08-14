import pandas as pd
import mysql.connector
from mysql.connector import Error
import os
import warnings

# Ignorar warnings de parsing do pandas
warnings.simplefilter(action='ignore', category=pd.errors.ParserWarning)

# Configuração do banco
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Adicione sua senha se necessário
    'database': 'olist'
}

# Parâmetros
folder = 'data'
batch_size = 5000  # Tamanho dos lotes para inserção

for file in os.listdir(folder):
    try:
        table_name = file.strip().replace('.csv', '')
        file_path = os.path.join(folder, file)

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        print(f"\nProcessando arquivo: {file_path}")
        df = pd.read_csv(file_path, on_bad_lines='skip')

        if table_name == 'orderitems':
            valid_products = set(pd.read_sql("SELECT prodID FROM products", connection)['prodID'])
            df = df[df['productID'].isin(valid_products)]

        if table_name == 'orderreviews':
            df = df.dropna(subset=['reviewID'])


        columns = ', '.join(df.columns)
        placeholders = ', '.join(['%s'] * len(df.columns))
        sql = f"REPLACE INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Inserção em lotes
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i+batch_size]
            data = [tuple(row) for row in batch.to_numpy()]
            cursor.executemany(sql, data)
            connection.commit()

        print(f"Dados do arquivo '{file}' inseridos com sucesso!")

    except Error as e:
        print(f"Erro ao processar '{file}': {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
