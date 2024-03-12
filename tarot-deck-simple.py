#imports necessary modules
import random
from loguru import logger

#defines the deck
tarot_deck = ["0. The Fool", "I. The Magician", "II. The High Priestess", "III. The Empress", "IV. The Emperor",
    "V. The Hierophant", "VI. The Lovers", "VII. The Chariot", "VIII. Strength", "IX. The Hermit",
    "X. Wheel of Fortune", "XI. Justice", "XII. The Hanged Man", "XIII. Death", "XIV. Temperance",
    "XV. The Devil", "XVI. The Tower", "XVII. The Star", "XVIII. The Moon", "XIX. The Sun",
    "XX. Judgement", "XXI. The World", "Ace of Wands", "Two of Wands", "Three of Wands",
    "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands",
    "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands",
    "King of Wands", "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups",
    "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups",
    "Ten of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
    "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords",
    "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords",
    "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords", "Ace of Pentacles",
    "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles", "Six of Pentacles",
    "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles",
    "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles"]

#sets initial values and welcomes the user
pref = "Undefined"
restart = True
print("Welcome! Let's begin your card drawing.")

#loop until user inputs a valid preference
while pref == "Undefined":
    pref = input("Would you like to enable upright/reversed variants? (Yes/No): ").lower()
    if pref == "yes":
        pref = True
        break
    elif pref == "no":
        pref = False
        break
    else:
        print("Invalid answer! Please reply with Yes or No.")
        pref = "Undefined"
        continue

#Loop for drawing cards
while restart == True:
    number_of_cards = input("Input number of cards: ")

    #error if the input isn't a number
    if not number_of_cards.isdigit():
        print(f"Error! {number_of_cards} is not a number!")
        continue

    #if input is valid, prints drawn cards according to input and pref
    elif int(number_of_cards) in range(1,78):
        def draw_card(deck):
           return random.sample(deck, int(number_of_cards))
        card = draw_card(tarot_deck)
        if pref == True:
            for result in card:
                print(result, random.choice(["(Upright)", "(Reversed)"]))
        elif pref == False:
            for result in card:
                print(result)

    #handles other cases of invalid input
    elif int(number_of_cards) == 0:
        print("Error! You can't draw 0 cards!")
        continue
    elif int(number_of_cards) not in range(1,78):
        print("That's way too many cards! Please try again.")
        continue

    #asks if user wants to draw again
    cont = input("Would you like to draw again? (Yes/No): ").lower()
    if cont != "yes":
        print("Okay! See you soon!")
        restart = False
        break
