import random

questions = [
                [
                    'What does the print() function do?',
                    'A: prints to the nearest printer',
                    'B: converts a list into a string',
                    'C: displays the input to the terminal'
                ],
                [
                    'What symbol defines a string?',
                    'A: \'\' or "" ',
                    'B: :',
                    'C: []'
                ],
                [
                    'What symbol starts a comment?',
                    'A: $',
                    'B: #',
                    'C: //'
                ], 
                [               
                    'What does the input() function do?',
                    'A: inserts an item into a list',
                    'B: reads user input from the terminal',
                    'C: writes the word input'
                ],               
                [
                    'What is the correct way to create a function?',
                    'A: def new_function():',
                    'B: function new_function():',
                    'C: int new_function():'
                ],
                [
                    'How do you check if two variables are equal to each other?',
                    'A: = ',
                    'B: ==',
                    'C: equals()'
                ],       
 [
                    'How would you output "Hello World." in Python?',
                    'A: p("Hello World")',
                    'B: print("Hello World.")',
                    'C: "Hello World"'
                ],
                [
                    'What is the file extension for Python files?',
                    'A: .py',
                    'B: .pyth',
                    'C: .edu'
                ],
                [
                    'Which statement is used to stop a loop?',
                    'A: stop',
                    'B: done',
                    'C: break'
                ], 
                [               
                    'What does the upper() function do?',
                    'A: capitalizes the first letter in a string',
                    'B: capitalizes all the letters in a string',
                    'C: turns uppercase letters into lowercase in a string'
                ],               
                [
                    'Which of the following is a float?',
                    'A: 3.7',
                    'B: 3',
                    'C: 0'
                ],
                [
                    'What does the pop() function do?',
                    'A: adds a new item to the middle of a string',
                    'B: removes and returns the last value in a string',
                    'C: returns "we actually call it soda where I\'\m from"'
                ],                                
            ]

answers = ['C','A','B','B','A','B','B','A','C','B','A','B']

questions_asked = []

def ask_question(question_index):
    question = questions[question_index]
    print('\n' + question[0])
    for answer_choice in question[1:]:
        print('\t' + answer_choice)

def get_answer():
    answer = input().upper()
    while answer != 'A' and answer != 'B' and answer != 'C':
        print('You must answer A, B, or C!')
        answer = input().upper()
    return answer

def check_answer(question_index, answer):
    correct_answer = answers[question_index]
    return (answer == correct_answer)

def random_question_result():
    while True:
        random_index = random.randint(0, len(questions))
        if random_index not in questions_asked:
            questions_asked.append(random_index)
            break
        
    ask_question(random_index)
    answer = get_answer()
    return check_answer(random_index, answer)

def get_choice(choices):
    choice = input().lower()
    while choice not in choices:
        print('That is not a valid choice!')
        choice = input().lower()
    return choice

def main():
    print('It is a dark and stormy night and you find yourself in the unfortunate position of being lost far away from home. ')
    print('In your frantic search for shelter, you see it in the distance: an old abandoned mansion, crumbling but seemingly safe.')
    print('You make your way to the front of the mansion where you are confronted by the first of many choices to come.\n')

    print('Do you...')
    print('\t' + 'A: Go through the front door')
    print('\t' + 'B: Crawl through the side window')
    this_choice = get_choice(['a', 'b']) 

    if this_choice == 'a':
        print('The front door creaks open and you are met with a frightening sight, a ghost!')
        print('This ghost demands that you answer his riddle correctly or he will kill you.')
        user_result = random_question_result()
        if user_result is False:
            print('You died!')
            return
    print('You\'ve sucessfully made it past the first obstacle, but there are many more to come.')
    print('You enter the foyer and see a large staircase infront of you.\n')

    print('Do you...')
    print('\t' + 'A: Go up the staircase')
    print('\t' + 'B: Explore more downstairs')
    this_choice = get_choice(['a', 'b'])

    if this_choice == 'b':
        print('Wrong choice! A ghost appears and shouts his riddle at you.')
        user_result = random_question_result()
        if user_result is False:
            print('You died!')
            return

        
    print('You survived!')

main()
    

