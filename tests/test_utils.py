import pytest
from otp_secret_sharing.utils import CHAR_POOL, check_repeating_sequence, decrypt, encrypt, generate_otp, one_time_pad, str_to_hex

#########################################
# check_repeating_sequence_unit() tests #
#########################################

def test_check_repeating_sequence_unit(check_repeating_sequence_fail_test_data):
    for sequence_length, value_a, value_b, expected_match in check_repeating_sequence_fail_test_data:
        result, found_match = check_repeating_sequence(value_a, value_b, sequence_length)
        assert type(result) is bool
        assert (type(found_match) is str) or (type(found_match) is None)

def test_check_repeating_sequence_func_with_match(check_repeating_sequence_fail_test_data):
    for sequence_length, value_a, value_b, expected_match in check_repeating_sequence_fail_test_data:
        result, found_match = check_repeating_sequence(value_a, value_b, sequence_length)
        assert result is True
        assert found_match == expected_match

def test_check_repeating_sequence_func_without_match(check_repeating_sequence_pass_test_data):
    for sequence_length, value_a, value_b in check_repeating_sequence_pass_test_data:
        result, found_match = check_repeating_sequence(value_a, value_b, sequence_length)
        assert result is False
        assert found_match is None

def test_check_repeating_sequence_fail_short_input(check_repeating_sequence_fail_short_input_data):
    for sequence_length, value_a, value_b in check_repeating_sequence_fail_short_input_data:
        with pytest.raises(ValueError) as e_info:
            _, _ = check_repeating_sequence(value_a, value_b, sequence_length)

#########################################
# decrypt() tests                       #
#########################################

def test_decrypt_unit(decrypt_test_data):
    for (ct, k), _ in decrypt_test_data:
        result = decrypt(ct, k)
        assert type(result) is str

def test_decrypt_func(decrypt_test_data):
    for (ct, k), result in decrypt_test_data:
        assert decrypt(ct, k) == result

def test_decrypt_fails_ciphertext_string():
    # decrypt() will fail if the ciphertext passed is a string that is not in hexadecimal format
    ciphertext = "ascii"  # ASCII string
    pre_shared_key = "70736b"  # hex string
    with pytest.raises(ValueError) as e_info:
        decrypt(ciphertext, pre_shared_key)

def test_decrypt_fails_psk_string():
    # decrypt() will fail if the pre-shared key passed is a string that is not in hexadecimal format
    ciphertext = "736563726574"  # hex string
    pre_shared_key = "ascii"  # ASCII string
    with pytest.raises(ValueError) as e_info:
        decrypt(ciphertext, pre_shared_key)

#########################################
# encrypt() tests                       #
#########################################

def test_encrypt_unit(encrypt_test_data):
    for (s, k), _ in encrypt_test_data:
        result = encrypt(s, k)
        assert type(result) is str
        assert int(result, 16)  # result should be base 16 hexadecimal value

def test_encrypt_fails_secret_string():
    # encrypt() will fail if the secret passed is a string that is not in hexadecimal format
    secret = "ascii"  # ASCII string
    pre_shared_key = "70736b"  # hex string
    with pytest.raises(ValueError) as e_info:
        encrypt(secret, pre_shared_key)

def test_encrypt_fails_psk_string():
    # encrypt() will fail if the pre-shared key passed is a string that is not in hexadecimal format
    secret = "736563726574"  # hex string
    pre_shared_key = "ascii"  # ASCII string
    with pytest.raises(ValueError) as e_info:
        encrypt(secret, pre_shared_key)

def test_encrypt_func(encrypt_test_data):
    for (s, k), result in encrypt_test_data:
        assert encrypt(s, k) == result

#########################################
# generate_otp() tests                  #
#########################################

def test_generate_otp_unit(generate_otp_test_data):
    for length in generate_otp_test_data:
        result = generate_otp(length)
        assert type(result) is str
        assert len(result) == length
        try:    
            _ = int(result, 16)  # result should be base 16 hexadecimal value
        except Exception as exc:
            assert False, f"Converting to Base 16 hexadecimal raised an exception {exc}"

def test_generate_otp_func(generate_otp_test_data):
    for length in generate_otp_test_data:
        for c in generate_otp(length):
            assert c in CHAR_POOL

#########################################
# one_time_pad() tests                  #
#########################################

def test_one_time_pad_unit(plaintext_test_data):
    for plaintext in plaintext_test_data:
        result = one_time_pad(plaintext)
        assert type(result) is tuple
        assert len(result) == 2
        psk, ciphertext = result
        assert type(psk) is str
        assert type(ciphertext) is str
        try:    
            _ = int(psk, 16)  # result pre-shared key should be base 16 hexadecimal value
            _ = int(ciphertext, 16)  # result ciphertext be base 16 hexadecimal value
        except Exception as exc:
            assert False, f"Converting to Base 16 hexadecimal raised an exception {exc}"

def test_one_time_pad_func(plaintext_test_data):
    for plaintext in plaintext_test_data:
        psk, ciphertext = one_time_pad(plaintext)
        plaintext_hex = str_to_hex(plaintext)
        assert len(plaintext_hex) == len(psk)  # Verify that the pre-shared key is the exact length of the plaintext input encoded with hexadecimal characters

def test_one_time_pad_fails_int():
    # one_time_pad() expects a string input and will fail if an int is passed
    with pytest.raises(ValueError) as e_info:
        one_time_pad(1)

@pytest.mark.parametrize('execution_number', range(50))
def test_one_time_pad_no_patterns(plaintext_test_data, execution_number):
    # Verify that the resulting ciphertext does not contain the same beginning three characters as the plaintext input in hex.
    # Verify that the ciphertext and plaintext input in hex do not contain the same sequences of 6 or more characters.
    # This is a critical test to verify that the pre-shared key used is at least as long as the input secret.  If the
    # pre-shared key is not as long as the input string (in hex) then the resulting ciphertext will contain sequences
    # from the original input string (in hex).
    for plaintext in plaintext_test_data:
        plaintext_hex = str_to_hex(plaintext)
        _, ciphertext_hex = one_time_pad(plaintext)

        assert plaintext_hex[0:4] != ciphertext_hex[0:4]

        for i in range(0,len(plaintext_hex),4):
            sequence = plaintext_hex[i:i+4]
            if len(sequence) == 4:
                assert sequence not in ciphertext_hex

#########################################
# str_to_hex() tests                    #
#########################################

def test_str_to_hex_unit(s2x_test_data):
    for s, _ in s2x_test_data:
        result = str_to_hex(s)
        assert type(result) is str
        assert len(s) <= len(result)  # hexadecimal string same length or longer than ASCII string

def test_str_to_hex_func(s2x_test_data):
    for s, h in s2x_test_data:
        assert str_to_hex(s) == h
