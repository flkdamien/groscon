import pymysql
from flask import Flask, render_template


app = Flask(__name__)

# Configuration de la base de données
app.config['MYSQL_HOST'] = 'localhost'  # Adresse IP ou nom d'hôte du serveur MySQL
app.config['MYSQL_USER'] = 'root'  # Nom d'utilisateur MySQL
app.config['MYSQL_PASSWORD'] = ''  # Mot de passe MySQL
app.config['MYSQL_DB'] = 'fluck_damien_expi1a'  # Nom de la base de données


@app.route('/')
def affichee_donnee():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM t_todolist_calendrier")
    data = cursor.fetchall()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()