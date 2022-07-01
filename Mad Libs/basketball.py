def madlib():
    print("Basketball is the best ___ in the world\n")
    body_part = input("Body Part: ")

    madlib = f"\nBasketball is the best {body_part} in the world\n"

    if body_part == "sport":
        answer = "correct!"
    else:
        answer = "wrong!"

    print(madlib)
    print(answer)