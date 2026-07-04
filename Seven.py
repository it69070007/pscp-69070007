"""Seven"""
def main():
    """หาหลักหน่วย ของ 7 ยกกำลัง x"""
    x = int(input())
    n = x%4
    if n == 1:
        print(7)
    elif n == 2:
        print(9)
    elif n == 3:
        print(3)
    elif n == 4:
        print(1)
    elif not n:
        print(1)
main()
