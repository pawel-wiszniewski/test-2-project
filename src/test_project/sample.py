import argparse
from typing import Optional


def main(args=None):
    params = parse_args(args)
    print(f"In parameter: {params.in_file}, out parameter: {params.out_file}")


def parse_args(args: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_file", required=True, help="File to change")
    parser.add_argument("--out_file", required=True, help="Output file")
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
