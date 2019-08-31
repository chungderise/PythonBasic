import math
import fractions
try:
    print("Phương trình bậc 2: ax2 + bx + c = 0")
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    c = float(input("Nhập số c: "))
    denta = (b**2) - (4*a*c)

    if a == 0:
        if (b== 0 and c == 0) or (b ==0 and c != 0):
            print("Phương trình vô nghiệm")
        else:
            x = c/b
            result = "Phương trình có một nghiệm duy nhất: " + str(x)
            print(result)
    elif a != 0:
       if denta < 0 :
           print("Denta = " + str(denta) + "< 0")
           print("Phương vô nghiêm")
       elif denta == 0:
           print("Denta = " + str(denta) + "= 0")
           x = (-b)/2*a
           xfra = fractions.Fraction(x)
           result = "Phương trình có nghiệm kép: x1=x2=" + str(xfra)
           print(result)
       elif denta > 0 :
           print("Denta = " + str(denta) + "> 0")
           x1 = (-b + math.sqrt(denta))/(2*a)
           x1fra = fractions.Fraction(x1)
           x2 = (-b - math.sqrt(denta))/(2*a)
           result = "Phương trình có 2 nghiệm phân biệt: x1=" + str(x1fra) + " x2 = " + str(x2)
           print(result)
    else:
        print("Phương trình không hợp lệ!")
except Exception as e:
    print("Nỗi nhập dữ liệu: " ,str(e))