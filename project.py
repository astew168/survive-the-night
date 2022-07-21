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
            ]

answers = ['C','A','B','B','A','B']

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

def test():
    ask_question(2)
    answer = get_answer()
    print(check_answer(2, answer))