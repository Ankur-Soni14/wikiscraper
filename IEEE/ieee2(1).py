def contalpha(n):
    num = 65

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        # ABCDEFEDCBA
        for j in range(0, i+1):

            # explicitly converting to char
            ch = chr(num)

        # printing char value
            print(ch, end=" ")

        # incrementing at each column
            num = num + 1

    # ending line after each row
    print("\r")


n = 5
contalpha(n)
