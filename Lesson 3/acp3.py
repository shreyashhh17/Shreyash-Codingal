import re, random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Cuisine and joke data
cuisines = {
    "indian": ["Butter Chicken", "Paneer Tikka", "Masala Dosa"],
    "chinese": ["Kung Pao Chicken", "Spring Rolls", "Chow Mein"],
    "italian": ["Pizza", "Pasta", "Risotto"]
}

jokes = [
    "Why did the tomato blush? Because it saw the salad dressing!",
    "What did the hungry clock do? It went back four seconds!",
    "I’m on a seafood diet. I see food and I eat it!"
]

# Normalize input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Suggest food based on cuisine
def suggest_food():
    print(Fore.CYAN + "FoodBot: What cuisine do you like? (Indian, Chinese, Italian)")
    choice = input(Fore.YELLOW + "You: ")
    choice = normalize_input(choice)

    if choice in cuisines:
        dish = random.choice(cuisines[choice])
        print(Fore.GREEN + f"FoodBot: You might love {dish}!")
        print(Fore.CYAN + "FoodBot: Would you like another suggestion? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            suggest_food()
        elif answer == "no":
            print(Fore.GREEN + "FoodBot: Hope you enjoy your meal!")
        else:
            print(Fore.RED + "FoodBot: I'll suggest again.")
            suggest_food()
    else:
        print(Fore.RED + "FoodBot: Sorry, I don’t know that cuisine.")
        suggest_food()

    show_help()

# Dining etiquette tips
def etiquette_tips():
    print(Fore.CYAN + "FoodBot: Dining etiquette tips:")
    print(Fore.GREEN + "- Always say please and thank you.")
    print(Fore.GREEN + "- Don’t talk with your mouth full.")
    print(Fore.GREEN + "- Start eating only after everyone is served.")
    print(Fore.GREEN + "- Use cutlery appropriately.")
    print(Fore.GREEN + "- Avoid loud chewing.")

# Tell a joke
def tell_joke():
    print(Fore.YELLOW + f"FoodBot: {random.choice(jokes)}")

# Help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest food (say 'suggest' or 'recommend')")
    print(Fore.GREEN + "- Give dining etiquette tips (say 'etiquette')")
    print(Fore.GREEN + "- Tell a food joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to leave me.\n")

# Main chatbot loop
def chat():
    print(Fore.CYAN + "Hello! I’m FoodBot, your dining buddy!")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!\n")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            suggest_food()
        elif "etiquette" in user_input or "tip" in user_input:
            etiquette_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.RED + "FoodBot: Bon Appétit! Have a delicious day!")
            break
        else:
            print(Fore.CYAN + "FoodBot: Hmm... could you rephrase that?")

# Run the bot
if __name__ == "__main__":
    chat()


#git config --global user.name "shreyashhh17"

#git config --global user.email "cool.shreyash17@gmail.com"