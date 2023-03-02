import pytest


class IntervalMap:
    def __init__(self):
        self.limits = []
        self.map = {}

    def __setitem__(self, upper_bound, value):
        self.limits.append(upper_bound)
        self.limits.sort()
        self.map[upper_bound] = value

    def get(self, index):
        if index >= self.limits[-1]:
            raise KeyError

        for upper_bound in self.limits:
            if index < upper_bound:
                break

        return self.map[upper_bound]


def test_interval_map():
    m = IntervalMap()

    m[15] = 'quinze'
    m[10] = 'dez'
    m[5] = 'cinco'

    assert m.get(0) == 'cinco'
    assert m.get(4) == 'cinco'
    assert m.get(5) == 'dez'
    assert m.get(9) == 'dez'
    assert m.get(10) == 'quinze'
    assert m.get(14) == 'quinze'

    with pytest.raises(KeyError):
        m.get(15)