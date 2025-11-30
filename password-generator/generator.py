# password-generator/generator.py
import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Generate a random password.
    Default length 12, includes upper, lower, digits and symbols.
    """
    char_sets = []
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        # safe set of symbols
        char_sets.append("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not char_sets:
        raise ValueError("At least one character set must be enabled")

    # ensure at least one char from each chosen set
    password_chars = [random.choice(s) for s in char_sets]

    # fill remaining length with random choices from all allowed chars
    all_allowed = "".join(char_sets)
    remaining = length - len(password_chars)
    if remaining > 0:
        password_chars += [random.choice(all_allowed) for _ in range(remaining)]

    random.shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("=== Simple Password Generator ===")
    try:
        length = int(input("Enter desired length (8-32) [12]: ") or 12)
    except ValueError:
        length = 12

    # clamp length
    if length < 4:
        print("Length too small. Using 4.")
        length = 4
    if length > 64:
        print("Length too large. Using 64.")
        length = 64

    # Simple user options
    use_upper = input("Include UPPERCASE? (Y/n): ").strip().lower() != 'n'
    use_lower = input("Include lowercase? (Y/n): ").strip().lower() != 'n'
    use_digits = input("Include digits? (Y/n): ").strip().lower() != 'n'
    use_symbols = input("Include symbols? (Y/n): ").strip().lower() != 'n'

    try:
        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    except ValueError as e:
        print("Error:", e)
        return

    print("\nGenerated password:\n" + pwd + "\n")
    # optionally copy to clipboard if pyperclip available
    try:
        import pyperclip
        pyperclip.copy(pwd)
        print("(Password copied to clipboard)")
    except Exception:
        pass


if __name__ == "__main__":
    main()

