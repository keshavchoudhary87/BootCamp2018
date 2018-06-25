import prob2

def test_prob2():
    assert prob2.month_length("January", False) == 31, "Error in January in non-leap year"
    assert prob2.month_length("February", False) == 28, "Error in February in non-leap year"
    assert prob2.month_length("March", False) == 31, "Error in March in non-leap year"
    assert prob2.month_length("April", False) == 30, "Error in April in non-leap year"
    assert prob2.month_length("May", False) == 31, "Error in May in non-leap year"
    assert prob2.month_length("June", False) == 30, "Error in June in non-leap year"
    assert prob2.month_length("July", False) == 31, "Error in July in non-leap year"
    assert prob2.month_length("August", False) == 31, "Error in August in non-leap year"
    assert prob2.month_length("September", False) == 30, "Error in September in non-leap year"
    assert prob2.month_length("October", False) == 31, "Error in October in non-leap year"
    assert prob2.month_length("November", False) == 30, "Error in Novemberin non-leap year"
    assert prob2.month_length("December", False) == 31, "Error in December in non-leap year"
    assert prob2.month_length("February", True) == 29, "Error in February in leap year"
    assert prob2.month_length("XYZ", True) == None, "Error when no month is inputted"
