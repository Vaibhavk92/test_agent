from calc import add, subtract, multiply, divide


def test_operations():
    # Test addition
    result = add(2, 3)
    print(f"add(2, 3) = {result}")
    assert result == 5
    
    result = add(-1, 1)
    print(f"add(-1, 1) = {result}")
    assert result == 0
    
    # Test subtraction
    result = subtract(5, 3)
    print(f"subtract(5, 3) = {result}")
    assert result == 2
    
    result = subtract(0, 1)
    print(f"subtract(0, 1) = {result}")
    assert result == -1
    
    # Test multiplication
    result = multiply(2, 3)
    print(f"multiply(2, 3) = {result}")
    assert result == 6
    
    result = multiply(-1, 1)
    print(f"multiply(-1, 1) = {result}")
    assert result == -1
    
    # Test division
    result = divide(6, 3)
    print(f"divide(6, 3) = {result}")
    assert result == 2
    
    result = divide(5, 2)
    print(f"divide(5, 2) = {result}")
    assert result == 2.5


test_operations()
