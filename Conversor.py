# Importa as funções do Flask necessárias para:
# - criar o servidor web;
# - renderizar páginas HTML;
# - receber dados enviados pelo formulário.
from flask import Flask, render_template, request

# Cria a aplicação Flask
app = Flask(__name__)

# Define a rota principal do sistema.
# methods=["GET", "POST"] permite:
# GET  -> carregar a página;
# POST -> enviar dados do formulário.
@app.route("/", methods=["GET", "POST"])

def index():

    # Variável que armazenará o resultado da conversão
    resultado = None

    # Verifica se o usuário enviou o formulário
    if request.method == "POST":

        # Captura o tipo de conversão selecionado
        tipo = request.form["tipo"]

        # Captura o valor digitado pelo usuário
        valor = float(request.form["valor"])

        # ==============================
        # Conversões de temperatura
        # ==============================

        # Celsius para Fahrenheit
        if tipo == "c_f":
            resultado = (valor * 9/5) + 32
            resultado = f"{round(resultado, 2)} °F"

        # Fahrenheit para Celsius
        elif tipo == "f_c":
            resultado = (valor - 32) * 5/9
            resultado = f"{round(resultado, 2)} °C"

        # ==============================
        # Conversões de metros e pés
        # ==============================

        # Metros para pés
        elif tipo == "m_p":
            resultado = valor * 3.280
            resultado = f"{round(resultado, 2)} pés"

        # Pés para metros
        elif tipo == "p_m":
            resultado = valor / 3.280
            resultado = f"{round(resultado, 2)} metros"

        # ==============================
        # Conversões de quilos e libras
        # ==============================

        # Quilos para libras
        elif tipo == "kg_lb":
            resultado = valor * 2.20
            resultado = f"{round(resultado, 2)} libras"

        # Libras para quilos
        elif tipo == "lb_kg":
            resultado = valor / 2.20
            resultado = f"{round(resultado, 2)} kg"

        # ==============================
        # Conversões de quilômetros e milhas
        # ==============================

        # Quilômetros para milhas
        elif tipo == "km_ml":
            resultado = valor * 0.621
            resultado = f"{round(resultado, 2)} milhas"

        # Milhas para quilômetros
        elif tipo == "ml_km":
            resultado = valor / 0.621
            resultado = f"{round(resultado, 2)} km"

    # Renderiza a página HTML e envia o resultado da conversão
    return render_template("index.html", resultado=resultado)

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":

    # Inicia o servidor Flask
    app.run(debug=True)
