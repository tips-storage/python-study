from datetime import datetime

def calculate_korean_age():
    # 사용자 이름 입력 받기
    name = input("이름을 입력해 주세요: ")
    
    # 태어난 연도 입력 받기
    try:
        birth_year = int(input("태어난 연도를 입력해 주세요 (예: 1995): "))
    except ValueError:
        print("올바른 연도를 숫자로 입력해 주세요.")
        return
    # 현재 연도 가져오기
    current_year = datetime.now().year
    
    # 한국 나이 계산 (현재 연도 - 태어난 연도 + 1)
    korean_age = current_year - birth_year + 1
    
    print(f"\n{name}님, {current_year}년 기준 한국 나이는 {korean_age}세입니다.")

if __name__ == "__main__":
    calculate_korean_age()
