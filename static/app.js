/* documento para que funcione el formulario*/

document.getElementById("contact-form").addEventListener("submit", function(event){
    event.preventDefault();

    const submitButton = this.querySelector('button[type="submit]');
    submitButton.classList.add('loading');

    const formData = new FormData(this);

    fetch('/send_email', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        showflashMessage('mensaje enciado correctamente.', 'success');
        this.reset(); //limpiar el formulario
        submitButton.classList.remove('loading');
    })
    .catch(error => {
        showflashMessage('hubo un error al enviar el mensaje', 'danger');
        console.error('Error:', error);
        submitButton.classList.remove('loading')
    })
});
function showflashMessage(message, category) {
    const flashContainer = document.getElementById('flash-message');
    const flashMessage = document.createElement('div');
    flashMessage.className = 'alert ${category}';
    flashMessage.textContent = message;

    flashContainer.appendChild(flashMessage);

    setTimeout(() => {
        flashMessage.remove();
    }, 5500);
}