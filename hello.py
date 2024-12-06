from flask import Flask
# from le module flask import la classe Flask
from markupsafe import escape
# depuis le module markupsafe importe la fo fonction escape

from flask import request
# depuis le module flask import l'objet global "request"

app = Flask(__name__)
# variable app = nouvelle de instance de la classe Flask nommé <__name__>

from markupsafe import escape


@app.route("/")
# @<instance d'une classe>.<fonction associé à la classe>
# définir via le méthode route (décorator ?) de Flask que l'url </> 
# sera ce qui déclenche la fonction
def index():
    return "<h1>Sommaire Noam et djibril cravache !</h1>"

'''
def <nom de la nouvelle fonction>
    return <ce qu'elle va retourner>

'''

'''
Pour lancer l'application
flask --app hello run
flask X.py run Y

python -m flask --app hello run
python -m flask X.py run
où soit
    X = app ou X = wsgi 

Y = --host= <adresse IPv4 voulue>
    place le serveur à l'adresse IP désirée
  = --debug
    active le mode débugage durant l'éxécution du serveur
'''

'''
type de convertisseur
string (celui par défaut, donc pas besoin de préciser )
int : accepte les entiers possitifs
float : accepte nombre à virgules positifs
path : une chaine de caractère qui prend des "/"
uuid : accepte de chaine de UUID
'''

'''
app.route('/X/')
    même s'il on rentre "url/X" dans la barre d'adresse, il n'y aura pas d'erreurs

app.route('/X')
     Si l'on rentre "url/X/" dans la barre d'adresse, il  aura la page d'erreur 404
 

'''

@app.route("/hello")
# @<instance d'une classe>.<fonction associé à la classe>
# définir via le méthode route (décorator ?) de Flask que l'url </> 
# sera ce qui déclenche la fonction
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/<name>")
# dans la partie /<name> de l'URL executer la fonction suivante
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/user/<username>')
# dans la route user avec la variable username
# tout les variables rentré comme ça sont entre <>
def affiche_profile_utilisateur(username):
    # afficher le profil de cette utilisateur
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
# dans la route post avec la variable post_id de type interger
# tout les variables rentré comme ça sont de la forme "<type_de_la_variable:nom_de_la_variable>"
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
# dans la route path avec la variable post_id de type path
# tout les variables rentré comme ça sont de la forme "<type_de_la_variable:nom_de_la_variable>"
def affiche_sous_chemin(subpath):
    # affiche le sous-chemin après /path/
    return f'Subpath {escape(subpath)}'

# 2 exemple de routes pour le login 
# exemple 1 :

@app.route('/login', methods=['GET', 'POST'])
# pour la route /login, répondre aux m"thodes http Get (celle par défaut) et Post
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
# permet de gérer toutes les routes avec une unique methode de app

# exemple 2 :
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
#les fonctions séparé fournit par Flask

'''
il existe la fonction "url_for()" qui permet de générer des routes
pour une fonctions
url_for('fonction, argument1, ... , argumentN')
'''

'''
pour des fichiers statiques comme les fichiers css ou javascript
crée un dossier dans le paquet nommé static par exemple, 
et il sera disponible dans l'application dans la route du même nom "/static"
'''

@app.route('/fun/UBW/H_S_Emiya/')
def UBW_H_S_Emiya():
    return "<h1>Archer's Chant :</h1> <br><br> <p>I am, the bone of my sword</p> <p>Steel, is my body, And fire is my blood</p> <p>I have created, over a thousand blades</p> <p>Unknown to Death, Nor known to life</p> <p>I have, withstood pain, to created, many weapons</p> <p>Yet, those hands, will never hold anything</p> <p>So, As I pray</p> <p>UNLIMITED, BLADE WORKS</p>"


# détails de l'objet request
"""
request{
methods= les methodes http utilisé
form= le formulaire avec les données entrées}
"""

