print("Welcome to My First Game!!!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

print("You are starting with", health, "health.")

if age >= 7:
   print("The Game Gods say that you are old enough to play!!")  
   
   wants_to_play = input("Do you want to play? ").lower()
   if wants_to_play == "yes":
       print("Let's play!")
       print("You are starting with", health, "health.")

       left_or_right = input("Every intrepid explorer's first order of business is to choose which direction to go..in this case..left or right...(left/right)? ")
       if left_or_right == "left".lower():
           ans = input("You follow the a small path to the left along a dimly lit corridor until you come to a Y intesection that continues straight or veers to the right. Which way Indy?...(straight/right)")

           if ans == "straight":
              print("After remembering an old addage about left being right you head down the straight passage.  You eventually find your way to a door that leads to a fresh and breezy copse of pines on a well used path outside of what appears to be a cave. However, in your hurry to make it out of the corridor you walked right over an unusually large vermin that bit your toe in protest and ran away in disgust to wash out its mouth. You've lost 2 health.")
              health -= 8
           elif ans == "right":
              print("You find a that it's a short walk to a door which leads to a fresh and breezy copse of pines on a well used path outside of what appears to be a cave")
           ans == input("As you take in the fresh air you notice a small cabin set back in the pines and a small dock on a river. Which do you go to?...(cabin or river)")
             
           if ans == "cabin":
              print("As you approach the cabin you smell a strong scent of heavily spiced mystery meat and fresh tomatoes. Over the entrance is a Bell shaped like a Taco. The owner of the cabin offers you lunch which you gladly accept. Ten minutes later you are lying on the ground and lose 8 health because of explosive diarrhea!!!")
              health -= 8
           elif ans == "river":
             print("You carefully make you way onto the rickety old dock and look around. You notice that there is a small wooden raft attached to a rope that crosses the river and a dugout canoe with a paddle. While trying to decide what to do you notice how hungry you are. You lose 1 health.")  
             health -= 1
              
             if health <= 0:
                print("Who knew that a plate of Nachos Bell Grande would be your undoing!?!?! You have died and your soul is now banished to the Bog of Eternal Stench....")
             if health >= 0:
                print("Not too bad for your first day no0b but next time get your mom to make us a sammich and juice box will ya..")
       
       else:
          print("You turn to the right and immediately walk into the web of a giant spider....I guess somebody is going to have a nice meal (and it isn't you). Sorry spider bait.")



   if wants_to_play == "no":
       print("That's too bad. Well, maybe next time.")

       


else: 
  print("The Game Gods have deemed you too young to play...")
  loop_back = True