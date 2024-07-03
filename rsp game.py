import random

best_score = float('inf') #최고 시도 횟수를 저장

#횟수를 저장할 변수
wins = 0
loses = 0
draws = 0

while True:
    rsp = ['가위', '바위', '보']

    rule = {'바위' : '보',
            '가위' : '바위',
            '보' : '가위'}
    while True:
        player_choice = input("가위, 바위, 보, 중 하나를 선택하세요.")
        if player_choice not in rsp:
            print("유효한 입력이 아닙니다.")
            continue
        com_choice = random.choice(rsp)

        if player_choice == com_choice:
            print(f"플레이어: {player_choice}, 컴퓨터: {com_choice}" "\n"
                "비겼습니다.")
            draws += 1
        elif rule[com_choice] == player_choice:
            print(f"플레이어: {player_choice}, 컴퓨터: {com_choice}" "\n"
                  "플레이어 승리!")
            wins += 1
            break
        else:
            print(f"플레이어: {player_choice}, 컴퓨터: {com_choice}" "\n"
                  "컴퓨터 승리!")
            loses += 1
            break

    # 게임 끝나고 다시 시작 여부
    game_end = input("게임을 다시 시작하겠습니까? (y/n): ").lower()
    if game_end == "n":
        print("게임을 종료합니다.")
        print(f"승: {wins} 패: {loses} 무승부: {draws}")
        break

