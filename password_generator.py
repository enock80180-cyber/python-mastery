# Project #59: Random Password Generator (Using the Random Toolbox)
import random  # 👈 Loading the random choice toolbox!

def generator_password(username):
    # A list of cool secret adjectives
    adjectives = ["Secret", "Crypto", "Matrix", "Cyber", "Shadow"]
    #Pick one random word from our list
    chosen_word = random.choice(adjectives)

    # Generate a random 3-digit number between 100 and 999
    random_number = random.randint(100, 999)

    # Combine them all together cleanly using an f-string 
    return f"{username}_{chosen_word}{random_number}"

print("🔐 Secure Password Generator Online\n")

#let's generate password for two different usernames 
pass_1 = generator_password("Alex")
pass_2 = generator_password("Coder")

print(f"Generated Password 1: {pass_1}")
print(f"Generated passwprd 2: {pass_2}")
