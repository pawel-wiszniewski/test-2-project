import argparse
from typing import Optional


def main():
    params = parse_args()
    print(params)


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", required=True, help="File to change")
    parser.add_argument("--out", required=True, help="Output file")
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
