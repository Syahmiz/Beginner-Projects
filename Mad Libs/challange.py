def madlib():
    print("If you're going to challange a couple to a chicken fight during spring break, make sure they're more ___ than you!\n")
    adjective = input("Adjective: ")

    madlib = f"\nIf you're going to challange a couple to a chicken fight during spring break, make sure they're \
    more {adjective} than you!\n"

    if adjective == "weaker":
        answer = "correct!"
    else:
        answer = "wrong!"

    print(madlib)
    print(answer)