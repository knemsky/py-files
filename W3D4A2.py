#Kurtis Nemsky

Hours = int(input("Please enter the number of hours:"))
RPH = int(input("Please enter the rate per hour:"))

if Hours > 40:
	RPH2 = RPH*1.5
	GrossPay = (40*RPH) + ((Hours-40)*RPH2)
	print("Gross Pay = "+ str(GrossPay))
else:
	GrossPay = Hours*RPH
	print("Gross Pay = "+ str(GrossPay))
