#!/usr/bin/env python3

import secrets
import string
import argparse
import random

def generate_complex_password(length: int) -> str:
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = "!@#$%^&*()-_=+<>?"

    all_chars = uppercase_chars + lowercase_chars + digit_chars + symbol_chars

    password_chars = [
        secrets.choice(uppercase_chars),
        secrets.choice(lowercase_chars),
        secrets.choice(digit_chars),
        secrets.choice(symbol_chars)
    ]

    for _ in range(4, length):
        password_chars.append(secrets.choice(all_chars))

    random.shuffle(password_chars)

    return ''.join(password_chars)


def main():
    parser = argparse.ArgumentParser(
        description = "Generate a complex password."
    )
    parser.add_argument(
        "length",
        type=int
    )
    parser.add_argument(
        "-o", "--outfile",
        type=str,
    )
    args = parser.parse_args()

    try:
        password = generate_complex_password(args.length)
    except:
        print("Error")

    print(password)
    if args.outfile:
        try:
            with open(args.outfile, 'w') as f:
                f.write(password + '\n')
            print(f"Password saved to: {args.outfile}")
        except Exception as e:
            print(f"Could not write to file '{args.outfile}': {e}")

if __name__ == "__main__":
    main()

