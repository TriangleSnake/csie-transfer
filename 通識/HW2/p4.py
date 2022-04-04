height=eval(input("Height: "))
age=eval(input("Age: "))
if height>120:
    price=400
else:
    price=150
if age>=65:
    price*=0.5
elif (age+height)%6==0:
    price*=0.7
print("入場費=",price)