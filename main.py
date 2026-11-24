print("welcome to my argument program")
bill=int(input("Enter the total amount of the bill: "))
tip_percentage=int(input("Enter the tip percentage: "))
def totat_amount(bill, tip_percentage):
    totat_bill=bill*(1+0.01*tip_percentage)
    totat_bill=round(totat_bill,2)
    print("The total bill is: ",totat_bill, " please pay the full amount")
totat_amount(bill,tip_percentage)