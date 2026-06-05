# Here is a simple marks calculator by using an input function.

Telugu = int(input("Enter Your Telugu marks here: "))
Hindi = int(input("Enter Your Hindi marks here: "))
English = int(input("Enter Your English marks here: "))
Maths = int(input("Enter Your Maths marks here: "))
Science = int(input("Enter Your Science marks here: "))
Social = int(input("Enter Your Social marks here: "))

Total_Marks = Telugu + Hindi + English + Maths + Science + Social

Percentage = ( Total_Marks / 600 ) * 100

print(f"Here are Your Total marks: {Total_Marks}"  )
print(f"And ")