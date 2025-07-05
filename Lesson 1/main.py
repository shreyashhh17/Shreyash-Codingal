print("Hey! How are you?")
user_name = input("Your Response: ")

print("How may I help you?")
print("Do you have any assignments you're stuck on, or do you want to learn something?")
response = input("Type 'assignments': ")

if response == "assignments":
    subject = input("Which subject? (Maths/Science): ")
    
    if subject == "maths":
        print("Go ahead.")
        question = input("Enter your Maths question: ")
        print(f"I'll try to help you with: {question}")
        print("a^2 + b^2 + 2a")
        
    elif subject == "science":
        print("Ask your question.")
        question = input("Enter your Science question: ")
        print(f"I'll try to help you with: {question}")
        print("Light is a form of energy which helps our eyes to see")
        
    else:
        print("Sorry, I can only help with Maths or Science for now.")
        
else:
    day = input("How was your day today? ")
    print(f"Glad to hear your day was: {day}")

studies = input("How are your studies going on? ")
print(f"Thanks for sharing! You said: {studies}")

print("You have reached your limit, we will try tomorrow😊")

#git config --global user.name "shreyashhh17"

#git config --global user.email "cool.shreyash17@gmail.com"