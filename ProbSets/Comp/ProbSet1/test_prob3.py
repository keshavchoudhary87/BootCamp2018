import prob3
import pytest

def test_operate():
    with pytest.raises(TypeError) as excinfo1:
        prob3.operate(1,2,1)
    assert excinfo1.value.args[0] == "oper must be a string"
    assert prob3.operate(1,2,'+') == 3, "addition error"
    assert prob3.operate(4,1, '-') == 3 , "subtraction error"
    assert prob3.operate(3,2,'*') == 6, 'multiplication error'
    assert prob3.operate(8,2,'/') == 4, 'division error'
    with pytest.raises(ZeroDivisionError) as excinfo2:
        prob3.operate(1,0,'/')
    assert excinfo2.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo3:
        prob3.operate(1,3,'(')
    assert excinfo3.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
