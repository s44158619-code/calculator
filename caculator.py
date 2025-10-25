num1_str = input("첫 번째 숫자를 입력하세요: ")
operator = input("연산자 (+, -, *, /, **, %) 를 입력하세요: ")
num2_str = input("두 번째 숫자를 입력하세요: ")

try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    print("오류: 잘못된 숫자 형식입니다.")
    exit()

result = None 

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("오류: 0으로 나눌 수 없습니다.")
    else:
        result = num1 / num2
elif operator == '**':
    result = num1 ** num2
elif operator == '%':
    if num2 == 0:
        print("오류: 0으로 나머지 연산을 할 수 없습니다.")
    else:
        result = num1 % num2
else:
    print("오류: 지원하지 않는 연산자입니다.")

if result is not None:
    print("결과:", result)

while True: 
    num1_str = input("첫 번째 숫자를 입력하세요 (종료하려면 'exit' 입력): ")
    if num1_str.lower() == 'exit': 
        break
    
    operator = input("연산자 (+, -, *, /, **, %) 를 입력하세요: ")
    num2_str = input("두 번째 숫자를 입력하세요: ")

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("오류: 잘못된 숫자 형식입니다. 다시 시도해주세요.")
        print("-" * 20)
        continue 

    result = None 

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("오류: 0으로 나눌 수 없습니다.")
        else:
            result = num1 / num2
    elif operator == '**': 
        result = num1 ** num2
    elif operator == '%': 
        if num2 == 0:
            print("오류: 0으로 나머지 연산을 할 수 없습니다.")
        else:
            result = num1 % num2
    else:
        print("오류: 지원하지 않는 연산자입니다.")

    if result is not None:
        print("결과:", result)
    
    print("-" * 20) 

print("계산기를 종료합니다.")