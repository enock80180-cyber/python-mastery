import random

# 1. Our list of possible answers
answers = ["Yes, absolutely!", "Ask again later", "Definitively no.", "Most likely!", "Outlook not so good"]

#2. Ask the player for a question
question = input("🎱 Ask the Magic 8-ball a question: ")

# 3. Pick a random answer from our list 
reply = random.choice(answers)

# 4. Show the result
print("\n🎱 Magic 8-Ball say:" + str(reply))
