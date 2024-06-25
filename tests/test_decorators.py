from _pytest.capture import capsys

from src.decorators import log


def test_log_ok(capsys):
    @log()
    def power_2(num):
        return num ** 2

    power_2(4)

    assert "power_2 ok" in capsys.readouterr().out


def test_log_error(capsys):
    @log()
    def sum_of_two(a, b):
        return a + b

    try:
        sum_of_two("1", 2)
    except TypeError:
        pass

    assert "sum_of_two error: TypeError. Inputs (('1', 2), {})" in capsys.readouterr().out
