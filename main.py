print("Welcome to My First Game!!!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

if age >= 7:
   print("The Game Gods say that you are old enough to play!!")  

   wants_to_play = input("Do you want to play? ") 
   if wants_to_play == "yes":
       print("Let's play!")
   if wants_to_play == "no":
       print("That's too bad. Well, maybe next time.")
       


else: 
  print("The Game Gods have deemed you too young to play...")







'''
string "hello", 'hi', "89"
int 8, 7, -9, 1000
float 8.1, 7.653, -9.35, 1000.0
bool True, False
'''
