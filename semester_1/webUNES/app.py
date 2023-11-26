from flask import Flask, render_template

app = Flask(__name__)



#rota das pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quem_somos") 
def quemsomos():
    return render_template("quem_somos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")



if __name__ == '__main__':
    app.run(debug=True)