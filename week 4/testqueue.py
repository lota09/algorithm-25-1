import myqueue

def test_LQ():
    lq = myqueue.L_queue()
    lq.enqueue(10)
    lq.enqueue(20)
    print(f"{lq.size()}개 : {lq.q_list}")
    print(lq.dequeue())
    print(lq.dequeue())
    print(f"{lq.size()}개 : {lq.q_list}")
    try:
        print(lq.dequeue())
    except Exception as e:
        print(e)

def test_CQ():
    cq = myqueue.C_queue(8)
    try:
        for i in range(9):
            cq.enqueue(i)
            print(f"[{cq.front}:{cq.rear}] : {cq.q_list}")
    except Exception as e:
        print(e)

    try:
        for i in range(9):
            cq.dequeue()
            print(f"[{cq.front}:{cq.rear}] : {cq.q_list}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_LQ()
    test_CQ()