#importamos la clase y metodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
import datetime

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET',"POST"])
def aritmetica():
    if request.method =="POST":
        #Valores que recibo del form n1, n2 son pasados
        num1=float(request.form.get('n1'))
        num2=float(request.form.get('n2'))
        #Realizamos operaciones aritmeticas
        suma= num1 + num2
        resta= num1 - num2
        multiplicacion= num1 * num2
        division = num1 / num2
        return render_template('index.html',    total_suma = suma,
                                                total_resta= resta,
                                                total_multiplicacion= multiplicacion,
                                                total_division= division)
    
    return render_template('index.html')
@app.route('/divisas', methods=['GET', "POST"])
def divisas():
    if request.method=="POST":
        #Valores que recibo del form divisas son pasados
        divisas=float(request.form.get('divisas'))
        #realizamos operaciones de divisas
        dolares= divisas / 4224,21
        euros= divisas / 4653,00
        yen= divisas / 29,00
        pesom= divisas / 218,00
        return render_template('divisas.html',  total_dolares= dolares,
                                                total_euros=euros,
                                                total_yen=yen,
                                                total_pesom=pesom)
    return render_template('divisas.html')

@app.route('/longitudes', methods=['GET',"POST"])
def longitudes():
    if request.method=="POST":
        #Valores que recibo del Form: Longitudes son pasados
        longitudes=float(request.form.get('longitudes'))
        #realizamos operaciones de longitudes
        kilometros= longitudes / 1000
        centimetros= longitudes * 100
        decimetros= longitudes * 10
        milimetros= longitudes *1000
        return render_template('longitudes.html',   t_kilometros=kilometros,
                                                    t_centimetros=centimetros,
                                                    t_decimetros=decimetros,
                                                    t_milimetros=milimetros)
    return render_template('longitudes.html')

        
if __name__ == "__main__":
    app.run(debug=True)