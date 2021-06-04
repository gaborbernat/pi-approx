from math import pi

from pi_approx_cy import approximate_pi

def test_approx() -> None:
    assert (approximate_pi(300) - pi) < 0.1
