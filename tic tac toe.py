choice=input("Do you wanna play tic tac toe [Yes(Y/y)/No(N/n):")

if choice == "Y" or choice == "y":
    a = "-"
    b = "-"
    c = "-"
    d = "-"
    e = "-"
    f = "-"
    g = "-" 
    h = "-"
    i = "-"
elif choice != "Y" or choice != "y":
    exit() 
def PRINT():
    print("     |     |     ")
    print(f"  {a}  |  {b}  |  {c}  ")
    print("-----|-----|-----")
    print(f"  {d}  |  {e}  |  {f}  ")
    print("-----|-----|-----")
    print(f"  {g}  |  {h}  |  {i}  ")
    print("     |     |    ")


PRINT()




