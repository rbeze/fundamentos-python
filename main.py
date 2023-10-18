from flask import Flask

# Crie uma instância do aplicativo Flask
app = Flask(__name__)

# Defina uma rota e uma função de visualização (view function)
@app.route('/')
def hello_world():
    return 'Olá, mundo! Este é o meu servidor web em Flask.'

if __name__ == '__main__':
    # Inicie o servidor Flask na porta 5000 (por padrão)
    app.run()
