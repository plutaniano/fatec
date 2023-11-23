from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)


load_dotenv()

app.config['MYSQL_HOST'] = os.getenv('localhost')
app.config['MYSQL_USER'] = os.getenv('root')
app.config['MYSQL_PASSWORD'] = os.getenv('vanda123')
app.config['MYSQL_DB'] = os.getenv('web_saude')

mysql = MySQL(app)



#feedback
@app.route('/receber_feedback', methods=['POST'])
def receber_feedback():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        feedback = request.form['feedback']     

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO feedback (nome, email, feedback) VALUES (%s, %s, %s)", (nome, email, feedback))
        mysql.connection.commit()
        cur.close()
        return 'Feedback recebido com sucesso!'

        

@app.route('/')
def index():
    return render_template('index.html')

            
@app.route('/imc')
def imc():
    return render_template('imc.html')

@app.route('/atividade')
def atividade():
     return render_template('atividade.html')

@app.route('/agua')
def agua():
     return render_template('agua.html')


# IMC
@app.route('/calcular', methods=['POST'])
def calcular():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    imc = peso / (altura ** 2) 

    if imc < 16.9:
        resultado = 'Muito abaixo do peso !'
    elif imc <= 18.4:
        resultado = 'Abaixo do peso !'
    elif imc <= 24.9:
        resultado = 'Peso Normal'
    elif imc <= 29.9:
        resultado = 'Acima do peso !'
    elif imc <= 34.9:
        resultado = 'Obesidade grau I'
    elif imc <= 40:
        resultado = 'Obesidade grau II'
    else:
        resultado = 'Obesidade grau III'

    return render_template('imc.html', resultado=resultado)


# ÁGUA
@app.route('/calcular_agua', methods=['POST'])
def calcular_agua():
    peso = float(request.form['peso'])
    agua = peso * 35  

    return render_template('agua.html', resultado=agua)


if __name__ == '__main__':
    app.run(debug=True)



 



