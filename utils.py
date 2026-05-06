op = input("기능을 선택하시오(div, reverse, is_even):")

if op == 'div':
    num1 = int(input("a:"))
    num2 = int(input("b:"))

    print(num1 / num2)

elif op == 'reverse':
    original_str = input("sentence:")
    reversed_str = original_str[::-1]

    print(reversed_str)

elif op == 'is_even':
    n = int(input("n:"))
    result = "짝수" if n % 2 == 0 else "홀수"

    print(result)