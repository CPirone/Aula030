from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
  return render_template(
      'index.html',
      title='Avaliação contínua: Aula 030',
      options=["Home", "Identificacao", "Contexto_requisicao"])


@app.route('/identificacao')
def identificacao():
  return render_template('identificacao.html',
                         title='Avaliação contínua: Aula 030',
                         aluno='Cleber Pirone',
                         prontuario='PT3008649',
                         instituicao='IFSP')


@app.route('/contexto_requisicao')
def contexto_requisicao():
  navegador = request.headers.get('User-Agent')
  ip = request.remote_addr
  host = request.host
  return render_template('contexto_requisicao.html',
                         title='Avaliação contínua: Aula 030',
                         navegador=navegador,
                         ip=ip,
                         host=host)


if __name__ == '__main__':
  app.run(debug=True)
