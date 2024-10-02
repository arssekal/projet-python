import os
import random
import time
def clear_screen():
    if os.name == "nt":
        os.system("cls")
# start the gym app 
def choice_gym():
    print("""
welcome to gym membership mabagement
          
--- choose an action ---
1. add new member
2. display all members
3. search for a member
4. exit
------------------------
""")
    c = int(input("enter your choice : "))
    return c

def search():
    print("""
------ serch by --------
1. membership id
2. name
3. mebership status
------------------------
""")
    c = int(input("enter your choice : "))
    return c
class Gym:

    def __init__(self,name,id,status) :
        self.name = name
        self.id = id
        self.status = status
    def display(self):
        print(f"name : {self.name}")
        print(f"membership id : {self.id}")
        print(f"status : {self.status}")
        print("---------------------")

# help us add a member
def add_member():
    name = input("enter your name : ")
    id = int(input("enter membership id : "))
    status = input("enter membersip status, or click enter to skip: ")
    #check status
    if len(status) == 0:
        status = "inactive"
    print("member added successfully !")
    return Gym(name,id,status)
# the main function gym
def gym_app():
    print("preparing the app ...")
    time.sleep(2)
    clear_screen()
    members = []
    while True:
        c = choice_gym()
        if c == 1:
          clear_screen()
          members.append(add_member())
          print("----------------------------")
          input("   type enter to continue")
          clear_screen()
        elif c == 2:
          clear_screen()
          print("displaying all members ...")
          time.sleep(2)
          if len(members) == 0:
            print("there is no member yet !")
          else :
            for member in members:
              member.display()
          print("----------------------------")
          input("==>   type enter to continue")
          clear_screen()
        elif c == 3:
            clear_screen()
            s = search()
            if s == 1:
              id = int(input("enter the id to search : "))
              clear_screen()
              print("members found :")
              k = len(members)
              for member in members:
                if id == member.id:
                    member.display()
                else:
                    k -= 1
              if k == 0:
                print("no member found with this id !")
            
            elif s == 2:
              name = input("enter a name  to search : ")
              clear_screen()
              print("members found :")
              k = len(members)
              for member in members:
                if name == member.name:
                    member.display()
                else:
                    k -= 1
              if k == 0:
                print("no member found with this name !")
        
            elif s == 3:
              status = input("enter the membership status  to search : ")
              clear_screen()
              print("members found :")
              k = len(members)
              for member in members:
                if status == member.status:
                    member.display()
                else:
                    k -= 1
              if k == 0:
                print("no member found with this status !")
            print("----------------------------")
            input("==>   type enter to continue")
            clear_screen()
        else:
          clear_screen()
          print("exiting the gym app ...")
          break
# end the gym app 

# choose a game
def choose():
  print("""
choose from 1 to 6 :
------------------------    
  1- twenty one
  2- quiz
  3- budget app
  4- gym app
  5- snake
  6- exit
------------------------
""")
  c = int(input("enter your choice : "))
  return c 
# start of the budget app
def menu():
  print("""
1. add an expence
2. show budget details
3. exit
 """)
  c = int(input("enter your choice (1/2/3) : "))
  return c
def budget_app():
  print("preparing the app ...")
  time.sleep(2)
  clear_screen()
  print("--- welcome to the budget app ---")
  intial_budget = float(input("enter your initial budget : "))
  c = menu()
  expence = {
    "expence_desc":[],
    "expence_amount":[],
  }
  while c > 0 and c < 3:
    if c == 1:
      expence_desc = input("enter your expence descriptio : ")
      expence_amount = int(input("enter your expence amount : "))
      expence["expence_desc"].append(expence_desc)
      expence["expence_amount"].append(expence_amount)
      print(f"Added expence : {expence_desc}, amount: {expence_amount}")
      c = menu()
    elif c == 2:
      print("total budget: ",intial_budget)
      print("expence :")
      total_spent = 0
      for i in range(len(expence["expence_amount"])):
        print(f"- {expence['expence_desc'][i]}: {expence['expence_amount'][i]}")
        total_spent += expence['expence_amount'][i]
      print(f"total spent: {total_spent}")
      print(f"remaining budget: {intial_budget - total_spent}")
      c = menu()
  print("exiting budget app")
#end of the budget app

# code of game 21
def display_cards(user_cards,pc_cards):
    print(f"your cards are {user_cards},your score is {sum(user_cards)}")
    print(f"computer first card is : {pc_cards[0]}")

def deal_card():
   cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
   random.shuffle(cards)
   return random.choice(cards)

logo = """                     
░░░░░░░░░ welcome to 21 game    ░░░░░░░░|
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|
░░░░░░░░░████░░░░░░░░██░░░░░░░░░░░░░░░░░|
░░░░░░░░██░███░░░░░██░█░░░░░░░░░░░░░░░░░|
░░░░░░░░██████░░░░██░░█░░░░░░░░░░░░░░░░░|
░░░░░░░░░░░░█░░░░░░░░░█░░░░░░░░░░░░░░░░░|
░░░░░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░░░░|
░░░░░░░░███░░░░░░░░░░░█░░░░░░░░░░░░░░░░░|
░░░░░████░░░░░░░░░░░░███░░░░░░░░░░░░░░░░|
░░░░░░████████░░░░██████████░░░░░░░░░░░░|
----------------------------------------
       """
def calculate_score(cards):
    #is there blacj jack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # sum(cards) > 21 ? and there is 11
    if sum(cards) > 21 and 11 in cards:
        index = cards.index(11)
        cards[index] = 1
    return sum(cards)

def compare(user_score, pc_score):
    result = {
        "draw" : "draw \n\n",
        "user_over": "you went over 21 ,sorry you lose\n\n",
        "pc_over": "pc went over 21 ,you win \n\n",
        "user21": "you win with black jack \n\n",
        "pc21": "sorry you lose, pc has black jack \n\n",
        "user_win" : "you win \n\n",
        "user_lose" : "you lose\n\n",
    }
    if user_score == pc_score :
        return result["draw"]
    elif user_score > 21 :
        return result["user_over"]
    elif pc_score > 21:
        return result["pc_over"]
    elif user_score == 0:
        return result["user21"]
    elif pc_score == 0:
        return result["pc21"]
    elif user_score > pc_score:
        return result["user_win"]
    else :
        return result["user_lose"]

def game21():
    print("starting game ...")
    time.sleep(2)
    clear_screen()
    print(logo)
    user_cards = [deal_card() for _ in range(2)]
    pc_cards = [deal_card() for _ in range(2)]
    game_continue = True
    while game_continue:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)
        print(f"\nyour cards are {user_cards},your score is {sum(user_cards)}")
        print(f"computer first card is : {pc_cards[0]}")
        if user_score == 0 or pc_score == 0 or user_score > 21 or pc_score > 21:
            game_continue = False
        else:
            get_card = input("get another card (y/n) : ").lower()
            if get_card == "y":
                user_cards.append(deal_card())
            else:
                game_continue = False
    while pc_score < 17:
        pc_cards.append(deal_card())
        pc_score = calculate_score(pc_cards)
    print(f"\n\nyour cards are {user_cards},your score is {sum(user_cards)}")
    print(f"computer cards are : {pc_cards},pc score is {sum(pc_cards)}")
    print(compare(user_score, pc_score))
#end game 21

#start quiz game
questions = [
    {
        'prompt' : "what is the capital of france ?",
        'options':['a. madrid','b. paris','c. agadir'],
        'answer': 'b',
    },
    {
        'prompt' : "what is the capital of morroco ?",
        'options':['a. rabat','b. paris','c. agadir'],
        'answer': 'a',
    },
    {
        'prompt' : "what is the capital of spain ?",
        'options':['a. madrid','b. paris','c. agadir'],
        'answer': 'a',
    },
    {
        'prompt' : "what is the capital of englend ?",
        'options':['a. madrid','b. paris','c. berlin'],
        'answer': 'c',
    }
]

def quiz():
    print("starting game ...")
    time.sleep(2)
    clear_screen()
    print("------ welcome to the quiz game ------")
    score = 0
    for q in questions:
        print(q['prompt'])
        for option in q['options']:
            print(option)
        user_answer = input("enter your answer (a,b,c) : ").lower()
        if user_answer == q['answer']:
           score += 1
           print("correct \n\n")
        else:
           print("false \n\n")
    print(f"your score is {score}/{len(questions)}")
    print("-----------------")
#end quiz game

clear_screen()
while True:
    c = choose()
    if c == 1:
        game21()
    elif c == 2:
        quiz()
    elif c == 3:
        budget_app()
    elif c == 4:
        gym_app()
    elif c == 5:
       print("this game does not exit for the moment")
    elif c == 6:
       clear_screen()
       print("exiting ...")
       time.sleep(2)
       print("see you next time")
       break
    else:
       clear_screen()
       print("invalid choice !")

    