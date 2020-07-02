ls=["s","w","g"]
print("This is a snack water gun game")
chance=10
no_of_chance=0
computer_point=0
human_point=0

while no_of_chance<chance:
     _input=input("Enter your choice s for snack, w for water and g for gun:")
     _choice=m.choice(ls)
     if _input==_choice:
         print(f"Both are same point so match is tie")
     #when user choose s:
     elif _input=="s" and _choice=="w":
          human_point=human_point+1
          print(f"your guess is {_input} and computer guess is {_choice}")
          print(f"The human point is {human_point}\n computer point is {computer_point}")

     elif _input=="s" and _choice=="g":
          computer_point=computer_point+1
          print(f"your guess is {_input} and computer guess is {_choice}")
          print(f"The computer point is {computer_point}\n and the human point is {human_point}")
     #if user choose w:
     elif _input=="w" and _choice=="s":
          computer_point=computer_point+1
          print(f"your guess is {_input} and computer guess is {_choice}")
          print(f"The computer point is {computer_point}\n and the human point is {human_point}")

     elif _input=="w" and _choice=="g":
          human_point=human_point+1
          print(f"your guess is {_input} and computer guess is {_choice}")
          print(f"The computer point is {computer_point} \n and the human point is {human_point}")

     #if user choose g:
     elif _input=="g" and _choice=="s":
          human_point=human_point+1
          print(f"your guess is {_input} and computer guess is {_choice}")
          print(f"The computer point is {computer_point}\n and the human point is {human_point}")
     elif _input=="g" and _choice=="w":
          computer_point=computer_point+1
          print(f"your guess is {_input} and computer guess is {_choice}")
          print(f"The computer point is {computer_point}\n and the human point is {human_point}")

     else:
          print("Please check your input")
     no_of_chance=no_of_chance+1
     print(f"{chance-no_of_chance} chance you have left")
print(f"Game is over")
if computer_point>human_point:
     print("Winner is computer")
else:
     print("Winner is Rahid")
