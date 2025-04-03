'''*******************************************************************
  - Project          : algorithm_0326
  - File name        : MazeDFS.py
  - Description      : Maze PathFinder with Depth-First Search algorithm
  - Owner            : Seokmin Kang
  - Revision history : 1) 2025.03.26 : Initial release
*******************************************************************'''
import stack

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

#깊이 우선 탐색 알고리즘 - 미로탐색 함수
def MazeDFS():
    s = stack.stack()
    s.push(START)
    
    while not s.isEmpty():
        x,y = s.pull()

        if (MAZE[y][x] == 'x'):
            print(f"목적지를 찾았습니다 : {x},{y}")
            return True
        
        #발자국 남기기 - 방문 경로 표시
        MAZE[y][x] = '*'

        #스택은 후입선출 : ↓ → ↑ ← 순으로 탐색
        if isValidPos(x-1 , y): # ←
            s.push((x-1 , y))
        if isValidPos(x , y-1): # ↑
            s.push((x , y-1))
        if isValidPos(x+1 , y): # →
            s.push((x+1 , y))
        if isValidPos(x , y+1): # ↓
            s.push((x , y+1))

        print(f"현재위치 : {x},{y} - 현재스택 : {s.s_list}")
        
    print("목적지를 찾을 수 없습니다.")
    return False


if __name__ == "__main__":
    MazeDFS()