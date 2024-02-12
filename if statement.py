# eng = int(input("Eng: "))
# math = int(input("Math: "))

# if math > eng:
#     print("math is greater than eng")
# elif math < eng:
#     print("math is less than eng")
# else:
#     print("math is equal to eng")


# if eng > 0 and math > 0:
#     print("Both are positive.")
# elif eng < 0 or math > 0:
#     print("Math is positive.")
# elif eng > 0 or math < 0:
#     print("Eng is positive.")
# else:
#     print("zero.")


# if not math > eng:
#     print("math is either less or equal to eng.")


x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative change to zero.")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
