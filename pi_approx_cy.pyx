"""Helps calculating pi"""

def approximate_pi(iteration_count: int) -> float:
    """
    Approximate the number 𝜋.

    :param iteration_count: the number of iterations to run
    :return: the approximation
    """
    cdef int sign = 1
    cdef float result = 0.0
    for at in range(iteration_count):
        result += sign / (2 * at + 1)
        sign *= -1
    return result * 4


__all__ = (
    "approximate_pi",
)
