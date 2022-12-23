# One-Time Pad Secret Sharing

This utility is an implementation of One-Time Padding (OTP) intended to be used for secret splitting.

Simplistically, In this case, you don't fragment the key into pieces, you create additional keys exactly the same length and then chuck the original key away. The only way to recreate the original key is to XOR all of the generated keys back together.

## Background

From [Wikipedia](https://en.wikipedia.org/wiki/One-time_pad):

> In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a
single-use pre-shared key that is not smaller than the message being sent. In this technique, a plaintext is paired with
a random secret key (also referred to as a one-time pad). Then, each bit or character of the plaintext is encrypted by
combining it with the corresponding bit or character from the pad using modular addition.
>
> The resulting ciphertext will be impossible to decrypt or break if the following four conditions are met:
>
> 1. The key must be at least as long as the plaintext.
> 2. The key must be random (uniformly distributed in the set of all possible keys and independent of the plaintext),
> entirely sampled from a non-algorithmic, chaotic source such as a hardware random number generator.
> 2. The key must never be reused in whole or in part.
> 3. The key must be kept completely secret by the communicating parties.
