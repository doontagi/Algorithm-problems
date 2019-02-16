TestCase = int(input()) # 테스트 케이스 정하기
Team = list(range(8))
WA = list(range(8))


for _ in range(TestCase): # 테스트 케이스 반복문
    for _ in range(0,8):
        Team[_] = input().split() # Team[] 이라는 변수에 팀정보 담기

    MyTeam = input() # 내가 응원하는팀 변수인덱스 생성
    RemainR = int(input()) # 잔여경기수 정하기
    VS = list(range(RemainR))

    for _ in range(0,8) : # Team[_][0]에는 팀이름, Team[_][1]에는 팀의 승리횟수, Team[_][2]에는 팀의 무승부+패배 횟수가 들어가있다
        Team[_][2] = int(Team[_][2]) + int(Team[_][3])

    for _ in range(RemainR) : # 남은경기 대진표 목록이 들어가는 VS 변수
        VS[_] = input().split()


    for a in range(RemainR) : # 
        if VS[a][0] == MyTeam or VS[a][1] == MyTeam : # VS[a] 대진표에 내가 응원하는 팀이 들어가있을 경우
            if VS[a][0] == MyTeam :
                for b in range(8) : 
                    if VS[a][0] == Team[b][0] :
                        Team[b][1] = int(Team[b][1]) + 1
                    if VS[a][1] == Team[b][0] :
                        Team[b][2] = int(Team[b][2]) + 1
            else :
                for b in range(8) :
                    if VS[a][1] == Team[b][0] :
                        Team[b][1] = int(Team[b][1]) + 1
                
                for b in range(8) :
                    if VS[a][0] == Team[b][0] :
                        Team[b][2] = int(Team[b][2]) + 1

        else : # VS[a] 대진표에 내가 응원하는 팀이 들어가 있지 않을 경우
            for b in range(8) :
                if VS[a][0] == Team[b][0] :
                    Team[b][2] = int(Team[b][2]) + 1
                if VS[a][1] == Team[b][0] :
                    Team[b][2] = int(Team[b][2]) + 1
 
    for _ in range(0,8) : # 내가 응원하는 팀에 색인 넣기
       if Team[_][0] == MyTeam :
           Obj = _

    for _ in range(0,8): # 각 팀의 승률을 계산하는 과정
        if int(Team[_][1]) == 0 and int(Team[_][2]) == 0 :
            WA[_] = 0
            continue
        else :
            WA[_] = int(Team[_][1]) / (int(Team[_][1]) + int(Team[_][2]))

    MObj = WA[Obj]
    MWA = list(set(WA))
    MWA.sort()
    MWA.reverse()

    for _ in range(len(MWA)) :
        if MWA[_] == MObj :
            if _ <= 3 :
                print("YES")
            else:
                print("NO")
                break;
