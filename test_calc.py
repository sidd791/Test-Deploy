import calc

class Test:
    def test_addition(self):
        assert 4 == calc.add_num(2, 2)

    def test_difference(self):
        assert 2 == calc.difference_num(2, 4)

    def test_product(self):
        assert 4 == calc.product_num(2, 2)