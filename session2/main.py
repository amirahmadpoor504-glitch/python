pay=float(input("enter your pay: "))
chile=input("Do you have children? (y / n):") or "n"
tax=0

if(pay>10_000_000 and pay<=25_000_000):
    tax=(pay-10_000_000) *0.1
    
elif(pay>25_000_000):
    tax=(15_000_000 * 0.1)+ ((pay-25_000_000)*0.2)


if(chile=="y"):
    tax-=500_000

total=pay-tax

print(f"total pay: {total}")