import random
import time


# Tells the user welcome to the game
print("Welcome to Guess the Number Between 1-100")
print("")


# This main function is where all the code and logic goes 
def main():
   while True:
      counter = 0

      time.sleep(1)

      random_number = random.randrange(1,100)

      player_guess = int(input("Guess the number between 1-100:"))
      
      # Checks if the player guess is within 1-100
      while player_guess > 100:
         if player_guess > 100:
            print("Invalid input, please try again!")
            player_guess = int(input("Guess the number between 1-100:"))


      # It'll keep running until the player guesses either correct or just leaves
      while True:
         if player_guess != random_number:
            print("")
            print("Wrong, Try Again!")
            print("")
            counter += 1
            print("Guess counter:",counter)
            if player_guess < random_number:
               print("The number you are look for is higher!")
               print(" ")
            elif player_guess > random_number:
               print("The number you ar looking for is lower!")
               print("")
            player_guess = int(input("Guess the number between 1-100:"))
         elif player_guess == random_number:
            print("")
            print("Correct! the number was", random_number)
            break

      print("You took",counter,"guess!")

      print("")

main()
