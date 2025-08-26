import random
words = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(words)
user_choice = input("Guess the word: ")
if user_choice == chosen_word:
    print("You guessed it right!")      
else:
    print(f"Wrong guess! The correct word was {chosen_word}.")