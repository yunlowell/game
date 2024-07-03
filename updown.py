import random  # 랜덤의 숫자 생성

best_score = float('inf') #최고 시도 횟수를 저장

while True:
    random_num = random.randint(1, 100)
    tries = 0 #시도 횟수 세려고 넣은 변수

    if best_score != float('inf'):
        print(f"이전 최고기록은 {best_score}번 입니다.")

    while True:
        player_num = int(input("숫자를 입력 하세요."))

        if player_num < 1 or 100 < player_num:
            print("유효한 숫자만 입력해 주세요. 1~100")
            continue
        tries += 1

        if random_num > player_num:
            print("업")
        elif random_num < player_num:
            print("다운")
        else:
            print(f"정답 입니다! {tries}번 시도했습니다.")

            #최고 시도 횟수 업데이트 하기
            if tries < best_score:
                best_score = tries
            break

    #게임 끝나고 다시 시작 여부
    game_end = input("게임을 다시 시작하겠습니까? (y/n)")
    if game_end == "n":
        print("게임을 종료합니다.")
        break

    #최고 시도 횟수 출력
    print(f"지금까지의 최고 시도 횟수는 {best_score}번 입니다.")
