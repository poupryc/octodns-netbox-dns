from octodns_netbox_dns import NetBoxDNSProvider


DEFAULT_CONFIG = {
    "id": 1,
    "url": "https://localhost:8000",
    "token": "",
    "view": False,
    "replace_duplicates": False,
    "make_absolute": True,
}


def test_escape1():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"v=TLSRPTv1; rua=mailto:tlsrpt@example.com"
    value = nbdns._fix_semicolon(rcd_value, escape=True)

    assert value == r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"


def test_escape2():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"
    value = nbdns._fix_semicolon(rcd_value, escape=True)

    assert value == r"v=TLSRPTv1\\; rua=mailto:tlsrpt@example.com"


def test_escape3():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"t=y\;o=~\;"
    value = nbdns._fix_semicolon(rcd_value, escape=True)

    assert value == r"t=y\\;o=~\\;"


def test_escape4():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"t=y;o=~;"
    value = nbdns._fix_semicolon(rcd_value, escape=True)

    assert value == r"t=y\;o=~\;"


def test_unescape1():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"
    value = nbdns._fix_semicolon(rcd_value, escape=False)

    assert value == r"v=TLSRPTv1; rua=mailto:tlsrpt@example.com"


def test_unescape2():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"v=TLSRPTv1\\; rua=mailto:tlsrpt@example.com"
    value = nbdns._fix_semicolon(rcd_value, escape=False)

    assert value == r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"


def test_unescape3():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"t=y\\;o=~\;"
    value = nbdns._fix_semicolon(rcd_value, escape=False)

    assert value == r"t=y\;o=~;"


def test_unescape4():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_value = r"t=y;o=~;"
    value = nbdns._fix_semicolon(rcd_value, escape=False)

    assert value == r"t=y;o=~;"
