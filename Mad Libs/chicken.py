def madlib():
    print("What came first, the chicken or the ___?\n")
    noun = input("Noun: ")

    madlib = f"\nWhat came first, the chicken or the {noun}?\n"

    if noun == "egg":
        answer = "correct!"
    else:
        answer = "wrong!"

    print(madlib)
    print(answer)