
def assignment2_6():
    A=[1,2,3,4]
    for i in range(-1,-5,-1):
        print(f"A[{i}] = {A[i]}")
    return

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
