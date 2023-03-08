import pytest

from test_project.sample import main, parse_args


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


def test_program_runs_with_correct_parameters():
    params = ["--in", "test.py", "--out", "output.py"]
    main(params)
