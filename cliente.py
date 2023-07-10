from ncclient import manager
from jinja2 import Template

device = {
    'host': '10.0.2.15',
    'port': 22,
    'username': 'DaimondzCid',
    'password': '31886d291c4066ff1e4eeb8288f2947fa67fa8349fcf72ecd9af0c1af04c87a5',
    'device_params': {'name': 'csr'}
}

def cambiar_nombre_router(nuevo_nombre):
    # Cargar el archivo de plantilla para cambiar el nombre
    with open('nombre_router_template.xml') as f:
        template = Template(f.read())

    # Renderizar la plantilla con el nuevo nombre
    xml_payload = template.render(nombre=nuevo_nombre)

    # Establecer conexión NETCONF con el router
    with manager.connect(device) as conn:
        # Enviar la configuración XML para cambiar el nombre
        response = conn.edit_config(target='running', config=xml_payload)
        print(response)

def crear_loopback_interface():
    # Cargar el archivo de plantilla para crear la interfaz loopback
    with open('loopback_interface_template.xml') as f:
        template = Template(f.read())

    # Renderizar la plantilla con la configuración de la interfaz loopback
    xml_payload = template.render()

    # Establecer conexión NETCONF con el router
    with manager.connect(device) as conn:
        # Enviar la configuración XML para crear la interfaz loopback
        response = conn.edit_config(target='running', config=xml_payload)
        print(response)

def configurar_router():
    nuevo_nombre = "Concha Cid Hernandez"  # Reemplaza con los apellidos de los integrantes
    cambiar_nombre_router(nuevo_nombre)
    crear_loopback_interface()

configurar_router()