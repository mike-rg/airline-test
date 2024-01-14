from app.client import Client
from app.company import Company
from app.package import Package


def test_company_creation():
    company = Company(id=1, name="Kiu Co.")
    assert company.id == 1
    assert company.name == "Kiu Co."
    assert company.clients == []
    assert company.packages == []
    assert str(company) == "1==Kiu Co."
    assert hash(company) == hash(1)

def test_add_client_to_company():
    company = Company(id=1, name="Kiu Co.")
    client = Client(id=1, name="John Doe", email="john@example.com", address="123 First St", active=True)

    assert not company.is_client(client)
    company.add_client(client)
    assert company.is_client(client)


def test_add_package_to_company():
    company = Company(id=1, name="Kiu Co.")
    client = Client(id=1, name="John Doe", email="john@example.com", address="123 First St", active=True)
    package = Package(id=101)

    assert not company.packages
    company.add_client(client)
    company.add_package(client, package)
    assert company.packages == [package]


def test_get_total_package_price():
    company = Company(id=1, name="Kiu Co.")
    client = Client(id=1, name="John Doe", email="john@example.com", address="123 First St", active=True)
    package1 = Package(id=101)
    package2 = Package(id=102)

    company.add_client(client)
    company.add_package(client, package1)
    company.add_package(client, package2)

    assert company.get_total_package_price() == 20


def test_get_total_packages():
    company = Company(id=1, name="Kiu Co.")
    client = Client(id=1, name="John Doe", email="john@example.com", address="123 First St", active=True)
    package1 = Package(id=101)
    package2 = Package(id=102)

    company.add_client(client)
    company.add_package(client, package1)
    company.add_package(client, package2)

    assert company.get_total_packages() == 2
