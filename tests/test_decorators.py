from _pytest.capture import capsys

from src.decorators import log


def test_log_ok(capsys):
    @log()
    def power_2(num):
        return num ** 2

    power_2(4)

    assert capsys.readouterr().out == "power_2 ok\n\n"
