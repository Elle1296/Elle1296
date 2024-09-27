
def computepay(hrs, rt):
        if hrs > 40: 
            reg_pay = 40 * rt
            ot_hrs = hrs - 40
            ot_pay = ot_hrs * (1.5 * rt)
            total_pay = reg_pay + ot_pay
            return total_pay
        elif hrs <= 40:  
            total_pay = hrs * rt
            return total_pay
        else:
            print("error")

for name in ("James", "Judy", "John"):
        hrs = float (input(f'{name}, please enter your weekly hours:'))
        rt = float(input('and your Pay Rate:'))
        
        print("Hours Entered:", hrs)
        print("Rate Entered:", rt)
        print(f"{name} receives ${computepay(hrs, rt):.2f}")
        print("All done")