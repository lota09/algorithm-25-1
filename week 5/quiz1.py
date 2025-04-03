import myqueue

def Q1():
    """1. 구구단 2-5단을 계산하여 결과를 순서대로 출력하는 코드를 for문을 이용하여 구현하라."""
    print("======== 문제 1 =========")
    for i in range(2,6):
        print(f"- 구구단 {i}단 -")
        for j in range(1,11):
            print(f"{i} * {j} = {i * j}")

def Q2():
    """2. 위 문제를 while 문을 이용하여 구현하라."""
    print("======== 문제 2 =========")
    i = 1
    while (i < 6):
        print(f"- 구구단 {i}단 -")

        j = 1
        while (j < 11):
            print(f"{i} * {j} = {i * j}")
            j +=1

        i +=1

def Q3(n):
    """3. 1부터 n까지 숫자를 전부 합하여 반환하는 함수를 작성하라."""
    print("======== 문제 3 =========")
    sum =0
    for i in range(1,n+1):
        sum +=i
    return sum


def Q4(n):
    cq = myqueue.C_queue(3)
    f1=0
    f2=1

    match n:
        case 1:
            return f1
        case 2:
            return f2
   
    if n < 3:
        raise IndexError("Only integers greater than 1 allowed")

    for i in range(n-2):
        cq.enqueue(f1)
        cq.enqueue(f2)
        f0 = cq.dequeue()
        f1 = cq.dequeue()
        f2 = f0 + f1

    return f2

if __name__ =="__main__":
    for i in range(1,10):
        print(Q4(i))
    try:
        print(Q4(0))
    except Exception as e:
        print(e)
