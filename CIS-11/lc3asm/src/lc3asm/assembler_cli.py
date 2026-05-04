from argparse import ArgumentParser, Namespace
import logging
from pathlib import Path

from lc3asm.logging import init_logger
from . import logger
from .assembler import assemble
from .preprocessor import preprocess
from .parser import make_parser

def parse_args() -> Namespace:
    parser = ArgumentParser('lc3asm', '<source_file> [<output_file>]', 'A super simple extended assembler compiler for LC3.')
    _ = parser.add_argument('input')
    _ = parser.add_argument('-s', '--output-preprocessor', required=False, help='Outputs assembly file after preprocessing.')
    _ = parser.add_argument('-o', '--output', required=False, help='Where to output the resulting .obj file')
    _ = parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()

    args.input = Path(args.input)

    if not args.output:
        args.output = args.input.with_suffix('.obj')
        logger.debug("No output filename provided, changing %s to %s", args.input, args.output)

    if args.output_preprocessor:
        args.output_preprocessor = Path(args.output_preprocessor)

    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('Set log level to DEBUG.')

    return args

def main() -> None:
    init_logger()
    args = parse_args()

    logger.debug("Loading LC3 parser...")
    parser = make_parser()

    logger.debug("Reading source file %s...", args.input)

    try:
        input_file = open(args.input, 'rb').read()
        logger.debug('Read %s, with the source %s', args.input, input_file)
    except e as Exception:
        raise Exception(f"Error loading source file {args.input}: {e}")

    postprocess, error = preprocess(args.input, input_file, parser)
    if error:
        exit(1)

    if args.output_preprocessor:
        open(args.output_preprocessor, 'w').write(postprocess)

    obj_file, error = assemble(args.input, input_file, parser)
    if error:
        exit(1)

    open(args.output, 'wb').write(obj_file)
