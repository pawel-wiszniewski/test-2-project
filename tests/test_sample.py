import pytest

from test_project.sample import parse_args


@pytest.mark.parametrize(
    "params",
    [
        ["--in", "test.py"],
        [],
        ["--out", "test.py"],
    ],
)
def test_program_will_require_parameters_in_and_out(params):
    with pytest.raises(SystemExit):
        parse_args(params)
