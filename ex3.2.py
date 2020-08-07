sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, Enter numeric value")
    quit()
    

if fh > 40 :
    reg = fh*fr
    otp = (fh - 40.0)* (fr*0.5)
    xp = reg + otp

else:
    print("Regular")
    xp = fh*fr
print("Pay",xp)
