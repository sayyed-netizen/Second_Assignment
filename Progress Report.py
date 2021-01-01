Roll_no = int(input("Please Enter Your Roll No: "))
Name = input("Please enter Your Name:")
English = float(input(" Please enter English Marks: "))
Math = float(input(" Please enter Math score: "))
Computers = float(input(" Please enter Computer Marks: "))
Physics = float(input(" Please enter Physics Marks: "))
Chemistry = float(input(" Please enter Chemistry Marks: "))
Biology = float(input(" Please enter Biology Marks: "))

total = English + Math + Computers + Physics + Chemistry + Biology
percentage = (total / 600) * 100
print("Roll Number:",Roll_no)
print("Name:",Name)
print("Total Marks = %.2f"  %total)
print("Marks Percentage = %.2f"  %percentage)

if(percentage >= 80):
    print("A Grade")
elif(percentage >= 60):
    print("B Grade")
elif(percentage >= 50):
    print("C Grade")
elif(percentage >= 40):
    print("D Grade")
else:
    print("Promoted")
