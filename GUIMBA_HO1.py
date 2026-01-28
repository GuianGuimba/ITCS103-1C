Words = input("Enter a Word: ").title()
Strip_Words = Words.strip() 
Length = len(Strip_Words)
Inlist = []

print(f"Enter a number {Length} times.\n")

for i in range(1,Length+1,1):
    try:
        number = int(input(f"Enter a number ({i}) : "))
        Inlist.append(number)
        break
    except ValueError:
        Inlist.append(1)
    
average = sum(Inlist) / Length

print(f"\n{Inlist}")
print(f"\nThe average number you input is {average}")
print(f"The Length of your word ({Words}) is {Length}")

if average > Length:
    print(f"The length of the word '{Words}' is greater than average\n")
else:
    print(f"The length of the word '{Words}' is less than average\n")
