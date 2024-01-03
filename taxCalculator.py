cmp = input("Enter your company name: ")
amount = int(input("Enter a tax amount: "))
per = int(input("Enter a tax percentage: "))

res1 = amount
res2 = per

cal = (res1*res2/100)
print(f'{cmp}  tax amount to pay is : {cal}')