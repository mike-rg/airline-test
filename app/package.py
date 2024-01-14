from enum import Enum


class PackageStatus(Enum):
    PENDING = 0
    SENT = 1
    DELIVERED = 2


class Package:
    def __init__(self, id):
        self.id = id
        self.status = PackageStatus.PENDING

    def __str__(self):
        return f"{self.id}=={self.status}"

    def __hash__(self):
        return hash(self.id)

    def is_pending(self):
        return self.status == PackageStatus.PENDING

    def is_sent(self):
        return self.status == PackageStatus.SENT

    def is_delivered(self):
        return self.status == PackageStatus.DELIVERED
