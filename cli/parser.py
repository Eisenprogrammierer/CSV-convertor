import argparse
import os
from typing import Dict, Any, List


CLI_ARGS: List[Dict[str, Any]] = [
	{"flags": ["-f", "--file"], "help": "Full path to the CSV file"},
	{"flags": ["-w", "--where"], "help": "Filter condition (e.g., 'price>500')"},
	{"flags": ["-a", "--aggregate"], "help": "Aggregate function (e.g., 'avg(price)')"},
]


def create_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(description="Process CSV files.")
	for arg in CLI_ARGS:
		parser.add_argument(*arg["flags"], help=arg["help"], required=arg.get("required", False))
	return parser


def validate_args(args: argparse.Namespace) -> argparse.Namespace:
    	if not os.path.isfile(args.file):
        	raise FileNotFoundError(f"File not found: {args.file}")

    	if args.where and not any(op in args.where for op in (">", "<", "=")):
        	raise ValueError("Condition must contain '>', '<' or '='")

    	return args
