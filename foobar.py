"""Mini Test 1 - Small Program (Stamps)

Buat list angka 1..100, cetak terbalik secara horizontal dengan aturan:
- Bilangan prima tidak dicetak
- Habis dibagi 3 dan 5 -> "FooBar"
- Habis dibagi 3       -> "Foo"
- Habis dibagi 5       -> "Bar"
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def transform(n: int) -> str:
    if n % 15 == 0:
        return "FooBar"
    if n % 3 == 0:
        return "Foo"
    if n % 5 == 0:
        return "Bar"
    return str(n)


def main() -> None:
    numbers = list(range(1, 101))
    result = [transform(n) for n in reversed(numbers) if not is_prime(n)]
    print(", ".join(result))


if __name__ == "__main__":
    main()
