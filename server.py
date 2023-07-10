import hashlib
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

# Función para almacenar usuarios y contraseñas en hash
def almacenar_usuario_contrasena(usuario, contrasena):
    hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Insertar usuario y contraseña en la tabla
    cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (usuario, hash_contrasena))

    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()

# Función para validar usuario y contraseña
def validar_usuario_contrasena(usuario, contrasena):
    hash_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Consultar usuario y contraseña en la tabla
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, hash_contrasena))
    resultado = cursor.fetchone()

    # Cerrar conexión
    conn.close()

    # Retornar True si se encontró el usuario y la contraseña coincidió, False de lo contrario
    return resultado is not None

# Clase para manejar las solicitudes HTTP
class RequestHandler(BaseHTTPRequestHandler):
    # Método para manejar las solicitudes GET
    def do_GET(self):
        # Configurar encabezados de respuesta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Generar respuesta HTML
        response = '''
            <html>
            <head>
                <title>Sitio web de ejemplo</title>
            </head>
            <body>
                <h1>Bienvenido al sitio web de ejemplo</h1>
                <form method="POST">
                    <label for="usuario">Usuario:</label>
                    <input type="text" id="usuario" name="usuario"><br>
                    <label for="contrasena">Contraseña:</label>
                    <input type="password" id="contrasena" name="contrasena"><br>
                    <input type="submit" value="Iniciar sesión">
                </form>
            </body>
            </html>
        '''

        # Enviar respuesta al cliente
        self.wfile.write(response.encode())

    # Método para manejar las solicitudes POST
    def do_POST(self):
        # Configurar encabezados de respuesta
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Obtener datos del formulario enviado por el cliente
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        usuario = post_data.split("&")[0].split("=")[1]
        contrasena = post_data.split("&")[1].split("=")[1]

        # Validar usuario y contraseña
        if validar_usuario_contrasena(usuario, contrasena):
            mensaje = "Inicio de sesión exitoso"
        else:
            mensaje = "Inicio de sesión fallido"

        # Generar respuesta HTML
        response = '''
            <html>
            <head>
                <title>Sitio web de ejemplo</title>
            </head>
            <body>
                <h1>{mensaje}</h1>
            </body>
            </html>
        '''.format(mensaje=mensaje)

        # Enviar respuesta al cliente
        self.wfile.write(response.encode())

# Crear base de datos SQLite y tabla de usuarios si no existen
def crear_base_datos():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (usuario TEXT PRIMARY KEY, contrasena TEXT)''')

    conn.commit()
    conn.close()

# Main
if __name__ == '__main__':
    # Crear la base de datos si no existe
    crear_base_datos()

    # Almacenar usuarios y contraseñas en hash
    almacenar_usuario_contrasena('Usuario1', 'Contraseña1')
    almacenar_usuario_contrasena('Usuario2', 'Contraseña2')
    almacenar_usuario_contrasena('Usuario3', 'Contraseña3')

    # Crear el sitio web en el puerto 9500
    server_address = ('', 9500)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Servidor en ejecución en el puerto 9500...')
    httpd.serve_forever()