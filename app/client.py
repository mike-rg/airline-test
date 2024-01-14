class Client:
    def __init__(self, id, name, email, address, active=False):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.active = active

    def __str__(self):
        return f"{self.id}=={self.name}=={self.email}=={self.active}"

    def __hash__(self):
        return hash(self.id)

    @property
    def is_active(self):
        return self.active
