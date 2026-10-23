import sys


def solve(s: str) -> None:
    # Write your solution here.
    # Print four space-separated counts in the order A C G T, on one line to stdout.
    print(s.count("A"),s.count("C"), s.count("G"), s.count("T"))
    pass


if __name__ == "__main__":
    s = sys.stdin.readline().strip()  # The DNA sequence to count bases in
    solve(s)