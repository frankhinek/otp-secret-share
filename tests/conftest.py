import pytest

@pytest.fixture()
def decrypt_test_data():
    return [
        # FORMAT: ((pre-shared key, ciphertext), plaintext)
        (("1451dc0a68c0", "6734bf780db4"), "secret"),  # Combining PSK "1451dc0a68c0" and ciphertext "6734bf780db4" recovers original "secret" phrase
        (("cbe9a1aa376f78c5ff7701558770dbee7e29d07c", "af9bc0c95f0219e88d1e663af55db98b104eb110"), "drachma-rigor-bengal"),  # Combining PSK "cbe9a1aa376f78c5ff7701558770dbee7e29d07c" and ciphertext "af9bc0c95f0219e88d1e663af55db98b104eb110" recovers original "drachma-rigor-bengal" phrase
    ]

@pytest.fixture()
def encrypt_test_data():
    return [
        # FORMAT: ((plaintext in hex, pre-shared key), ciphertext)
        (("736563726574", "1451dc0a68c0"), "6734bf780db4"),  # OTP result for "secret" (hex) and PSK "1451dc0a68c0" is ciphertext "6734bf780db4"
        (("64726163686d612d7269676f722d62656e67616c", "cbe9a1aa376f78c5ff7701558770dbee7e29d07c"), "af9bc0c95f0219e88d1e663af55db98b104eb110"),  # OTP result for "drachma-rigor-bengal" and PSK "cbe9a1aa376f78c5ff7701558770dbee7e29d07c" is ciphertext "cbe9a1aa376f78c5ff7701558770dbee7e29d07c"
    ]

@pytest.fixture()
def plaintext_test_data():
    return [
        "Abrogate",
        "cancel; deny; repeal",
        "Blasphemy",
        "speech which offends religious sentiments",
        "Credible",
        "believable",
        "Enigma",
        "puzzle; mystery",
        "Harbingers",
        "indicators; bringers of warnings",
        "Labyrinthine",
        "complicated; highly convoluted",
        "Nuzzle",
        "cuddle; snuggle",
        "Plaudit",
        "statement giving strong praise",
        "Reprehensible",
        "shameful; very bad",
        "Tardy",
        "slow; late; overdue; delayed",
        "A Man, A Plan, A Canal, Panama!"
    ]

@pytest.fixture()
def generate_otp_test_data():
    return [
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 96
    ]

@pytest.fixture()
def s2x_test_data():
    return [
        ("a", "61"),
        ("Z", "5a"),
        ("\t", "09"),
        ("secret", "736563726574"),
        ("psk", "70736b"),
        ("A Man, A Plan, A Canal, Panama!", "41204d616e2c204120506c616e2c20412043616e616c2c2050616e616d6121")
    ]