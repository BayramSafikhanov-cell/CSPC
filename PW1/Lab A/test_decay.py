"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


# TODO 2: test_matches_law

    
def test_matches_law():
    N0, lam = 1000, 0.4
    dt, steps = 0.05, 200
    t = dt * steps

    finals = [simulate(N0, lam, seed=s)[-1] for s in range(200)]
    avg = np.mean(finals)
    expected = N0 * np.exp(-lam * t)

    assert avg == pytest.approx(expected, rel=0.05)

