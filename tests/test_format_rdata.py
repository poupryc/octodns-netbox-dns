from octodns_netbox_dns import NetBoxDNSProvider


DEFAULT_CONFIG = {
    "id": 1,
    "url": "https://localhost:8000",
    "token": "",
    "view": False,
    "replace_duplicates": False,
    "make_absolute": True,
}


def test_a():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "A"
    rcd_value = "127.0.0.1"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "127.0.0.1"


def test_aaaa():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "AAAA"
    rcd_value = "fc07::1"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "fc07::1"


def test_mx():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "MX"
    rcd_value = "10 mx.example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == {
        "preference": 10,
        "exchange": "mx.example.com.",
    }


def test_txt1():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "TXT"
    rcd_value = "v=TLSRPTv1; rua=mailto:tlsrpt@example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"


def test_txt2():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "TXT"
    rcd_value = r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"v=TLSRPTv1\\; rua=mailto:tlsrpt@example.com"


def test_txt3():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "TXT"
    rcd_value = r"v=DKIM1; k=rsa; p=/0f+sikE+k9ZKbn1BJu0/soWht/+Zd/nc/+Gy//mQ1B5sCKYKgAmYTSWkxRjFzkc6KAQhi+/IzaFogEV050wcscdC8Rc8lAQzDUFrMs2ZZK1vFtkwIDAQAB"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert (
        value
        == r"v=DKIM1\; k=rsa\; p=/0f+sikE+k9ZKbn1BJu0/soWht/+Zd/nc/+Gy//mQ1B5sCKYKgAmYTSWkxRjFzkc6KAQhi+/IzaFogEV050wcscdC8Rc8lAQzDUFrMs2ZZK1vFtkwIDAQAB"
    )


def test_txt4():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "TXT"
    rcd_value = r"t=y\;o=~\;"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"t=y\\;o=~\\;"


def test_txt5():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "TXT"
    rcd_value = r"t=y;o=~;"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"t=y\;o=~\;"


def test_srv():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    rcd_type = "SRV"
    rcd_value = r"0 5 25565 mc.example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == {
        "priority": 0,
        "weight": 5,
        "port": 25565,
        "target": "mc.example.com.",
    }
