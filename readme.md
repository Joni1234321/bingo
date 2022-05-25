# How to use
### 1. Players
Write the names of all players in the `user/names.txt` file  
Separate each name with newline
### 2. Generate 
Run generate.py followed by the number of plates per player  
If you for example wanted 2 plates per player then write `python generate.py 2`  
or 6 plates per player then write `python generate.py 6`
### 3. Print plates
Each players plates are now converted to a pdf and stored in the folder `user/bingoplader`  
Now give each player their respective documents or print them if you want to
### 4. Play the game
Run main.py like this `python main.py`  
Now you play the game by generating a number yourself from a third party, either online (https://www.random.org/ for example)  
or via a bag of numbers  
Then you just input each number you draw into the console (it will only register numbers between 1 and 90)  
If you typed the wrong number, then write `undo` in the terminal, and it will undo the last number drawn

# IMPORTANT FILES
## Where do you change names?
You write the names in `user/names.txt` before you run `generate.py`
## Where are plates stored?
They are generated as a PDF at `user/bingoplader`  