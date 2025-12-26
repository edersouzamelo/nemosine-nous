import argparse
from core.core import init

def main():
    parser = argparse.ArgumentParser(description="Nemosine Nous CLI")
    parser.add_argument("--ticks", type=int, default=1, help="Number of lifecycle ticks")
    args = parser.parse_args()

    init(ticks=args.ticks)

if __name__ == "__main__":
    print("Nemosine Nous iniciado")
    main()


