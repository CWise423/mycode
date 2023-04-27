#!/usr/bin/python3

def main():
    q1 = " "
    q2 = " "
    q3 = " "
    q4 = " "
    q5 = " "
    q6 = " "
    q7 = " "
    q8 = " "
    q9 = " "
    q10 = " "

    score = 0
    while score < 10:

        q1 = input("Where can I buy a Beefy 5-layer Burrito?\n>").lower()
        answer = q1
        if q1 == "taco bell":
            print("Live Mas")
            score = score + 1
        else:
            print("No bueno. The answer is Taco Bell")
            score = score
        
        print(f"Score= {score}")

        q2 = input("Where can I order Chick-n-Minis for breakfast?\n>").lower()
        answer = q2
        if q2 == "chick-fil-a":
            print("I knew you eat that Gospel Chicken")
            score = score + 1
            
        elif q2 == "chickfila":
            print("I'll take it put it's actually spelled 'Chick-fil-a'.")
            score = score + 1

        else:
            print("I pray the Lord blesses you with Chick-fil-a's Gospel Chicken.")
            score = score
        print(f"Score =  {score}")
        q3 = input("If I want a Triple Whopper, where do I go?\n>").lower()
        answer = q3
        if q3 == "burger king":
            print("Have it your way.")
            score = score + 1

        else:
            print("Amateur. It's Burger King.")
            score = score

        print(f"Score= {score}")

        q4 = input("If someone wanted a Filet-O-Fish (ew), which restaurant would they visit?\n>").lower()
        if q4 == "mcdonalds":
            print("Those Double Arches == double chins.")
            score = score + 1

        else: 
            print("I'm happy that you didn't know this one. Gross!")
            score = score

        print(f"Score= {score}")

        q5 = input("Want bacon? Come to this restaurant for the Baconator!\n>").lower()
        if q5 == "wendys":
            print == ("Correct. And supposedly the patty is fresh, never frozen?!")
            score = score + 1
        else:
            print("Nope. Just for that, I'm eating your Wendy's Frostie!")
            score = score

        print(f"Score= {score}")

        q6 = input("Forget McDonalds' fries, you need those famous curly fries from....?\n>").lower()
        if q6 == "arby's":
            print("Did we just become best friends?")
            score = score + 1

        elif q6 == "arbys":
            print("Did we just become best friends?")
            score = score + 1

        else:
            print("They may have curly fries there, but Arby's are better.")
            score = score
        print(f"Score= {score}")

        q7 = input("Keep it all-American with a footlong chili-cheese dog from..?\n>").lower()
        if q7 == "sonic":
            print("Yes. You get a free Strawberry Limeade.")
            score = score + 1
        else: 
            print("Incorrect. Drive in to Sonic more often.")
            score = score

        print(f"Score= {score}")
    
        q8 = input("If you're hella hungry, visit this place for a Double-Double.\n>").lower()
        if q8 == "in-n-out":
            print("NorCal or SoCal, you're alright with me.")
            score = score + 1
    
        else:
            print("Nah. It's In-n-Out, bruh.")
            score = score

        print(f"Score= {score}")

        q9 = input("Home of the World-famous Chicken that comes in a bucket.\n>").lower()
        if q9 == "kfc":
            print("Colonel Sanders would be proud!")
            score = score + 1

        elif q9 == "kentucky fried chicken":
            print("Colonel Sanders would be proud!")
            score = score + 1

        else:
            print("Sorry, I think you meant to say Kentucky Fried Chicken.")
            score = score

        print(f"Score= {score}")

        q10 = input("A Southern chain that offers the Kickin' Chicken Sandwich.\n> ").lower()
        if q10 == "zaxbys":
            print("If you know, you know.")
            score = score + 1

        else:
            print("Bless your heart. You've never had Zaxbys?")
            score = score

        break

    print(f"You got {score} out of 10 right.")

main()
