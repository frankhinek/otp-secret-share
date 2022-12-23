import pytest

@pytest.fixture()
def check_repeating_sequence_fail_test_data():
    return [
        # FORMAT: (sequence length, value A, value B, repeating sequence present)
        (2, "c668e0ad053b455f4a16a8f890976c723c2271f58823b5e2fb", "3edfe5e28e2be4b10ddb2ec7bd033be46bc2acd924ba319dda", "3b"),
        (2, "1d243790d13aead220bded8f8e7b84096a751d5dc30ec45aa0", "0adb6d555bf13f0a417d642fe300aeabd69a2c6d89897cefa9", "ea"),
        (2, "61b971a0f2aa9d6c086a673989b613cdf01dd3fb5068aed862", "0ea0badc1351554c016dada3af84e377089ef7122ef85b3443", "71"),
        (2, "f64f123a3b2b8303a6f4abfc23b142a3d0475411565cde5b9e", "924b9a718ede88063dfe4dea77f24603c2fb5617de1fe4d8f8", "03"),
        (3, "eeabba9a86092163caa2cf23da9e6d6d000adf02e715f8c4b5", "24cbd93f0b339caaefcdd0287a7e103ba2c4107b364ffd5f36", "a2c"),
        (3, "0e8cd9336932e24ce03a82a55da070713386f81b4ebe965194", "ba8a041f64a5c9d3019c16517e29fe7dd94f5a2637a438e1e9", "651"),
        (3, "451643e5bc493ef7410072d56f8fe90a632c86cb88787f322a", "cc88ca8dc696071ffeee7787f62ac5b6eb4614610fd7eda799", "787"),
        (3, "ac12a426fa4a03529aed11893b9710869eb030d14f269b11d5", "227659d59ecb5bc309c5425f2482531329f7501f82248c729a", "29a"),
        (4, "f0c83d6211b5d871f993f4da2944ee19e73fdba3e059dbe461", "e5aca26e76e607e0d1320e63f7fe73f2315ed4a1072e5233c0", "e73f"),
        (4, "6e438d410322ab65065e3175c61446d9dccb6ad90908c7aaa1", "eb39b69ada4443de2b0fc614e603807f4953add93fa8fce85a", "c614"),
        (4, "b2c0d8dcc04ae35f16429369ba4b18727c953e6c7d3b2d1941", "8a4bb84f97801c167c95197cd8d4f410588f2e7d1b0e2dff3f", "7c95"),
        (4, "772eb37ed9cdf3f8975b3be616b3a01869088d990cc02f2d70", "e0c019ae9b0d6772e6507993eb9785a05ca11d934c0ce0fe26", "772e"),
        (5, "096667df1ec2a78f5bf2f6ddb63a8a698fcedee522d1b9b3d2", "4832679462dcf5bf26b2d07dca7501f7ee97e860731c11b2c5", "f5bf2"),
        (5, "3f7390ab58ea196fd15798116217c00a10cfbb3d33c686d0c8", "06d09cc734860d0ab584812662552bbb5beec0a3e355a9c279", "0ab58"),
        (5, "1722a27701489e5f348aced7456cfd49919350b027cebe4a73", "2e5ca350b0358f72b6fcc81ddccd5adfe21439ca190e6e83b4", "350b0"),
        (5, "4144d0759c7c77dad95da8059448b14ec5b6edbed7dcf8f6c3", "c2b37ab759c3e027dd7dcfdbaec1e94b954221547f5c28132f", "d7dcf"),
        (6, "fafecf669d055f05231bdbc8de2aae25ba6c460cf610fbf32b", "e9399efafecf81350bfcf44b4a5db55466049eb905d884359e", "fafecf"),
        (6, "4a5af19f453fea9cc675c6b3f13cf7abace8eb2db56783dc0b", "8471e828b6783dc1dff703552ef63f87f8c362a7203b25f826", "6783dc"),
        (6, "5d89c4103fd8c24871b2b7ea7d7da34ba29faa9c67c1264b5c", "e3dc4ba29ffae1492994a9b56b26f15912c7d7607500eaaaf2", "4ba29f"),
        (6, "b19138fca20f4a7da9ed99e2b2d0a07463672d200eefadd5a1", "7ab2d0a0034e2167e9d62d381d999170ef196490b6420ecec8", "b2d0a0"),

        (4, "696e64696361746f72733b206272696e67657273206f66207761726e696e6773", "85daf45a4760d6821074d7d4dcd73db7761c97c457fecad297977fe8961f10a2", "7761")
    ]

@pytest.fixture()
def check_repeating_sequence_pass_test_data():
    return [
        # FORMAT: (sequence length, value A, value B)
        (2, "c668e0ad053b455f4a16a8f890976c723c2271f58823b5e2fb", "3edfe3f28a2be4b10ddb2ec7bd01b3e46bc2acd924ba319dda"),
        (3, "eeabba9a86092163caa2cf23da9e6d6d000adf02e715f8c4b5", "24cbd93f0b339caaefcdd0287a7e103bc2a4107b364ffd5f36"),
        (4, "f0c83d6211b5d871f993f4da2944ee19e73fdba3e059dbe461", "e5aca26e76e607e0d1320e63f7ff37e2315ed4a1072e5233c0"),
        (5, "096667df1ec2a78f5bf2f6ddb63a8a698fcedee522d1b9b3d2", "4832679462dc2fb5f6b2d07dca7501f7ee97e860731c11b2c5"),
        (6, "fafecf669d055f05231bdbc8de2aae25ba6c460cf610fbf32b", "e9399efcefaf81350bfcf44b4a5db55466049eb905d884359e"),
    ]

@pytest.fixture()
def check_repeating_sequence_fail_short_input_data():
    return [
        # FORMAT: (sequence length, value A, value B)
        (2, "a", "3edfe3"),
        (2, "a9a860", "b"),
        (3, "ee", "24cbd93f0b339caae"),
        (3, "cbd123", "ab"),
        (4, "f0c", "e5aca26e"),
        (4, "9e73fdba3e059dbe461", "e5a"),
    ]

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