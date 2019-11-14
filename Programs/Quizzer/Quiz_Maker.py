import time

class Quiz():
    
    def __init__(self, num):
        """
        create 3 variables
            number set to the parameter
            question_Bank set to a blank dictionary
            answers set to an array 
        """
        self.number = num
        self.question_Bank = {}
        self.answers = []
        
    def question_Getter(self):
        """
        @self: return the result of asking the user what the question is.
        """
         
        return input("What is the Question \n")
    
    
    def answers_Getter(self):
        """
        @self: Create a blank array
        Run a four loop for times
            Create a string that contains a letter in order each time the loop runs (a - d)
            Concatenate the string the result of a user response asking for an answer
            append the string to the array
        @return: the array
        """
        blank = ["(a)" , "(b)" , "(c)" , "(d)"]
        num = 0
        for i in blank:
            i += input("What is the answer \n")
            blank[num] = i
            num += 1
        return blank
    
    
    def choose_Correct(self, answers):
        """
        @self: print each of the answers on new lines
        @return: the result of user input asking which answer is correct.
        """
       
        for x in self.answers:
            print(x)
        return input("Which answer is correct \n")
        
        
    def question_Creater(self):
        for i in range(0,self.number):
            question = self.question_Getter()
            answers = self.answers_Getter()
            answer = self.choose_Correct(answers)
            self.question_Bank[question] = answers
            self.answers.append(answer)
        self.quiz_Txt_Gen()
    
    def quiz_Txt_Gen(self):
        the_quiz = open("Quizzer" , 'w')
        for i in self.question_Bank:
            the_quiz.write(i + "\n\t")
            for q in self.question_Bank[i]:
                the_quiz.write(q + "\n")
                if self.question_Bank[i].index(q) != (len(self.question_Bank[i]) - 1):
                    the_quiz.write("\t")
            time.sleep(2)
        the_quiz.write("\n\n\n\nANSWERS\n")
        for i in range(0,len(self.answers)):
            the_quiz.write("#" + str(i + 1) + ": " + self.answers[i] + "\n")
        the_quiz.close()
        
"""
Make an instance of the quiz class (You will need a parameter)
call question_Creater
"""
a = Quiz(1)
a.question_Creater()