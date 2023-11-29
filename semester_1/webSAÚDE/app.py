from flask import Flask, request, render_template, redirect
from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
mysql = connect(
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    host=os.environ['MYSQL_HOST'],
    database=os.environ['MYSQL_DB'],
)

with mysql.cursor() as cursor:
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS table_feedback (
                nome      VARCHAR(255),
                email     VARCHAR(255),
                feedback  VARCHAR(255),
                avaliacao INTEGER
            )
        """
    )


@app.route('/receber_feedback', methods=['POST'])
def receber_feedback():
    with mysql.cursor() as cursor:
        cursor.execute(
            """
                INSERT INTO table_feedback (nome, email, feedback, avaliacao)
                     VALUES (%(nome)s, %(email)s, %(feedback)s, %(avaliacao)s)
            """,
            request.form,
        )
    return redirect("/")


@app.route('/', methods=['GET'])
def index():
    with mysql.cursor(dictionary=True) as cursor:
        cursor.execute(
            """
                SELECT nome, feedback, avaliacao
                  FROM table_feedback
                 LIMIT 10
            """
        )
        feedbacks = cursor.fetchall()
    return render_template('index.html', feedbacks=feedbacks)


@app.route('/imc')
def imc():
    return render_template('imc.html')


@app.route('/atividade')
def atividade():
     return render_template('atividade.html')


@app.route('/agua')
def agua():
     return render_template('agua.html')


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


@app.route('/calcular_agua', methods=['POST'])
def calcular_agua():
    peso = float(request.form['peso'])
    agua = peso * 35
    return render_template('agua.html', resultado=agua)


if __name__ == '__main__':
    app.run(debug=True)
