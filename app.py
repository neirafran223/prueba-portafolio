from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY', '123')

app.config['MAIL_SERVER'] = 'neirafran23@gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        msg = Message('Nuevo mensaje se contacto',
                      sender=app.condig['MAIL_USERNAME'],
                      recipients=[app.config['mail_username']])
        msg.body = f"nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}"

        mail.send(msg)
        flash("Mensaje enciado correctamente.", "success")
    except Exception as e:
        print(f"Error: {e}")
        flash("Ocurrio un error al enciar el mensaje. Intenta de nuevo mas tarde.", "danger")
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)