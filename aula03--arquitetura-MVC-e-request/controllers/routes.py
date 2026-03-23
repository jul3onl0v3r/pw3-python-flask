#Importando o render_template
# Motor para renderizar as páginas
from flask import Flask, render_template
#Criando a função para receber o Flask(app)

def init_app(app):
    #A apartir daqui virão as rotas
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
    
        #Criando um objeto  Python (dicionário) para representar as propriedades de um jogo
        game = {
            "Titulo": "Red Dead Redemption 2",
            "Ano": 2018,
            "Categoria": "Ação e Aventura"
        }
        #Criando um Vetor (lista)
        jogadores = ['BKSEdu', 'Alanzoka', 'Maxmrm', 'Chris']
        return render_template('games.html', 
                               #enviando as variáveis
                               titulo=titulo, 
                               ano=ano, 
                               categoria=categoria,
                               jogadores=jogadores,
                               game=game)
    
    @app.route('/consoles')
    def console():
        consoles = "Playstation 5"
        lancamento = "2020"
        return render_template('consoles.html',
                               #enviando as variáveis
                               consoles=consoles, 
                               lancamento=lancamento)
    
    