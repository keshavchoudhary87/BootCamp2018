import prob4
import pytest

@pytest.fixture
def set_up_fractions():
    frac_1_3 = prob4.Fraction(1, 3)
    frac_1_2 = prob4.Fraction(1, 2)
    frac_n2_3 = prob4.Fraction(-2, 3)
    frac_5_1 = prob4.Fraction(5,1)
    frac_5_6 = prob4.Fraction(5,6)
    return frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6


def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = prob4.Fraction(30, 42)
    assert frac.numer == 5
    assert frac.denom == 7

    with pytest.raises(ZeroDivisionError) as excinfo1:
        prob4.Fraction(5,0)
    assert excinfo1.value.args[0] == "denominator cannot be zero"

    with pytest.raises(TypeError) as excinfo2:
        prob4.Fraction(1.3, 4.2)
    assert excinfo2.value.args[0] == "numerator and denominator must be integers"



def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6 = set_up_fractions
    assert str(frac_1_3) == "1/3"
    assert str(frac_1_2) == "1/2"
    assert str(frac_n2_3) == "-2/3"
    assert str(frac_5_1) == "5"


def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.


def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6 = set_up_fractions
    assert frac_1_2 == prob4.Fraction(1, 2)
    assert frac_1_3 == prob4.Fraction(2, 6)
    assert frac_n2_3 == prob4.Fraction(8, -12)

    assert float(frac_1_2) == frac_1_2

def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6 = set_up_fractions
    assert frac_1_2 + frac_1_3 == frac_5_6

def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6  = set_up_fractions
    assert frac_5_6 - frac_1_2 == frac_1_3

def test_fraction_mul(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6  = set_up_fractions
    assert frac_1_3 * frac_1_2 == prob4.Fraction(1,6)

def test_fraction_truediv(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3, frac_5_1, frac_5_6  = set_up_fractions
    assert frac_1_3 / frac_1_2 == prob4.Fraction(2,3)

    with pytest.raises(ZeroDivisionError) as excinfo3:
        frac_5_1 / prob4.Fraction(0,5)
    assert excinfo3
