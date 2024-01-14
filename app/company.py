PACKAGE_PRICE = 10


class Company:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.clients = []
        self.packages = []

    def __str__(self):
        return f"{self.id}=={self.name}"

    def __hash__(self):
        return hash(self.id)

    def is_client(self, client):
        return client in self.clients

    def add_client(self, client):
        if not self.is_client(client):
            self.clients.append(client)

    def add_package(self, client, package):
        if self.is_client(client):
            self.packages.append(package)

    def get_total_package_price(self):
        return len(self.packages) * PACKAGE_PRICE

    def get_total_packages(self):
        return len(self.packages)
