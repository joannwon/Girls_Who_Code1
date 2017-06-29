print("I AM THE AGE WIZARD! What is your name?!!")
name = input()

print("TELL ME YOUR AGE!!")
age = input()

age = int(age)

if age >= 100:
    print("Wow you is oooold")
elif age >12 and age <20:
    print("You teens and your memes")
else:
    print("Under 100 years old? Back in my old days...")
    
print("I'm going to tell you something about yourself")
print("Your name is %s and your age is %d. Booyaaa!" %(name,age))
