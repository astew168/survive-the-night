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