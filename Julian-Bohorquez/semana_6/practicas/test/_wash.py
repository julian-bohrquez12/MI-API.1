# tests/test_{TU_PREFIJO}.py
import pytest
from fastapi.testclient import TestClient

class TestAutolavadoAPI:
    
    ##Tests específicos para {AUTOLAVADO} - FICHA 3147246
    ##🚨 PERSONALIZAR TODO SEGÚN TU NEGOCIO
    

    def test_create_servicio_success(self, client, sample_servicio_data, auth_headers):
        ##Test de creación exitosa de {servicio} en {autolavado}"""
        response = client.post(
            "/wash_servicio/",
            json=sample_servicio_data,
            headers=auth_headers
        )

        assert response.status_code == 201
        data = response.json()

        # Validaciones específicas de tu dominio
        assert data["cliente"] == sample_servicio_data["cliente"]
        assert data["vehiculo"] == sample_servicio_data["vehiculo"]
        # Agregar más validaciones específicas

    def test_get_servicio_not_found(self, client, auth_headers):
        #Test de servicio no encontrado en autolavado
        response = client.get("servicio_wash999", headers=auth_headers)

        assert response.status_code == 404
        assert "servicio no encontrado" in response.json()["detail"]

    invalid_data = {
    "clientes": " ",
    "vehiculo": " ",
    "servicio": "Lavado general"
}


    response = client.post(
            "/{wash_servicio/",
            json=invalid_data,
            headers=auth_headers
        )

    assert response.status_code == 422
    errors = response.json()["detail"]

        # Validar errores específicos de tu dominio
    assert any("cliente" in str(error) for error in errors)

def test_update_servicio_complete(client, auth_headers):
    """Test de actualización completa para el dominio de servicios"""
    # Crear entidad
    create_data = {
        "nombre": "Lavado Premium",
        "precio": 50000,
        "duracion": 60
    }
    create_response = client.post("/washservicios/", json=create_data, headers=auth_headers)
    entity_id = create_response.json()["id"]

    # Datos de actualización específicos de tu dominio
    update_data = {
        "nombre": "Lavado Premium Plus",
        "precio": 60000,
        "duracion": 75
    }

    response = client.put(f"/washservicios/{entity_id}", json=update_data, headers=auth_headers)

    assert response.status_code == 200
    updated = response.json()

    # Validar cambios específicos de tu dominio
    assert updated["nombre"] == update_data["nombre"]
    assert updated["precio"] == update_data["precio"]
    assert updated["duracion"] == update_data["duracion"]


def test_update_servicio_partial(client, auth_headers):
    """Test de actualización parcial específica para servicios"""
    # Crear entidad
    create_data = {
        "nombre": "Lavado Express",
        "precio": 20000,
        "duracion": 30
    }
    create_response = client.post("/washservicios/", json=create_data, headers=auth_headers)
    entity_id = create_response.json()["id"]

    # Actualización parcial (ejemplo: solo precio)
    partial_data = {
        "precio": 25000
    }

    response = client.patch(f"/washservicios/{entity_id}", json=partial_data, headers=auth_headers)

    assert response.status_code == 200
    updated = response.json()
    assert updated["precio"] == partial_data["precio"]


def test_delete_servicio_success(client, auth_headers):
    """Test de eliminación exitosa en servicios"""
    # Crear entidad
    create_data = {
        "nombre": "Lavado Básico",
        "precio": 15000,
        "duracion": 20
    }
    create_response = client.post("/washservicios/", json=create_data, headers=auth_headers)
    entity_id = create_response.json()["id"]

    # Eliminar
    response = client.delete(f"/washservicios/{entity_id}", headers=auth_headers)

    assert response.status_code == 200

    # Verificar que ya no existe
    get_response = client.get(f"/washservicios/{entity_id}", headers=auth_headers)
    assert get_response.status_code == 404


def test_delete_servicio_not_found(client, auth_headers):
    """Test de eliminación de entidad inexistente en servicios"""
    response = client.delete("/washservicios/99999", headers=auth_headers)

    assert response.status_code == 404


def test_servicio_business_rules(client, auth_headers):
    """Test de reglas de negocio específicas para servicios"""
    # Ejemplo de validación: el precio no puede ser negativo
    invalid_data = {
        "nombre": "Lavado Especial",
        "precio": -1000,   # inválido
        "duracion": 45
    }

    response = client.post("/washservicios/", json=invalid_data, headers=auth_headers)

    assert response.status_code in (400, 422)
def test_servicio_business_rules(client, auth_headers):
    """Test de reglas de negocio específicas para el dominio Autolavado"""

    # Ejemplos específicos de negocio:
    # - Validar que el precio sea mayor a 0
    # - Validar que la duración del servicio sea mayor a 0
    # - Validar que el nombre del servicio no esté vacío

    # Caso 1: Precio inválido (negativo)
    invalid_data_price = {
        "nombre": "Lavado Económico",
        "precio": -5000,   # inválido
        "duracion": 30
    }
    response = client.post("/washservicios/", json=invalid_data_price, headers=auth_headers)
    assert response.status_code in (400, 422)

    # Caso 2: Duración inválida (cero)
    invalid_data_duration = {
        "nombre": "Lavado Express",
        "precio": 20000,
        "duracion": 0   # inválido
    }
    response = client.post("/washservicios/", json=invalid_data_duration, headers=auth_headers)
    assert response.status_code in (400, 422)

    # Caso 3: Nombre vacío
    invalid_data_name = {
        "nombre": "",   # inválido
        "precio": 15000,
        "duracion": 20
    }
    response = client.post("/washservicios/", json=invalid_data_name, headers=auth_headers)
    assert response.status_code in (400, 422)

def test_servicio_business_rules(client, auth_headers):
    """Test de reglas de negocio específicas para el dominio Autolavado"""

    # Ejemplos específicos de negocio:
    # - Validar que el precio sea mayor a 0
    # - Validar que la duración del servicio sea mayor a 0
    # - Validar que el nombre del servicio no esté vacío

    # Caso 1: Precio inválido (negativo)
    invalid_data_price = {
        "nombre": "Lavado Económico",
        "precio": -5000,   # inválido
        "duracion": 30
    }
    response = client.post("/washservicios/", json=invalid_data_price, headers=auth_headers)
    assert response.status_code in (400, 422)

    # Caso 2: Duración inválida (cero)
    invalid_data_duration = {
        "nombre": "Lavado Express",
        "precio": 20000,
        "duracion": 0   # inválido
    }
    response = client.post("/washservicios/", json=invalid_data_duration, headers=auth_headers)
    assert response.status_code in (400, 422)

    # Caso 3: Nombre vacío
    invalid_data_name = {
        "nombre": "",   # inválido
        "precio": 15000,
        "duracion": 20
    }
    response = client.post("/washservicios/", json=invalid_data_name, headers=auth_headers)
    assert response.status_code in (400, 422)
