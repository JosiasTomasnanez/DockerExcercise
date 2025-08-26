import requests

TOKEN = "admin-token-123"
BASE_URL = "http://localhost:4242/api/admin/features"
HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}

def crear_flag(nombre, enabled=True):
    data = {
        "name": nombre,
        "enabled": enabled,
        "strategies": [{"name": "default", "parameters": {}}]
    }
    resp = requests.post(BASE_URL, json=data, headers=HEADERS)
    print(resp.status_code, resp.text)

if __name__ == "__main__":
    crear_flag("colores_dinamicos", enabled=True)
