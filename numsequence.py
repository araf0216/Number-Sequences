def menu():
    print("Here are your choices:\n1 - Pentagonal Sequence\n2 - Heptagonal Sequence\n3 - Hendecagonal Sequence")

def pentagonal(sl):
    seq = []
    for v in range(sl):
        v += 1
        seq.append(int(((3 * (v ** 2)) - v) / 2))
    return seq

def heptagonal(sl):
    seq = []
    for v in range(sl):
        v += 1
        seq.append(int(((5 * (v ** 2)) - (3 * v)) / 2))
    return seq

def hendecagonal(sl):
    seq = []
    for v in range(sl):
        v += 1
        seq.append(int(((9 * (v ** 2)) - (7 * v)) / 2))
    return seq

def main():
    print("Welcome to the number sequence generator program!")
    menu()

    choice = int(input("Enter your choice (1 - 3): "))
    while choice not in range(1, 4):
        choice = int(input("Invalid entry. Re-enter your choice (1 - 3): "))
    
    seq_len = int(input("Enter the number of values for the list (>=3): "))
    while seq_len < 3:
        seq_len = int(input("Invalid entry. Re-enter the number of values for the list (>=3): "))
    
    if choice == 1:
        seq = pentagonal(seq_len)
        choice = "pentagonal"
    elif choice == 2:
        seq = heptagonal(seq_len)
        choice = "heptagonal"
    elif choice == 3:
        seq = hendecagonal(seq_len)
        choice = "hendecagonal"
    
    print(f"Here's a list containing the first {seq_len} numbers of the {choice} sequence: {seq}")

    odds = list(filter(lambda x: 0 if x % 2 == 0 else x, seq))

    print(f"And here is the list of odd pentagonal numbers: {odds}")
    
    repeat = input("Would you like to run the program again? Enter yes or no: ").lower()

    while repeat == "yes":
        main()
    else:
        print("Thanks for using the program! Goodbye!")

main()