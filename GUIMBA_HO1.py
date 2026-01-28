Words = input("Enter a Word: ").title()
Strip_Words = Words.strip() 
Length = len(Strip_Words)
Inlist = []

print(f"Enter a number {Length} times.\n")

for i in range(1,Length+1,1):
    number = int(input("Enter a number: "))
    Inlist.append(number)

average = sum(Inlist) / Length

print(f"\n{Inlist}")
print(f"\nThe average number you input is {average}")
print(f"\nThe Length of your word ({Words}) is {Length}")

if average > Length:
    print(f"The average is greater than the amount of letter")
else:
    print(f"The average is less thab the amount of letter")
