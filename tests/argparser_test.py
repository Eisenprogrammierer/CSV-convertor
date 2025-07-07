import pytest
from cli.parser import create_parser, validate_args


@pytest.fixture
def parser():
	return create_parser()


def test_parser_with_no_args(parser):
	args = parser.parse_args([])
	assert args.file is None


def test_parser_with_file_arg(parser):
	args = parser.parse_args(["--file", "data.csv"])
	assert args.file == "data.csv"


def test_validate_args_with_mocked_file(mocker, parser):
	mocker.patch("os.path.isfile", return_value=True)
	args = parser.parse_args(["--file", "any_file.csv"])
	assert validate_args(args)["file"] == "any_file.csv"


def test_validate_args_with_mocked_missing_file(mocker, parser):
	mocker.patch("os.path.isfile", return_value=False)
	args = parser.parse_args(["--file", "ghost.csv"])
	with pytest.raises(FileNotFoundError):
		validate_args(args)
