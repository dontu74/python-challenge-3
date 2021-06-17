#Don Tu Python Exam
import os
os.system('cls' or 'clear')

print("Welcome To The NYC Nightclub Scene Drinking Age Verification Site!\n")

answer = input("Would you like to continue: Y or N?\n")
while answer == "y" or answer == "Y": 

  os.system('cls' or 'clear')  
  firstName = input("Please enter your first name\n")

  os.system('cls' or 'clear') 
  lastName = input("Please enter your last name\n")

  os.system('cls' or 'clear')  
  age = int(input("Please enter your age\n"))



    #if/else conditional statement to determine age
  if age >= 21:
    #if age is greater than 21, output the below message
    os.system('cls' or 'clear')
    print("Thank you {}, You are old enough to enter the nightclub, please drink responsibly\n".format(firstName))
  elif age == 18 or age == 19 or age == 20:
    os.system('cls' or 'clear')
    print(" {}, You are old enough to enter the nightclub but you can only purchase soft drink, no alcohol ALLOWED !\n".format(firstName))  
  else:
    #if age is below 21, output the below message
    os.system('cls' or 'clear')
    print("Sorry,{} You are not old enough to enter this nightclub\n".format(firstName))
    


  
  print("Thank you, {}, {}! You indicate an age of {}. We will keep your information on file.\n".format(firstName, lastName,age))
  
  print("Please visit another club that serves non-alcohol beverage!!!!\n")
  print("Thank you and come back and visit again when you turned 21 years old")
  quit()

else:
  print("Sorry, you can not proceed beyond this point")
  print("Have a wonderful day !!")
