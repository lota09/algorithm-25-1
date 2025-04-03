import myqueue

'''*******************************************************************
  - Project          : algorithm_0331
  - File name        : MazeBFS.py
  - Description      : Maze PathFinder with Breadth-First Search algorithm
  - Owner            : Seokmin Kang
  - Revision history : 1) 2025.03.31 : Initial release
*******************************************************************'''

MAZE_COL = 5 #열
MAZE_ROW = 6 #행

#시작점
START = (0,1)

#미로 지도
MAZE = \
    [
        list("#####"),
        list("s    "),
        list("# # #"),
        list("#   #"),
        list("x## #"),
        list("     ")
    ]

#주변 위치가 유효한 위치인지 확인
def isValidPos(x,y):
    if 0 <= x < MAZE_COL and 0 <= y < MAZE_ROW :
        return MAZE[y][x] == ' ' or MAZE[y][x] == 'x'
    return False

def MazeBFS() :
    cq = myqueue.C_queue(4)
    cq.enqueue((0,1))  #출발 위치 (0,1)을 큐에 삽입
    print('너비 우선 탐색: ')

    while not cq.isEmpty(): 
        here = cq.dequeue()  #현재 위치를 큐에서 꺼낸다
        #print(here, end='->')
        x,y = here
        if (MAZE[y][x] == 'x') : return True   #미로 탈출 성공
        else :
            #발자국 남기기 - 방문 경로 표시
            MAZE[y][x] = '*'
            if isValidPos(x , y-1): # ↑
                cq.enqueue((x , y-1))
            if isValidPos(x+1 , y): # →
                cq.enqueue((x+1 , y))
            if isValidPos(x , y+1): # ↓
                cq.enqueue((x , y+1))
            if isValidPos(x-1 , y): # ←
                cq.enqueue((x-1 , y))

            print(f"현재위치 : {x},{y} - 현재큐 : {cq.q_list}")

    return False


if __name__ == "__main__":
    MazeBFS()
    #개선점 : 미로의 두 경로가 만나게 된다면 같은 위치가 중복으로 큐에 넣게되면서 중복탐색이 발생함.
    #큐 항목에 중복 항목을 넣지 못하게 하는 메서드를 넣어서 개선할 수 있음

