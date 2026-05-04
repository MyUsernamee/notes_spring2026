from argparse import ArgumentParser

def main() -> None:
    parser = ArgumentParser('lc3d', '<file>')
    _ = parser.add_argument('filename')
