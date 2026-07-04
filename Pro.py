"""โปรส่วนลดร้านอาหาร"""
def main():
    """มา x คน จ่าย y คน คนละ a บาท"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    if z >= x:
        n = int(z/x)
        total = (y*n*a)+((z-x*n)*a)
    else:
        total = z*a
    print(total)
main()
