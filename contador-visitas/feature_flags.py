from UnleashClient import UnleashClient
import atexit

UNLEASH_TOKEN = "admin-token-123"

# Inicializar cliente Unleash
ff_client = UnleashClient(
    url="http://localhost:4242/api",
    app_name="contador-visitas",
    instance_id="mi-instancia",
    custom_headers={"Authorization": UNLEASH_TOKEN}
)

# Asegurarse de cerrar el cliente al salir
atexit.register(lambda: ff_client.destroy())

# Función para consultar una flag
def is_enabled(flag_name):
    return ff_client.is_enabled(flag_name)

