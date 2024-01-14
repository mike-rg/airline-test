from app.client import Client


def test_client_creation():
    client = Client(id=1, name="John Doe", email="john@example.com", address="123 First St", active=True)
    assert client.id == 1
    assert client.name == "John Doe"
    assert client.email == "john@example.com"
    assert client.address == "123 First St"
    assert client.active is True
    assert str(client) == "1==John Doe==john@example.com==True"
    assert hash(client) == hash(1)

def test_client_is_active():
    active_client = Client(id=1, name="John Doe", email="john@example.com", address="123 First St", active=True)
    inactive_client = Client(id=2, name="Jane Doe", email="jane@example.com", address="456 Second St", active=False)

    assert active_client.is_active is True
    assert inactive_client.is_active is False
