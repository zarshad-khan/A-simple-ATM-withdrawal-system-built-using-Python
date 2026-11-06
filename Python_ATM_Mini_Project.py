# =====================================
#       SIMPLE ATM WITHDRAWAL SYSTEM
#          Python Mini Project
# =====================================

Balance = 100000

print("=" * 40)
print("       WELCOME TO PYTHON ATM")
print("=" * 40)

print(f"\nAvailable Balance: Rs. {Balance}")

withdraw = int(input("\nEnter withdrawal amount: Rs. "))

if withdraw > Balance:
    print("\nTransaction Failed!")
    print("Reason: Insufficient Balance")

elif withdraw > 0 and withdraw <= Balance:
    remaining = Balance - withdraw

    print("\nTransaction Successful!")
    print("-" * 40)
    print(f"Withdrawn Amount : Rs. {withdraw}")
    print(f"Remaining Balance: Rs. {remaining}")
    print("-" * 40)
    print("Thank you for using Python ATM!")

else:
    print("\nInvalid Withdrawal Amount!")
    print("Please enter a positive amount.")

print("\n" + "=" * 40)
print("          HAVE A NICE DAY!")
print("=" * 40)