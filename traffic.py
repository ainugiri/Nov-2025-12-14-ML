def action(signalcolor):
    if signalcolor == 'red':
        print("stop")
    elif signalcolor==    "yellow":
        print("caution")
    elif signalcolor == "green":
        print("Move Forward")

signalcolor = input("Enter the signal color (red, yellow, green): ") 
action(signalcolor)

# rulebased system : set of if then rules
