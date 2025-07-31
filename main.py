w=float(input("Enter the capacity of the solar panel:"))
eff=0.2 
hrs=float(input("Enter hrs of direct sunlight:"))
power=w*eff*hrs 
print("Electricity produced in 1 day by 1 solar panel="+str(power)+" watts")
