x=input("Is Mr. X alive?") #Asking the user for input
try:
    if x.lower() == "no" or x.lower() == "nope":
        print("Om shanti!")
    else:
        print("Stay safe from Covid-19")
except:
    print("Please write Yes or No") #Telling the user to type either "Yes" or "No"
