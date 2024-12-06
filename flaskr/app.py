from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy
import pymysql 
# import azure-storage-blob
# import azure-keyvault-secrets

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kadmin@link-up-database.database.azure.com:3306/linkup_data?driver=ODBC+Driver+17+for+SQL+Server' 

db = SQLAlchemy(app)

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(50), nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(100), nullable=False, unique=True)
    postes = db.relationship('Poste', backref='user')  # Relation avec la table Poste
    medias = db.relationship('Media', backref='user')  # Relation avec la table Media

class Poste(db.Model):
    id_poste = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    contenu_message = db.Column(db.Text)

class Media(db.Model):
    id_media = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    lien_contenu = db.Column(db.String(255))

def create_user(username, password, email):

    with app.app_context():

        new_user = User(pseudo=username, mot_de_passe=password, mail=email)

        db.session.add(new_user)

        db.session.commit()

def create_poste(sender, message):

    with app.app_context():

        new_poste = Poste(id_user=sender, contenu_message=message)

        db.session.add(new_poste)

        db.session.commit()

def create_poste(sender, link):

    with app.app_context():

        new_poste = Poste(id_user=sender, lien_contenu=link)

        db.session.add(new_poste)

        db.session.commit()

@app.route('/users', methods=['POST'])

def create_user_route():

    data = request.get_json()

    create_user(data['username'], data['email'])

    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':

    with app.app_context():

        db.create_all() # Créer les tables de la base de données

app.run(debug=True)