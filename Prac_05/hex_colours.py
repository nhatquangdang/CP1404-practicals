colour = {"BROWN": "#a52a2a", "CORAL": "#a52a2a",
          "CORNFLOWERBLUE": "#a52a2a", "CYAN": "#00ffff", "DARKSALMON": "#e9967a"}
for key, value in colour.items():
    print("List of color: {}".format(key.title()))

picks = input("Enter a colour: ").upper()
while picks != "":
    if picks in colour:
        print("Your colour code is ", colour[picks])
    else:
        print("Try again")
    picks = input("Enter a colour: ").upper()
