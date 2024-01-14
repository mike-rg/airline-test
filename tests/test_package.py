from app.package import Package, PackageStatus


def test_package_creation():
    package = Package(id=101)
    assert package.id == 101
    assert package.status == PackageStatus.PENDING
    assert str(package) == "101==PackageStatus.PENDING"
    assert hash(package) == hash(101)

def test_package_status():
    package = Package(id=101)
    assert package.is_pending() is True
    assert package.is_sent() is False
    assert package.is_delivered() is False

    package.status = PackageStatus.SENT
    assert package.is_pending() is False
    assert package.is_sent() is True
    assert package.is_delivered() is False

    package.status = PackageStatus.DELIVERED
    assert package.is_pending() is False
    assert package.is_sent() is False
    assert package.is_delivered() is True
