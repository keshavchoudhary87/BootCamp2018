@pytest.fixture
def set_up_hands():
    hand1 = ["1022", "1122", "0100", "2021", "0010", "2201",
             "2111", "0020", "1102", "0210", "2110", "1020"]
    handWrongNumCards = ["0000"]
    handNotUnique = ["0000", "0000", "0000", "0000", "0000", "0000",
                     "0000", "0000", "0000", "0000", "0000", "0000"]
    handWrongDigits = ["00000", "1122", "0100", "2021", "0010", "2201",
                       "2111", "0020", "1102", "0210", "2110", "1020"]
    handWrongChar = ["3022", "1122", "0100", "2021", "0010", "2201",
                     "2111", "0020", "1102", "0210", "2110", "1020"]
    return hand1, handWrongNumCards, handNotUnique, handWrongDigits, handWrongChar

def test_count_sets():
    hand1, handWrongNumCards, handNotUnique, handWrongDigits, handWrongChar = set_up_hands()
    assert funcs.count_sets(hand1) == 6
    # Raises ValueError if there are not exactly 12 cards
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handWrongNumCards)
    # Raises ValueError if the cards are not all unique
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handNotUnique)
    # Raises ValueError if one or more cards does not have exactly 4 digits
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handWrongDigits)
    # Raises ValueError if one or more cards has a character other than 0, 1, 2
    with pytest.raises(ValueError) as excinfo:
        funcs.count_sets(handWrongChar)

def test_is_set():
    # Different in all aspects
    assert funcs.is_set("0000", "1111", "2222") == True
    assert funcs.is_set("1022", "1122", "1020") == False
    assert funcs.is_set("1020", "1120", "1220") == True
