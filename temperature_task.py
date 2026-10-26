userInput = str(input("Is the temp warm, cool or cold?  "))
userInput = userInput.lower().strip()
if userInput == "cool":
    print("We wont need a jacket today, its warm outside")
elif userInput == "warm":
    print("We wont need a jacket today, its warm outside")
elif userInput == "cold":
    print("We will need a jacket today, its cold outside")
else:
    print("sorry we dont have a explanation for that temperature, please check the input and try again2")
