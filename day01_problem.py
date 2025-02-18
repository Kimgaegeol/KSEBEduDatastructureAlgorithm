# guess number 예제를 자동화하고 로그파일(guess.txt)을 남기도록 코드를 수정하시오.
# 단 해당 프로그램이 로그시간을 갖도록 한다.

import random

def get_random_number(start_number, end_number) -> int:
    return random.randint(start_number, end_number)

def set_chance_logic(number) -> int:
    if number < 3:
        return 0
    elif number == 3:
        return 1
    else:
        chance = 0
        while(True):
            number = number // 2
            chance += 1
            if number == 0:
                return chance

def log_write(answer,chance,is_win):
    with open("log.txt", "a") as file:
        file.write(f"답 : {answer} | 남은 기회 : {chance} | 맞춤 여부 : {is_win} ")
        file.close()

def log_read(file_name):
    try:
        with open(file_name, 'r') as file:
            for txt in file.readlines():
                print(txt)
            file.close()
    except FileNotFoundError as err:
        print(f"생성된 파일이 없습니다. ({err})")

if __name__ == "__main__":
    while(True):
        mode = input("지금까지의 기록을 확인하시려면 'log'라고 써주세요 : ")
        if mode == "log":
            log_read("log.txt")

        start_number = 1
        end_number = int(input("숫자 맞추기 게임을 시작합니다.\n3 이상의 숫자를 입력해주셔야 합니다.\n숫자를 입력해주세요 : ")) + 1

        answer = random.randint(1, end_number)
        chance = set_chance_logic(end_number)

        while chance != 0:
            guess = (end_number+start_number) // 2
            print(f"추측한 숫자 : {guess}")
            if guess == answer:
                chance = chance - 1
                print(f'You win. Answer is {answer}')
                log_write(answer,chance,True)
                break
            elif guess > answer:
                chance = chance - 1
                end_number = (end_number+start_number) // 2
                print(f'{guess} is bigger. Chance left : {chance}')
            else:
                chance = chance - 1
                start_number = (end_number+start_number) // 2
                print(f'{guess} is lower. Chance left : {chance}')
        else:
            print(f'You lost. Answer is {answer}')
            log_write(answer, chance, True)

        mode = input("게임을 끝내시려면 'end'라고 써주세요 : ")
        if mode == "end":
            break