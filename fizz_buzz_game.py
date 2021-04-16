def fizz_buzz(number: int) -> str:

    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    return str(number)
highest = int(input("Please select the number you wish to play to: "))
next_number = 0
while next_number < highest - 1:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Enter your number: ")
    if correct_answer == player_answer:
        print("Well done! You got it!")
    else:
        print("I'm sorry that was incorrect, the correct answer was {}, you lose :("
              .format(correct_answer))
        break











