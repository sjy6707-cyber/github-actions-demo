# 테스트 코드
from calculator import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    print("✅ add 테스트 통과!")

def test_subtract():
    assert subtract(5, 3) == 2
    print("✅ subtract 테스트 통과!")

def test_multiply():
    assert multiply(4, 3) == 12
    print("✅ multiply 테스트 통과!")

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    print("\n🎉 모든 테스트 통과!")
