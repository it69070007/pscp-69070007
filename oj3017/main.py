"""Bill"""
def main():
    """คำนวณเงินทั้งหมดหลังจากได้รวมค่าบริการและ VAT 7%"""
    price = int(input())
    service = price*0.1
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    total = price + service
    vat = total*0.07
    total += vat
    print(f"{total:.2f}")
main()
