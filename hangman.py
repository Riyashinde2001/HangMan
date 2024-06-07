import random
from hangmanword import hangmanword_list
chose_word = random.choice(hangmanword_list)
wordlength = len(chose_word)

end_game = False
lives = 6

from hangmanwork import logo
print(logo)
 
display =[]
for _ in range(wordlength):
   display += '_'


 
 # // so here we set a for loop to change words with _ blank space for that we use for loop in range we set a range to wrd lenth
while not end_game: 
    guess = input("guess a letter: ").lower()
   
    
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(wordlength):
       letter = chose_word[position]
       if letter == guess:
         display[position] = letter
    if guess not in chose_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1 
        if lives == 0:
            end_game = True
            print("you lose.") 
        
    print(f"{' '.join(display)}") 
    
    
    
    if '_' not in display:
        end_game = True
        print("you win")
     
    from hangmanwork import stages    
    print(stages[lives])          
      