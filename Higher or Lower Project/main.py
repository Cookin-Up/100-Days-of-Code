import random
from game_data import data
from art import logo, vs

#display logo
print(logo)

#display 2 celebs from list A and B, include name, country, occupation
def choose_celeb(dictionary):
    celeb_dict = random.choice(dictionary)
    return celeb_dict

#check and see if guess was correct, either increment score if True, or Game over if false
def compare_followers(guess, a,b):
    if a['follower_count'] > b['follower_count']:
        return True
    else:
        return False
score = 0
game_on = True

celeb_dict_a = choose_celeb(data)
celeb_dict_b = choose_celeb(data)

if celeb_dict_b == celeb_dict_a:
    celeb_dict_b = choose_celeb(data)


while game_on:
    # ask user to guess who has higher follower count, A or B
    print(f"Compare A: {celeb_dict_a["name"]}, a {celeb_dict_a["description"]} from {celeb_dict_a["country"]}")
    print(vs)
    print(f"Against B: {celeb_dict_b["name"]}, a {celeb_dict_b["description"]} from {celeb_dict_b["country"]}")
    user_guess = input('Who has more instagram followers? Type A or B: ').lower()
    if user_guess == "a" and compare_followers(user_guess, celeb_dict_a, celeb_dict_b) == True:
        score +=1
        (print(f'You are right, score is {score}'))
        # 1/2 restart game if correct guess, old B becomes new A, new B is new rand celeb
        celeb_dict_a = celeb_dict_b
        celeb_dict_b = choose_celeb(data)
    elif user_guess == "b" and compare_followers(user_guess, celeb_dict_a, celeb_dict_b) == False:
        score +=1
        (print(f'You are right, score is {score}'))
        # 2/2 restart game if correct guess, old B becomes new A, new B is new rand celeb
        celeb_dict_a = celeb_dict_b
        celeb_dict_b = choose_celeb(data)
    elif user_guess == "b" and compare_followers(user_guess, celeb_dict_a, celeb_dict_b) == True:
        # 1/2 Display final score for game once game over
        print(f"Game over, you lose, final score was {score}")
        game_on = False
    elif user_guess == "a" and compare_followers(user_guess, celeb_dict_a, celeb_dict_b) == False:
        # 2/2 Display final score for game once game over
        print(f"Game over, you lose, final score was {score}")
        game_on = False



