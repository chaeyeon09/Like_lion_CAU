# 로또 한장의 가격 1000원
# 구입금액 입력 받기
# 랜덤 생성된 로또 출력하기
# 지난 주 당첨번호 입력받기
# 로또 당첨 결과 출력하기
# 수익률 출력하기

import random

lotto_numbers = []

lotto_prize = {1: 5000000, 2: 100000, 3: 20000, 4: 5000, 5: 3000, 6: 1000}
lotto_score = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}


def lotto_check(past_lotto_number):
    # 로또 1장을 구매했을 때 얻는 수익 / 랜덤함수를 이용해서 여기서 당첨금이 있을 수도 있고, 없을 수도 있음(=0)
    one_lotto = []
    for i in range(6):
        while True:
            output = random.randint(1, 45)
            if output not in one_lotto:
                one_lotto.append(output)
                break
    print(one_lotto)

    win_count = 0
    for i in range(6):
        if one_lotto[i] in past_lotto_number:
            win_count += 1

    if win_count < 1:
        print("less than 1 matched: wrong!")
        return 0
    else:
        print("you matched more than 1: matched " + str(win_count))
        score = lotto_score[win_count]
        print("you got " + str(score) + "rd(th) score")
        one_prize = lotto_prize[score]
        print("you got " + str(one_prize) + "dollor")

        return one_prize


def run():
    past_lotto_number = []
    for i in range(6):
        past_lotto_number.append(int(input("지난 주 lotto 번호를 입력해 주세요 : ")))

    money = int(input("구입 금액을 입력하세요: "))
    lotto_count = money // 1000
    benefit_rate = 0
    prize = 0
    for i in range(lotto_count):
        once_prize = lotto_check(past_lotto_number)
        prize += once_prize

    print("totally you got " + str(prize) + "dolloar")
    benefit_rate = prize / money
    print("수익률: " + str(benefit_rate))


def main():
    run()


if __name__ == "__main__":
    main()
