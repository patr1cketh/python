import random
from filereader import QuestionFileReader
from Bot import QuestionBot

def control_flow():
    response = ""
    while response != "y" or "n":
        response = input("Continue? (y/n) \n")
        if response == "y":
            break
        elif response == "n":
            print("Goodbye.")
            quit()

bot_names = ["Billy", "Bob", "Bailey", "Beatrice"] # List of bot names

question_file_reader = QuestionFileReader("question_bank_2.txt") # new instance of QuestionFileReader class

questions_dict = question_file_reader.all_dictionary_questions()

def get_random_questions(questions, num_of_questions): # takes a dictionary of questions and an integer and returns a new dictionary with the required number of questions
    questions_as_list = list(questions.values()) # creates a list question dictionarys
    return_dict = {}
    for question_number in range(1, num_of_questions + 1): # repeats for the number of questions
        return_dict[question_number] = random.choice(questions_as_list) # populates the new dictionary with a random question.
    return return_dict

random_questions_set = get_random_questions(questions_dict, 5)

question_bot = QuestionBot(bot_names[random.randrange(len(bot_names))], random_questions_set) # creates a new instance of the QuestionBot class with a random name and 5 random questions

question_bot.draw()
question_bot.display_name()
response = ""
# The program will proceed if the user inputs "y" or quit if the user inputs "n"
while response != "y" or "n":
    response = input()
    if response == "y":

        # This loop will run for each question in the questions dictionary
        for i in range(len(questions)):
            bot_1.current_question() # Displays the question
            response = input() # Waits for user response
            if bot_1.check_answer(response) == True: # Checks if the answer is correct
                bot_1.display_correct() # If correct, calls display_correct()
                bot_1.increment_score() # Increments the score
            else:
                bot_1.display_incorrect() # If incorrect, calls display_incorrect()
            bot_1.increment_question_number() # Increments the question number
        
        # After all the questions have been answered the goodbye message is set
        bot_1.set_goodbye_message() 
        bot_1.terminate_messsage() # Displays the goodbye message
        quit() # Ends the program

    # If the user does not want to play the bot says goodbye and the program ends           
    if response == "n":
        bot_1.draw()
        print("Goodbye")
        quit()
        


        



