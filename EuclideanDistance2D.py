"""หาระยะทางแบบยุคลิคระหว่าง Q และ P"""
import math
def main():
    """คำนวณระยะทางแบบยุคลิค"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    print(math.sqrt(pow(q1-p1,2)+pow(q2-p2,2)))
main()
