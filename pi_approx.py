"""Helps calculating pi"""
import argparse

__version__ = "1.0"


def approximate_pi(iteration_count: int) -> float:
    """
    Approximate the number 𝜋.

    :param iteration_count: the number of iterations to run
    :return: the approximation
    """
    sign, result = 1, 0.0
    for at in range(iteration_count):
        result += sign / (2 * at + 1)
        sign *= -1
    return result * 4


def run() -> None:
    parser = argparse.ArgumentParser(description="Calculate pi approximation.")
    parser.add_argument("it", metavar="N", type=int, help="iteration count")
    ns = parser.parse_args()
    result = approximate_pi(ns.it)
    print(f"result is {result}")


__all__ = (
    "__version__",
    "approximate_pi",
    "run",
)
