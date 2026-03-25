# 能被 4 整除的年份是闰年，但是能被 100 整除的年份不是闰年，除非它能被 400 整除。

def panduan(a):
    if a%4==0:
        if a%100==0:
            if a%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(panduan(2000))
print(is_leap_year(2000))
   
 
    
 

