from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        # Aquí puedes guardar el mensaje o enviar un email
        with open('mensajes.txt', 'a') as f:
            f.write(f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}\n\n')

        flash('Mensaje enviado correctamente', 'success')
        return redirect(url_for('contacto'))

    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
