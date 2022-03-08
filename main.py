import random
import hangman_stage as hs
import wordlist as wl
import os

chosen_word=random.choice(wl.word_list)
display=[]
lives=len(hs.stages)-1
end_of_game=False

print(hs.logo)

for _ in range(len(chosen_word)):
    display+="_"


while not end_of_game:
    guess=input("Guess a letter: ").lower()
    
    os.system('cls')
    if guess in display:
      print(f"You've already guessed {guess}")
      
    for positions in range(len(chosen_word)):
        letter=chosen_word[positions]
        if letter==guess:
            display[positions]=letter
    print(f"{' '.join(display)}")
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives ==0:
            end_of_game=True
            print("You lose.")
            
            
    if "_" not in display:
        end_of_game=True
        print("You win !")
    
    print(hs.stages[lives])