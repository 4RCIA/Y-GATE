from flask import Flask, session, request, redirect, url_for, render_template
from flask_mysqldb import MySQL
import secrets
import os
import base64
import bcrypt
from werkzeug.utils import secure_filename

app= Flask(__name__)
IMG_FOLDER= os.path.join('static', 'IMG')

app.config['MYSQL_HOST']= 'bjiyhmlszbvvprt8qa6i-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']= 'ut9bcvpmxhcv5pgg'
app.config['MYSQL_PASSWORD']= 'zQLI8lBf4lha8dvsfG4g'
app.config['MYSQL_DB']= 'bjiyhmlszbvvprt8qa6i'
app.static_url_path = '/static'
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['UPLOAD_FOLDER']= IMG_FOLDER
app.config['UPLOAD_FOLDER'] = 'static'
mysql=MySQL(app)
@app.route("/")
def loby():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from COLEGIO")
        result = cur.fetchone()
        if result:
            return render_template("index.html", message=result)
    except Exception as e:
        return render_template("index.html", message=f"Error al conectar con la base de datos: {e}")

if __name__ == '__main__':
    app.run(debug=True)