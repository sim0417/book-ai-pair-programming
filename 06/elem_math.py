import random


def create_math_problem(max_value=10):
    # 문제 유형 결정 (0: 덧셈, 1: 뺄셈, 2: 곱셈, 3: 나눗셈)
    problem_type = random.randint(0, 3)

    # 숫자 두 개를 랜덤으로 선택
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)

    if problem_type == 0:  # 덧셈 문제
        question = f"{num1} + {num2} = ?"
        answer = num1 + num2
    elif problem_type == 1:  # 뺄셈 문제
        num1, num2 = max(num1, num2), min(num1, num2)  # 결과가 음수가 되지 않도록 조정
        question = f"{num1} - {num2} = ?"
        answer = num1 - num2
    elif problem_type == 2:  # 곱셈 문제
        question = f"{num1} × {num2} = ?"
        answer = num1 * num2
    else:  # 나눗셈 문제
        # 나누어 떨어지는 결과를 얻기 위해 곱셈 결과에서 출발
        answer = random.randint(1, max_value)
        num1 = num2 * answer
        question = f"{num1} ÷ {num2} = ?"

    return question, answer


def create_multiple_math_problems(num_problems=10, max_value=10):
    problems_and_answers = []
    for _ in range(num_problems):
        question, answer = create_math_problem(max_value)
        problems_and_answers.append((question, answer))
    return problems_and_answers


# 사용자 입력 처리
try:
    n = input("생성할 문제의 개수를 입력하세요 (기본값 10): ")
    n = int(n) if n else 10  # 입력값이 없으면 기본값 10 사용
except ValueError:
    print("유효하지 않은 입력입니다. 기본값 10을 사용합니다.")
    n = 10

# 문제 생성 및 출력
problems_and_answers = create_multiple_math_problems(n, 10)
for i, (question, answer) in enumerate(problems_and_answers, start=1):
    print(f"{i}. 문제: {question} 정답: {answer}")
