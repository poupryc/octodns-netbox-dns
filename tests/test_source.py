from octodns_netbox_dns import NetBoxDNSSource


DEFAULT_CONFIG = {
    "id": 1,
    "url": "https://localhost:8000",
    "token": "",
    "view": False,
    "replace_duplicates": False,
    "make_absolute": True,
}


def test_absolute1():
    nbdns = NetBoxDNSSource(**DEFAULT_CONFIG)
    rcd = "example.com"
    absolute = nbdns._make_absolute(rcd)

    assert absolute == "example.com."


def test_absolute2():
    nbdns = NetBoxDNSSource(**DEFAULT_CONFIG)
    rcd = "example.com."
    absolute = nbdns._make_absolute(rcd)

    assert absolute == "example.com."
