
import random

# 정답 숫자 3개 생성 (중복 없이)
answer = random.sample(range(1, 10), 3)

print("=== 숫자야구 게임 ===")
print("서로 다른 숫자 3개를 맞혀보세요!")
print("스트라이크: 숫자와 위치가 모두 같음")
print("볼: 숫자는 같지만 위치가 다름")
print()

count = 0

while True:
    guess = input("숫자 3개 입력: ")

    # 입력 검사
    if len(guess) != 3 or not guess.isdigit():
        print("숫자 3개를 입력해주세요!")
        continue

    if len(set(guess)) != 3 or '0' in guess:
        print("1~9 사이의 중복 없는 숫자를 입력하세요!")
        continue

    guess = [int(n) for n in guess]
    count += 1

    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    print(f"{strike} 스트라이크 {ball} 볼")

    if strike == 3:
        print(f"\n정답입니다! 총 {count}번 만에 맞혔습니다!")
        break
