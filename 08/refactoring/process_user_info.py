"""
# 요구사항 
- 사용자 정보 처리 (name, age, city)
    - 환영 메시지를 생성
    - 사용자의 나이에 따라 특정 할인율을 적용
    - 사용자 이름을 포함한 작별 메세지를 생성
"""


def create_farewell_message(user_name):
    return f"안녕히 가세요, {user_name}님!"


def create_welcome_message(name, city):
    return f"환영합니다, {name}님! {city}에서 오셨군요!"


def calculate_discount(age):
    if age < 18:
        return 0.1  # 10% 할인
    elif age <= 25:
        return 0.05  # 5% 할인
    else:
        return 0


class UserInfoProcessor:
    def __init__(self, user):
        self.user = user

    def get_welcome_message(self):
        return create_welcome_message(self.user["name"], self.user["city"])

    def get_discount(self):
        return calculate_discount(self.user["age"])

    def get_bye_message(self):
        return create_farewell_message(self.user["name"])

    def process(self):
        welcome_message = self.get_welcome_message()
        discount = self.get_discount()
        bye_message = self.get_bye_message()

        return welcome_message, discount, bye_message


def main():
    user = {"name": "지수", "age": 23, "city": "서울"}
    processor = UserInfoProcessor(user)
    message, discount, bye_message = processor.process()
    print(message, discount, bye_message)


if __name__ == "__main__":
    main()
