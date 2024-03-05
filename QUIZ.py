class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def check_answer(self, user_answer):
        return user_answer == self.correct_choice


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question.text)
        for i, choice in enumerate(question.choices, start=1):
            print(f"{i}. {choice}")
        user_answer = input("Enter the number of your choice: ")
        return int(user_answer)

    def run_quiz(self):
        for question in self.questions:
            user_choice = self.display_question(question)
            if question.check_answer(user_choice):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_choice}: {question.choices[question.correct_choice - 1]}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


# Example usage:
question1 = Question("What is the capital of South Africa?", ["Cape Town", "Pretoria", "Durban", "Grauteng"], 2)
question2 = Question("Which programming language is this quiz written in?", ["Python", "Java", "C++", "JavaScript"], 1)
question3 = Question("What is the currency of South Africa?", ["Dollar", "Rand", "Euro", "Poumd"], 2)

quiz_questions = [question1, question2, question3]
quiz = Quiz(quiz_questions)
quiz.run_quiz()




