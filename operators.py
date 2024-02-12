math = int(input("Math: "))
eng = int(input("Eng: "))
phy = int(input("Phy: "))
kisw = int(input("Kisw: "))
comp = int(input("Comp: "))

sum = math + eng + phy + kisw + comp
modulus = eng % math
avg = sum / 5

print(f"Total is {sum}.")
print(f"Modulus is {modulus}.")
print(f"Mean grade is {avg}")
