date = input("Enter Today's Date: ")
mood = input("What is your mood today? ")
thoughts = input("Tell me your current thoughts:\n")

with open(f"files/{date}.txt", "w") as file:
    file.write(f"My mood for today is: {mood}\n\n")
    file.write(f"My thoughts for today were: \n{thoughts}")