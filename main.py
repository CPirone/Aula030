from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Avaliação contínua: Aula 030', options=["Home", "Identificação", "Contexto de requisição"])

@app.route('/identificacao')
def identificacao():
    return render_template('identificacao.html', title='Avaliação contínua: Aula 030', aluno='Cleber Pirone', prontuario='PT3008649', instituicao='IFSP')

@app.route('/contexto_requisicao')
def contexto_requisicao():
    return render_template('contexto_requisicao.html', title='Avaliação contínua: Aula 030', navegador='Google Chrome (Versão 122.0.6261.57 (Versão oficial) 64 bits)', ip='99.9.9.99', host='cpirone.pythonanywhere.com')

if __name__ == '__main__':
    app.run(debug=True)
