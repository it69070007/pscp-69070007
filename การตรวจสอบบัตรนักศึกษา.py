"""ตรวจสอบรหัสประจำตัว"""
def main():
    """รหัสหลักที่ 3 และ 4 คือ '1' และ '6'"""
    num = input()
    if num[2] == '1' and num[3] == '6':
        print("yes")
    else:
        print("no")
main()
