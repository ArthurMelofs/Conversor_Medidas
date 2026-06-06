from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if request.method == "POST":

        tipo = request.form["tipo"]
        valor = float(request.form["valor"])

        # Temperatura
        if tipo == "c_f":
            resultado = (valor * 9/5) + 32
            resultado = f"{round(resultado, 2)} °F"

        elif tipo == "f_c":
            resultado = (valor - 32) * 5/9
            resultado = f"{round(resultado, 2)} °C"

        # Metros e pés
        elif tipo == "m_p":
            resultado = valor * 3.280
            resultado = f"{round(resultado, 2)} pés"

        elif tipo == "p_m":
            resultado = valor / 3.280
            resultado = f"{round(resultado, 2)} metros"

        # Quilos e libras
        elif tipo == "kg_lb":
            resultado = valor * 2.20
            resultado = f"{round(resultado, 2)} libras"

        elif tipo == "lb_kg":
            resultado = valor / 2.20
            resultado = f"{round(resultado, 2)} kg"

        # Quilômetros e milhas
        elif tipo == "km_ml":
            resultado = valor * 0.621
            resultado = f"{round(resultado, 2)} milhas"

        elif tipo == "ml_km":
            resultado = valor / 0.621
            resultado = f"{round(resultado, 2)} km"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)