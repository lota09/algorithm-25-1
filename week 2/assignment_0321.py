def assignment2_1():
    args1=6
    for args2 in range(1,10):
        print(f"{args1} x {args2} = {args1*args2}")
    return

def assignment2_4(temp_c):
    temp_f=32+temp_c*180/100
    print(f"{temp_c}˚C는 화씨로 {temp_f:.2f}˚F 입니다.")
    return temp_f

if __name__ == "__main__":
    print(f"\n예제 2.1 :")
    assignment2_1()
    print(f"\n예제 2.4 :")
    assignment2_4(-18)
