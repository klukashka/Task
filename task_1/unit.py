from task_1.solution import strict
import pytest


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def check(a: str, b: int) -> str:
    return f"{a}, {b}"


def test_sum_two_correct_args():
    result = sum_two(42, 73)
    assert result == 115


def test_greet_correct_args():
    result = check("ABCD", 30)
    assert result == "ABCD, 30"


def test_sum_two_incorrect_args():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)

def test_greet_incorrect_args_name():
    with pytest.raises(TypeError):
        check(123, 30)

def test_greet_incorrect_args_age():
    with pytest.raises(TypeError):
        check("ABCD", "thirty")


def test_sum_two_correct_kwarg_args():
    result = sum_two(a=3, b=4)
    assert result == 7


def test_greet_correct_kwarg_args():
    result = check(a="Blob", b=21)
    assert result == "Blob, 21"


def test_sum_two_mixed_args():
    result = sum_two(5, b=6)
    assert result == 11


def test_sum_two_no_args():
    with pytest.raises(TypeError):
        sum_two()
