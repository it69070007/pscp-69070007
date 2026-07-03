"""แสดงค่า string ในกรอบรูปสี่เหลี่ยม"""
def main():
    """แสดงค่า string"""
    s = input()
    for _ in range(len(s)+2):
        print("*",end="")
    print(f"\n*{s}*")
    for _ in range(len(s)+2):
        print("*",end="")
main()
