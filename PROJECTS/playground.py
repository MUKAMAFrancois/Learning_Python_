bds={"john":"dec 3", "Alice":"apr9"}

while True:
        if bd=="":
            print("exited")
            break
        elif bd in bds.keys():
            print(f"{bd} has bd of {bds[bd]}")

        else:
            print(" doesn't exist, enter the one")
            bd=input(" enter:")
            bds[bd]=bd