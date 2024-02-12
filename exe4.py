print("Grades calculator.")
math = int(input("Math: "))
eng = int(input("Eng: "))
phy = int(input("Phy: "))
kisw = int(input("Kisw: "))
hist = int(input("Hist: "))

sum = (math + eng + phy + kisw + hist)
avg = sum/5
print(f"Sum : {sum}")
print(f"Avarage: {avg}")


if avg < 40 and avg >= 0:
    print("Grade E")
elif avg < 51 and avg >= 40:
    print("Grade D")
elif avg < 60 and avg >= 51:
    print("Grade C")
elif avg >= 60 and avg < 70:
    print("Grade B")
elif avg >= 70 and avg <= 100:
    print("Grade A")
else:
    print("invalid grade")