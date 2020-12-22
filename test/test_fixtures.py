def test_numbers(numbers):
    nl = [int(n) for n in numbers]
    for i in range(10):
        assert i in nl
