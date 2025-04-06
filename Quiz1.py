def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:")

    questions=[
        "1.What is the largest animal on Earth?: a.Blue Whale, b.Mouse, c.Cat\n ",
        "2.Which bird can fly backwards?: a. Cuckoo, b.Eagle, c.Hummingbird\n",
        "3.What is the only mammal capable of flight? a.Bat, b.Squirrel, c.Dolphin\n "
    ]
    answers=[
        "Blue Whale",
        "Hummingbird",
        "Bat"
    ]
    score=0

    for i in range(len(questions)):
        user_answer=input(questions[i]).strip().lower()
        if user_answer.lower()==answers[i].lower():
            print("Correct!")
            score+=1
        else:
            print("Incorrect!")

    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

quiz()
