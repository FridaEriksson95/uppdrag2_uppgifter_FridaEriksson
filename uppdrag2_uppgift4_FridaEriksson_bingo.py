import random
import os

#Random number generator between 1-15
SlumpTal = [random.randint(1, 20) for _ in range(10)]
Lottnummer = random.randint(1, 1000)

#opening and rules
print("Välkommen till LottoBollar! Du ska nu få gissa på 10 st nummer för chans till bingo!\n")
print("Såhär går det till:\n")
print("Du skriver in dina 10 valda bingonummer med gissning mellan 1-20 som sedan jämförs med de 10 slumpade numrerna.")
print("Om du får 8 rätt eller mer, så ringer du in din bingobricka till LottoBollars kundsupport. Lycka till!\n")

#Users choice of numbers between 1-20
Bricka = []
for i in range(1, 11): 
    while True:   
        nummer = int(input("Välj tal för lottobrickans nummer {}: ".format(i)))
        if nummer <= 20:
            break
#If user enters a number outside the range of 1-20        
        else:
             print("Ogiltig siffra. Försök igen: ")
 #Users Lottobricka with the random numbers between 1-20            
    Bricka.append(nummer)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Bricka)
   
print("SlumpTal:", SlumpTal)
print()
#Summarize of users bricka and slumptal
correct_guesses = sum(1 for num in SlumpTal if num in Bricka)
#If the user has 8 correct guesses
if correct_guesses > 8:
    print(f"BINGO!!!\nDitt lottnummer är: {Lottnummer}")
    print(f"Du hade rätt på {correct_guesses} gissade tal. Skriv ner ditt lottnummer ovan & ange vid kontakt med oss!\n")
    print("Kundsupport 010000000.\nTack för att du spelade!\n")
    input("Tryck Enter för att avsluta..")
    os.system('cls' if os.name == 'nt' else 'clear')
#If the user has less than 8 correct guesses    
else:
    correct_guesses > 0; 
    print(f"Bättre lycka nästa gång! Du hade rätt på {correct_guesses} gissade tal. Tack för att du spelade!")  
    input("Tryck Enter för att avsluta..\n")
    os.system('cls' if os.name == 'nt' else 'clear')     
    
#Mina försök utöver korrigeringar i kod ovan.    
    #bingo = any(num in Bricka for num in SlumpTal)
#if SlumpTal in Bricka:
#if bingo:
        #print(f"BINGO! Du hade rätt på {Bricka.count(SlumpTal[0])} gissade tal.")