# This is a simple Bill Splitter made by using input commands and simple arithmetic. You simply have to enter the data as asked in the terminal.

no_of_people = int(input("Among how many people are you splitting your bill?: "))
bill = float(input("what's the total amount of the bill?: "))
tip = float(input("How much tip are you going to give?: "))


total_bill_including_tip = bill + tip
share_of_each_person = total_bill_including_tip / no_of_people


print(f"Here is the share of each person: {round(share_of_each_person, 2)}")