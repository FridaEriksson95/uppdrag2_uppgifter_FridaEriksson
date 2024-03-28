import os
import random

#Random number
SlumpTal = random.randint(1, 100)
number_of_guesses = 10 

#Opening
print("Välkommen till Gissa Talet!")
print("Du ska nu gissa ett tal mellan 1 och 100, du har 10 försök på dig. Varsågod..")
while True:
    try:
#Users guess       
        guess = int(input("Skriv in ett tal: "))
        
#user guesses right, congrats and ending       
        if guess == SlumpTal:
                print("Grattis, du gissade rätt!")
                input("Tack för att du spelade. Tryck Enter för att avsluta programmet!")
                os.system('cls' if os.name == 'nt' else 'clear')
                break
#User guess outside the range of 1-100           
        elif guess < 1 or guess > 100:
            print("Din gissning är utanför intervallet 1-100.")
#User guess very close but too low        
        elif guess in range(SlumpTal - 3, SlumpTal + 1):
                number_of_guesses -= 1  
                print(("Antal försök kvar: "), + number_of_guesses)
                print("Du är riktigt nära, det bränns.. bara lite högre!\n")
#User guess very close but too high
        elif guess in range(SlumpTal + 1, SlumpTal + 4):
                number_of_guesses -= 1  
                print(("Antal försök kvar: "), + number_of_guesses)
                print("Du är riktigt nära, det bränns.. bara lite lägre!\n")  
#User guess too high
        elif guess > SlumpTal:
                number_of_guesses -= 1  
                print(("Antal försök kvar: "), + number_of_guesses, "\n")
                print("Gissa lägre!")
#User guess too low
        elif guess < SlumpTal:
                number_of_guesses -= 1  
                print(("Antal försök kvar: "), + number_of_guesses,"\n")
                print("Gissa högre!")
#Unavalible option
    except ValueError:
        print("Du gjorde inte ett giltigt val!\nSkriv in en siffra mellan 1-100.")   
        
#User reached out of tries
    if number_of_guesses == 0:
                print(f"Du gissade inte rätt på dina 10 försök. Numret var {SlumpTal}.")
                input("Tack för att du spelade. Tryck Enter för att avsluta programmet!")
                os.system('cls' if os.name == 'nt' else 'clear')
                break      
            
#Mina försök att få till spelet efterhand under uppgiften, osammanhängande tester!            
#Här ska användaren gissa ett tal mellan 1 och 100
#guess = int(input("Skriv in ett tal: "))
#def get_guess():
 #   while True:

  #      if guess < SlumpTal:
   #         return guess
    #    else:
     #       print("Inkorrekt inskrivning. Skriv ett nummer mellan 1-100.")
            
#def check_guess(guess, SlumpTal, number_of_guesses):   
 #       number_of_guesses -= 1  
  #      if guess == SlumpTal: 
   #         return "Du gissade rätt!"
    #    elif guess <  SlumpTal:
     #       return "Du gissade för lågt"
      #  else:
       #     return "Du gissade för högt"
        
#print(("Antal försök kvar: "), + number_of_guesses)
             
        #om användaren gissar för lågt
            #number_of_guesses -= 1
            #print("Tyvärr du gissade för lågt")
            #print(("Antal försök kvar: "), + number_of_guesses)
            #input("Försök igen: ")
            
    
        #if guess > SlumpTal:
        #om användaren gissar för högt
        #number_of_guesses -= 1
        #print("Tyvärr du gissade för högt")
        #print(("Antal försök kvar: "), + number_of_guesses)
       # input("Försök igen: ")
        
        #om användaren gissar rätt
       
      #      print("Grattis, du gissade rätt!")
     #       input("Tryck Enter för att avsluta programmet..")
            
        #om användaren är väldigt nära
    #elif guess == SlumpTal + 3 or guess == SlumpTal - 3:
       # number_of_guesses -= 1
       # print("Du är dock nära och det bränns..")
      #  print(("Antal försök kvar: "), + number_of_guesses)
     #   input("Försök igen: ")
            
    #if number_of_guesses == SlumpTal:
      #  print("Du gissade rätt!")
     #   input("Tryck Enter för att avsluta programmet..")
    #break
    
# Exit the program

