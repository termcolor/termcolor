"""Benchmarks run via pytest-codspeed."""

from __future__ import annotations

import pytest

from termcolor import (
    ATTRIBUTES,
    RESET,
    bold,
    colored,
    cprint,
    red,
    reset,
    termcolor,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from pytest_codspeed import BenchmarkFixture

TEXT = "Hello, World!"
RED = "\033[31m"


@pytest.fixture(autouse=True)
def _force_color(monkeypatch: pytest.MonkeyPatch) -> None:
    # Benchmark the colouring, not the "is this a tty" early return.
    monkeypatch.setenv("FORCE_COLOR", "1")
    termcolor.can_colorize.cache_clear()
    # Warm the cache so the first benchmarked call is not a cache miss.
    colored(TEXT)


def test_colored_plain(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT)


def test_colored_color(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT, "red")


def test_colored_color_on_color(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT, "red", "on_blue")


def test_colored_color_on_color_attrs(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT, "red", "on_blue", ["bold", "underline"])


def test_colored_all_attrs(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT, "red", "on_blue", list(ATTRIBUTES))


def test_colored_rgb(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT, (255, 0, 255), (0, 128, 0))


def test_colored_no_color(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT, "red", no_color=True)


def test_colored_force_color(benchmark: BenchmarkFixture) -> None:
    benchmark(colored, TEXT, "red", force_color=True)


def test_can_colorize(benchmark: BenchmarkFixture) -> None:
    benchmark(termcolor.can_colorize)


def test_cprint(benchmark: BenchmarkFixture) -> None:
    benchmark(cprint, TEXT, "red", "on_blue", ["bold"])


def test_fstring_plain_str(benchmark: BenchmarkFixture) -> None:
    # Reference point for test_code_fstring: plain str constants
    def fstring() -> str:
        return f"{RED}{TEXT}{RESET}"

    benchmark(fstring)


def test_code_fstring(benchmark: BenchmarkFixture) -> None:
    def fstring() -> str:
        return f"{red}{TEXT}{reset}"

    benchmark(fstring)


def test_code_call(benchmark: BenchmarkFixture) -> None:
    benchmark(red, TEXT)


def test_code_call_nested(benchmark: BenchmarkFixture) -> None:
    def nested() -> str:
        return bold(red(TEXT))

    benchmark(nested)


def test_code_call_force_color(benchmark: BenchmarkFixture) -> None:
    benchmark(red, TEXT, force_color=True)
