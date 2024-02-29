from octodns_netbox_dns import NetBoxDNSProvider


DEFAULT_CONFIG = {
    "id": 1,
    "url": "https://localhost:8000",
    "token": "",
    "view": False,
    "replace_duplicates": False,
    "make_absolute": True,
}


def test1():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd = "example.com"
    absolute = nbdns._make_absolute(rcd)

    assert absolute == "example.com."


def test2():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd = "example.com."
    absolute = nbdns._make_absolute(rcd)

    assert absolute == "example.com."
