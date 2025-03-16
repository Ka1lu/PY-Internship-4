import random
import matplotlib.pyplot as plt

headcount = 0
tailcount = 0

while True:
    outcome = random.choice(["Heads", "Tails"])
    print(f"\nThe result is {outcome}")

    if outcome == "Heads":
        headcount += 1
    else:
        tailcount += 1

    print(f"\nTotal outputs in this session:\nHeads: {headcount} \nTails: {tailcount}")

    status = input("\nEnter '1' to retoss, any other key to exit: ")
    if status != '1':
        break

labels = ['Heads', 'Tails']
sizes = [headcount, tailcount]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['blue', 'orange'])
plt.title("Coin Toss Results")
plt.show()
