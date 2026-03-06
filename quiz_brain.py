class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list 
        
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list) 

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = str(input(f"Q.{self.question_number}: {current_question.text} (True/False): "))
        print(f"this is th user answer: {user_answer}")
        return user_answer

    def check_answer(self, user_answer):
        #it is not only if the answe is true, it's if it matches the actaual answer 
        if user_answer == self.question_list[self.question_number].answer :
            print("correct!")
            self.score += 1
        else:
            print("incorrect")
        print(f"score: {self.score}")


    