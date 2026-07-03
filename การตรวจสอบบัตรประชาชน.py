"""ตรวจสอบบัตรประชาชน"""
def main():
    """ตรวจตัวเลขที่ป้อนต้องมีค่าเท่ากับ 13 หลัก"""
    num = input()
    lennum = len(num)
    if lennum == 13:
        print("yes")
    else:
        print("no")
main()
