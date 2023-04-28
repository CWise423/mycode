#!/usr/bin/python3

def main():
    
    print("How well do you know your fastfood menus?\n Find out by answering the questions using 1-4.\n")

    questions = {
            "question1": "Where can I buy a Beefy 5-layer Burrito?\n 1.McDonalds \n2.Taco Bell \n3.Taco Johns \n4.Long John Silvers\n",
            "question2": "Where can I order Chick-n-Minis for breakfast?\n 1.Burger King \n2.KFC \n3.Popeyes \n4. Chick-fil-a\n",
            "question3": "If I want a Tripple Whopper, where do I go?\n 1.Hardees \n2.McDonalds \n3.Burger King \n4.Wendy's\n",
            "question4": "If someone wanted a Filet-O-Fish (ew), which restaurant would they visit?\n 1.Burger King \n2.McDonalds \n3.Long John Silvers \n4.Captain D's\n",
            "question5": "Want bacon? Come to this restaurant for the Baconator!\n 1.Wendys \n2.McDonalds \n3.Arbys \n4.Burger King\n",
            "question6": "Forget McDonalds fries! You need those famous curly fries from...??\n 1.Chick-fil-a \n2.Arbys \n3.Popeyes \n4.Bojangles\n",
            "question7": "Keep it all-American with a footlong chili-cheese dog from..?\n 1.In-n-Out \n2.Carls Jr. \n3.Sonic \n4.Arbys\n",
            "question8": "If you're hella hungry, visit this place for a Double-Double.\n 1.McDonalds \n2.Whattaburger \n3.In-n-Out \n4.Don't screw this one up\n",
            "question9": "Home of the World-famous Chicken that comes in a bucket.\n> 1.Popeyes \n2.Bojangles \n3.Zaxbys \n4.KFC\n",
            "question10": "What Southern chain offers the Kickin Chicken Sandwich?\n 1.Popeyes \n2.Bojangles \n3.Zaxby's \n4.Chick-fil-a\n"

            }

    score = 0
    
    print(questions["question1"])
    answer = input(">")
    while True:    
        if answer == "2":
            print("Live Mas")
            score += 1
            break
        
        else:
            print("No bueno. The answer was Taco Bell.")
            break
        
    print(f"Score= {score}")

    print(questions["question2"])
    answer = input(">")
    while True:
        if answer == "4":
            print("I knew you eat that Gospel Chicken!")
            score += 1
            break

        else: 
            print("I pray the Lord blesses you with Chick-fil-a's Gospel Chicken!")
            break

    print(f"Score= {score}")
        
    print(questions["question3"])
    answer = input(">")
    while True:
        if answer  == "3":
            print("Have it your way.")
            score += 1
            break
        else:
            print("Amateur. It's Burger King.")
            break

    print(f"Score= {score}")

    print(questions["question4"])
    answer = input(">")
    while True:
        if answer == "2":
            print("Those Double Arches == double chins.")
            score += 1
            break

        else: 
            print("I'm happy that you didn't know this one. Gross!")
            break

    print(f"Score= {score}")

    print(questions["question5"])
    answer = input(">")
    while True:
        if answer  == "1":
            print == ("Correct. And supposedly the patty is fresh, never frozen?!")
            score += 1
            break

        else:
            print("Nope. Just for that, I'm eating your Wendy's Frostie!")
            break
    print(f"Score= {score}")

    print(questions["question6"])
    answer = input(">")
    while True:
        if answer  == "2":
            print("Did we just become best friends?")
            score += 1
            break

        else:
            print("They may have curly fries there, but Arby's are better.")
            break

    print(f"Score= {score}")

    print(questions["question7"])
    answer = input(">")
    while True:
        if answer == "3":
            print("Yes. You get a free Strawberry Limeade.")
            score += 1
            break

        else: 
            print("Incorrect. Drive in to Sonic more often.")
            break

        print(f"Score= {score}")
    
    print(questions["question8"])
    answer = input(">")
    while True:
        if answer == "3":
            print("NorCal or SoCal, you're alright with me.")
            score += 1
            break

        else:
            print("Nah. It's In-n-Out, bruh.")
            break

        print(f"Score= {score}")

    print(questions["question9"])
    answer = input(">")
    while True:
        if answer == "4":
            print("Colonel Sanders would be proud!")
            score += 1
            break

        else:
            print("Sorry, but the bucket of greasy goodness comes from KFC.")
            break

        print(f"Score= {score}")

    print(questions["question10"])
    answer = input(">")
    while True:
        if answer == "3":
            print("If you know, you know.")
            score += 1
            break

        else:
            print("Bless your heart. You've never had Zaxbys?")
            break

    print(f"You got {score} out of 10 right. Please play again...(and watch your cholesterol!")


main()
