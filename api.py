from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/executar-script', methods=['POST'])
def executar_script():
    # Exemplo: recebe dados JSON e retorna uma soma
    dados = request.get_json()
    numeros = dados.get('numeros', [])
    
    resultado = sum(numeros)
    return jsonify({'soma': resultado})

@app.route('/analise-vendas', methods=['GET'])
def analise_vendas():
    # Exemplo: carrega CSV e retorna total de vendas
    try:
        df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';')
        total_vendas = df['Quantidade Vendida'].sum()
        return jsonify({'total_vendas': total_vendas})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
