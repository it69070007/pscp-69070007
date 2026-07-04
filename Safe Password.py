"""Safe Password"""
def main():
    """รหัสผ่านตู้เซฟเป็น H 4567"""
    c = input()
    n = int(input())
    if c == "H" and n == 4567:
        print("safe unlocked")
    elif c == "H":
        print("safe locked - change digit")
    elif n == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")
main()
