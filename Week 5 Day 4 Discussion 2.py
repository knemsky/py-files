#Kurtis Nemsky
def computepay(hours,rate):
    if hours > 40:
        RPH2 = rate*1.5
        GrossPay = (40*rate) + ((hours-40)*RPH2)
        print("Hours: "+ str(hours))
        print("Gross Pay = "+ str(GrossPay))
    else:
        GrossPay = hours*rate
        print("Hours: "+ str(hours))
        print("Gross Pay = "+ str(GrossPay))

computepay(45,10)