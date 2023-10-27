from flask import Flask, request, render_template
app = Flask(__name__)

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


@app.route('/calcular', methods=['POST'])
def calcular():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    imc = peso / (altura ** 2) 

    if imc < 16.9:
        resultado = 'Muito abaixo do peso!'
    elif imc <= 18.4:
        resultado = 'Abaixo do peso!'
    elif imc <= 24.9:
        resultado = 'Peso Normal!'
    elif imc <= 29.9:
        resultado = 'Acima do peso!'
    elif imc <= 34.9:
        resultado = 'Obesidade grau I'
    elif imc <= 40:
        resultado = 'Obesidade grau II'
    else:
        resultado = 'Obesidade grau III'

    return render_template('imc.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)




# peso_kg = float(input("Digite o seu peso (kg): "))
# altura = float(input("Digite a sua altura (m): "))
# imc = (peso_kg) / (altura * 2) 
# if imc < 16.9:
#     print(f'Seu IMC é {imc}.Muito abaixo do peso!')
# elif 17 <= imc <= 18.4:
#     print(f'Seu IMC é {imc}.Abaixo do peso!')
# elif 18.5 <= imc <= 24.9:
#     print(f'Seu IMC é {imc}.Peso Normal, Parabéns!') 
# elif 25 <=  imc <= 29.9:
#      print(f'Seu IMC é {imc}.Acima do peso!') 
# elif 30 <=  imc <= 34.9:
#      print(f'Seu IMC é {imc}.Obesidade grau I') 
# elif 35 <=  imc <= 40:
#      print(f'Seu IMC é {imc}.Obesidade grau II') 
# else:
#      print(f'Seu IMC é {imc}.Obesidade grau III')


 



