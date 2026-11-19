import pytest

from net import hashring as mod

CASES = [
    ('hash_key', ['alpha'], 3195417371, False),
    ('hash_key', ['beta'], 2727731389, False),
    ('build_ring', [['a'], 2], [[3591822140, 'a'], [3733569455, 'a']], False),
    ('build_ring', [['a', 'b'], 1], [[825135572, 'b'], [3591822140, 'a']], False),
    ('lookup', [[[10, 'a'], [20, 'b']], 'x'], 'a', False),
    ('lookup', [[], 'x'], None, False),
    ('add_node', [[[10, 'a']], 'b', 1], [[10, 'a'], [825135572, 'b']], False),
    ('replicas', [[[10, 'a'], [20, 'b'], [30, 'a']], 'x', 2], ['a', 'b'], False),
    ('hash_key', [''], 3661210606, False),
    ('build_ring', [[], 2], [], False),
    ('lookup', [[[10, 'a']], 'x'], 'a', False),
    ('add_node', [[], 'a', 2], [[3591822140, 'a'], [3733569455, 'a']], False),
    ('add_node', [[[10, 'a'], [20, 'b']], 'c', 0], [[10, 'a'], [20, 'b']], False),
    ('replicas', [[], 'x', 2], [], False),
    ('replicas', [[[10, 'a']], 'x', 3], ['a'], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_hashring_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
