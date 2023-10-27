from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/imc')
def imc():
     return render_template('imx.html')

@app.route('/atividade')
def atividade():
     return render_template('atividade.html')

@app.route('/agua')
def agua():
     return render_template('agua.html')

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


 



