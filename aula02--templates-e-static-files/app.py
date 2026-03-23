# Comentario do Python
# Importando o flask na aplicação
from flask import Flask, render_template 
#render_temmplate renderiza as paginas HTML

# Carregando o Flask em uma variavel 
# Declarando variavel no Python
app = Flask(__name__, template_folder='views')
#__name__ é uma váriavel do ambiente do Python que tem o nome do modúlo atual

# Criando a rota principal do site
@app.route('/')
# Def serve para criar funçoes no Python
def home():
    return render_template('index.html')

@app.route('/games')
def games():

    #criando variáveis para passar as informações de um jogo
    titulo = "Resident Evil Requiem"
    ano = 2026
    categoria = "Survival Horror"
    jogadores = ['BKSEdu', 'Alanzoka', 'Maxmrm', 'Chris']
    return render_template('games.html', 
                           
                           #enviando as variáveis
                           titulo=titulo, 
                           ano=ano, 
                           categoria=categoria,
                           jogadores=jogadores)

@app.route('/consoles')
def console():
    consoles = "Playstation 5, Xbox Series X, Nintendo Switch, Playstation 4, Xbox One"
    lancamento = "2020, 2020, 2017, 2013, 2013"
    return render_template('consoles.html',
                           #enviando as variáveis
                           consoles=consoles, 
                           lancamento=lancamento)


# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) # Ligando o modo de Depuração (reinicia automaticamente)
# Rum() - Iniciar um servidor
# Verificando se app.py for o arquivo principal ele inicia o sercidor

