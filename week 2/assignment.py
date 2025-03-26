def assignment2_1():
    args1=6
    for args2 in range(1,10):
        print(f"{args1} x {args2} = {args1*args2}")
    return

def assignment2_2():
    args1=6
    args2=1
    while args2 < 10:
        print(f"{args1} x {args2} = {args1*args2}")
        args2+=1
    return

def assignment2_3():
    args1=6
    for args2 in range(9,0,-1):
        print(f"{args1} x {args2} = {args1*args2}")
    return

def assignment2_4(temp_c):
    temp_f=32+temp_c*180/100
    return temp_f

def assignment2_5(temp_f):
    temp_c=(temp_f-32)*100/180
    return temp_c

def assignment2_6():
    A=[1,2,3,4]
    for i in range(-1,-5,-1):
        print(f"A[{i}] = {A[i]}")
    return

def assignment2_7(arr):
    sum=0
    for item in arr:
        sum+=item
    return sum

def assignment2_8():
    msg = "Data Structures in Python"
    print(msg)
    print(msg.upper())
    print(msg.lower())
    return

def assignment2_9():
    price = {
        '콩나물해장국':4500,
        '갈비탕':9000,
        '돈가스':8000
    }
    price['팟타이']=7000
  
    for k in price.keys():
        print(f"{k} : {price[k]}원")
    return

def assignment2_10():
    price = {
        '콩나물해장국':4500,
        '갈비탕':9000,
        '돈가스':8000,
    }
    price['팟타이']=7000
  
    for k in price.keys():
        price[k]-=500
        print(f"{k} : {price[k]}원")
    return

if __name__ == "__main__":
    assignment2_10()
    #print(assignment2_4(30))
    #print(assignment2_5(86))
    #print(assignment2_7([1,2,3,5]))