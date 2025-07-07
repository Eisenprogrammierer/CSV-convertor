import sys
from cli.parser import create_parser, validate_args
from core.csv_processor import CSVProcessor
from output.formatter import Formatter


def main():
    """Основной рабочий поток программы."""
    try:
        parser = create_parser()
        args = validate_args(parser.parse_args())
        
        if not args or not args.file:
            parser.print_help()
            sys.exit(0)
        
        processor = CSVProcessor(args.file)
        
        result = None
        
        if args.where:
            column, condition = parse_condition(args.where)
            filtered_data = processor.filter_data(column, condition)
            print(Formatter.format_table(filtered_data))
        
        if args.aggregate:
            func, column = parse_aggregate(args.aggregate)
            result = processor.aggregate_data(column, func)
            print(Formatter.format_aggregation(func, column, result))
        
    except FileNotFoundError as e:
        print(Formatter.format_error(f"File not found: {e.filename}"))
        sys.exit(1)
    except Exception as e:
        print(Formatter.format_error(f"Error: {str(e)}"))
        parser.print_help()
        sys.exit(1)


def parse_condition(condition: str) -> tuple[str, str]:
    """Разбирает строку условия на колонку и оператор со значением."""
    for op in (">", "<", "="):
        if op in condition:
            return condition.split(op)[0], f"{op}{condition.split(op)[1]}"
    raise ValueError(f"Invalid condition format: {condition}")


def parse_aggregate(aggregate: str) -> tuple[str, str]:
    """Разбирает строку агрегации на функцию и колонку."""
    if "(" in aggregate and ")" in aggregate:
        func = aggregate.split("(")[0]
        column = aggregate.split("(")[1].rstrip(")")
        return func, column
    raise ValueError(f"Invalid aggregate format: {aggregate}")


if __name__ == "__main__":
    main()
