def test_number_replacer(numbers, number_replacer, number_restorer):
    replaced = number_replacer.process(numbers)
    for i in numbers:
        assert i not in replaced
    restored = number_restorer.process(replaced)
    assert numbers == restored
