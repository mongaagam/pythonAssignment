a = int(input("Enter a number: "))
print(f"Multiplication table of {a}:")

try:
    for i in range(1, 11):
        print(f"{a} X {i} = {a * i}")

    raise ExceptionGroup(
        "Errors",
        [ValueError("Wrong Value")]
    )

except* ValueError:
    print("Exception handled")
