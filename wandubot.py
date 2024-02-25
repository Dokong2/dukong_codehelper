import sys
import os
import pickle
import pygame
pygame.init()

def next():
    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            break

def args():
    argv = sys.argv
    if len(argv) == 1:
        print("◜(ㅣ∇ㅣ)◞ <[완두콩 코드 봇입니다!]")
        try:
            with open("./data/data.kim", 'rb') as f:
                data = pickle.load(f)
        except:
            print("대화는 스페이스키로 넘기세요.")
            next()
            print("◜(ㅣoㅣ)> <[저를 처음 사용하시군요!]")
            next()
            print("◜(ㅣoㅣ)◞ <[그럼 절 사용할 매뉴얼을 알려드릴게요!]")
            next()
            print("◜(ㅣ∇ㅣ)◞/ <[1번째, 저를 명령 프롬포트에서 실행시키려면 먼저 [wandubot]을 입력합니다!]")
            next()
            print("◜(ㅣ∇ㅣ)◞/ <[2번째, 그리고 스페이스를 한번 누르고, 파이썬 파일을 만드려면 [python]을 입력,]")
            next()
            print("◜(ㅣ∇ㅣ)◞/ <[go 파일은 [go]를 입력하세요!]")
            next()
            print("◜(ㅣ∇ㅣ)◞/ <[그리고 또 스페이스를 한번 누른 뒤, 파일 이름을 입력하세요!]")
            next()
            print("◜(ㅣ∇ㅣ)◞/ <[그러면 알아서 웰컴 스크립트를 입력해드릴거에요!]")
            next()
            print("◜(ㅣ∇ㅣ)◞ <[설명은 이것으로 끝입니다!]")
            next()
            print("◜(ㅣ∇ㅣ)◞ <[그러면 절 이제 재시작해서 절 사용해보세요!]")
            next()
            print("◜(/ ∇ \)◞ <[잘가요!]")
            next()
            print("정보를 저장중입니다. 프로그램을 끄지 마세요..")
            with open('./data/data.kim', 'wb') as f:
                pickle.dump(data, f)


if __name__ == "__main__":
    args()