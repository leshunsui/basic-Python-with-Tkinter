score = int(input("Enter Your Score:"))

grades = {
    range(0, 50): "F",
    range(50, 60): "D",
    range(60, 70): "C",
    range(70, 80): "B",
    range(80, 101): "A"
}

for ranges, grade in grades.items():
    if score in ranges:
        print(f"You Got Grade {grade}") #ผมใช้  f string ในการบอกค่าในวงเล็บที่ใส่ลงไป
        break
else:
    print("error")