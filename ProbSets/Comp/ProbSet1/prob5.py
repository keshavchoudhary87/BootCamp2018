def count_sets(cards):
    """Return the number of sets in the provided Set hand.
    Parameters:
        cards (list(str)) a list of twelve cards as 4-bit integers in
        base 3 as strings, such as ["1022", "1122", ..., "1020"].
    Returns:
        (int) The number of sets in the hand.
    Raises:
        ValueError: if the list does not contain a valid Set hand, meaning
            - there are not exactly 12 cards,
            - the cards are not all unique,
            - one or more cards does not have exactly 4 digits, or
            - one or more cards has a character other than 0, 1, or 2."""

    # Check for invalid input
    if len(cards) != 12:
        raise ValueError("There are not exactly 12 cards.")
    if len(cards) > len(set(cards)):
        raise ValueError("The cards are not all unique")
    for card in cards:
        if len(card) != 4:
            raise ValueError("One or more cards does have exactly 4 digits")
    for card in cards:
        for num in card:
            if num not in "012":
                raise ValueError("One or more cards has a character other than 0, 1, or 2")

    # Count the number of sets in this hand
    numSets = 0
    combs = list(combinations(cards, 3))
    for potSet in combs:
        if is_set(str(potSet[0]), str(potSet[1]), str(potSet[2])):
            numSets += 1

    return numSets


def is_set(a, b, c):
    """Determine if the cards a, b, and c constitute a set.
    Parameters:
        a, b, c (str): string representations of 4-bit integers in base 3.
            For example, "1022", "1122", and "1020" (which is not a set).
    Returns:
        True if a, b, and c form a set, meaning the ith digit of a, b,
            and c are either the same or all different for i=1,2,3,4.
        False if a, b, and c do not form a set."""

    digit1, digit2, digit3, digit4 = True, True, True, True

    # Make a set of the corresponding digits.
    # If the set of each digit has length 1 or 3, then
    # the cards form a sets.
    digit1Set = {a[0], b[0], c[0]}
    digit2Set = {a[1], b[1], c[1]}
    digit3Set = {a[2], b[2], c[2]}
    digit4Set = {a[3], b[3], c[3]}

    goodLengths = [1, 3]

    if len(digit1Set) not in goodLengths:
        digit1 = False
    if len(digit2Set) not in goodLengths:
        digit2 = False
    if len(digit3Set) not in goodLengths:
        digit3 = False
    if len(digit4Set) not in goodLengths:
        digit4 = False

    return (digit1 and digit2 and digit3 and digit4)
