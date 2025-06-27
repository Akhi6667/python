name = input("Enter student's name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
total = subject1 + subject2 + subject3
average = total / 3

if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
else:
    grade = 'F'
print("\n--- Student Report ---")
print(f"Name      : {name}")
print(f"Total     : {total}")
print(f"Average   : {average:.2f}")
print(f"Grade     : {grade}")