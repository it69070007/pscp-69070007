"""Colors"""
def main():
    """ผสมสี 2 สี จากแม่สีที่ให้มา แล้วตอบว่าได้สีอะไร"""
    c1 = input()
    c2 = input()
    if c1 == "Red" and c2 == "Yellow" or c2 == "Red" and c1 == "Yellow":
        print("Orange")
    elif c1 == "Red" and c2 == "Blue" or c2 == "Red" and c1 == "Blue":
        print("Violet")
    elif c1 == "Yellow" and c2 == "Blue" or c2 == "Yellow" and c1 == "Blue":
        print("Green")
    elif c1 == "Red" and c2 == "Red":
        print("Red")
    elif c1 == "Yellow" and c2 == "Yellow":
        print("Yellow")
    elif c1 == "Blue" and c2 == "Blue":
        print("Blue")
    else:
        print("Error")
main()
