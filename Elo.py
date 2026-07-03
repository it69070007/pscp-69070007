"""Elo rating system"""
def main():
    """คำนวณ EA EB"""
    RA = int(input())
    RB = int(input())
    s = input()
    if s == 'A':
        EA = 1/(1+10**((RB-RA)/400))
        print(f"{EA:.2f}")
    elif s == 'B':
        EB = 1/(1+10**((RA-RB)/400))
        print(f"{EB:.2f}")
main()
