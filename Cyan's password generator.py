"""สร้างรหัสผ่านของผู้ใช้ตามเงื่อนไข"""
def main():
    """ความยาวตัวอักษร >= 5 คือเงื่อนไข 1"""
    name = input()
    surname = input()
    age = input()
    if len(name) >= 5 and len(surname) >= 5:
        print(name[:2]+surname[-1]+age[-1])
    else:
        print(name[0]+age+surname[-1])
main()
