import os

# 스택 구현
class stack:
    def __init__(self):
        self.s_list=[]

    def push(self,item):
        self.s_list.append(item)

    def pull(self):
        return self.s_list.pop()
    
    def isEmpty(self):
        return self.s_list.__len__() == 0 
    
    def size(self):
        return self.s_list.__len__()
    
    def clear(self):
        self.__init__()

# 회문 검사
def isPalindrome(string):
    s = stack()
    for ch in string:
        s.push(ch)

    for ch in string:
        if ch != s.pull():
            return False
    
    return True

# 텍스트 역순 출력
def getReversed(string):
    s = stack()
    result = []
    for ch in string:
        s.push(ch)
    
    while not s.isEmpty():
        result.append(s.pull())
    
    return "".join(result)

# 파일 읽기
def readlnFile(file_path):
    if not os.path.exists(file_path):
        return None
    
    with open(file_path,'r',encoding='utf-8') as file:
        return file.readline().strip()

#예제 4.12
def assignment4_12():
    """
    예제 4.12 : 정수를 이진수로 변환하여 출력하는 함수.
    """
    s = stack()
    n = 4096
    while n > 0:
        s.push(n%2)
        n = n//2
    while not s.isEmpty():
        print(s.pull(),end="")
    print("\n")

#예제 4.13
def assignment4_13_A():
    s = stack()
    for i in range(10):
        if i%3 == 0:
            s.push(i)

    print(f"예제 4.13 - A 스택 리스트 항목 : {s.s_list}")

def assignment4_13_B():
    s = stack()
    for i in range(20):
        if i%3 == 0:
            s.push(i)
        elif i%4 == 0:
            s.pull()

    print(f"예제 4.13 - B 스택 리스트 항목 : {s.s_list}")


if __name__ == "__main__":
    # 스택 실습 : 스택구현, 회문검사, 텍스트 역순 출력
    print("---- 스택 실습 ----")

    file_path = "stack.txt"
    str_lst = ["hello!","level",f"{readlnFile(file_path)}"]

    for string in str_lst:
        print(f"{string} 의 회문 검사 결과: {isPalindrome(string)}")
        print(f"{string} 의 역순 출력 결과: {getReversed(string)}")
        print()
    
    # 예제 4.12 : 정수를 이진수로 변환하여 출력하는 함수.
    print("---- 예제 4.12 ----")
    print(assignment4_12.__doc__.strip())
    assignment4_12()

    # 예제 4.13
    print("---- 예제 4.13 ----")
    assignment4_13_A()
    assignment4_13_B()