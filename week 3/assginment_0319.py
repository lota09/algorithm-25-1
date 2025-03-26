def element_sum(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

if __name__ == "__main__":
    arr = [10,30,20,60,50,40]
    print(element_sum(arr))
