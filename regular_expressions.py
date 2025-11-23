def pythonicNameRe() -> str:
    return r"[A-Za-z_]\w*"


def passwordRe():
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z#$%\d_-]{8,}"


def ipV4AddressRe() -> str:
    part = r"(25[0-5]|2[0-4]\d|1\d\d|0?\d?\d)"
    return part + r"(\." + part + r"){3}"


def mobileIsraelNumberRe() -> str:
    prefix = r"(?:\+972-5[0-9]-?|05[0-9]-?)"
    subscriber = r"(?:\d{7}|\d{3}-\d{2}-\d{2}|\d-\d{2}-\d{2}-\d{2})"
    return prefix + subscriber
