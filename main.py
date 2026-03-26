#userstory: Система повинна нараховувати користувачу бали за правильні відповіді.

from typing import List

class Question:
    def __init__(self, text: str, correct_answer: str, points: int = 10):
        self.text = text
        self.correct_answer = correct_answer

    def is_correct(self, user_answer: str) -> bool:
        return user_answer.strip().lower() == self.correct_answer.strip().lower()

class User:
    def __init__(self, username: str):
        self.username = username
        self.score = 0

    def add_points(self, points: int):
        self.score += points
        print(f"💰 Користувачу {self.username} нараховано {points} балів! (Поточний рахунок: {self.score})")

class QuizSystem:
    def __init__(self):
        self.questions: List[Question] = []

    def add_question(self, question: Question):
        self.questions.append(question)

    def run_quiz(self, user: User):
        print(f"\n=== Початок тестування: {user.username} ===")
        print(f"Всього питань: {len(self.questions)}\n")

        for index, question in enumerate(self.questions, start=1):
            print(f"Питання {index} [Вартість: {question.points} балів]:")
            print(f" > {question.text}")
            
            user_input = input("Ваша відповідь: ")

            if question.is_correct(user_input):
                print("✅ Вірно!")
                user.add_points(question.points)
            else:
                print(f"❌ Невірно. Правильна відповідь: {question.correct_answer}")
            print("-" * 30)

        print(f"=== Тестування завершено ===")
        print(f"🏆 Фінальний результат {user.username}: {user.score} балів.")

if __name__ == "__main__":
    system = QuizSystem()

    system.add_question(Question("Який протокол використовується для передачі веб-сторінок?", "http", 10))
    system.add_question(Question("Скільки байтів в одному кілобайті?", "1024", 15))
    system.add_question(Question("Як називається процес знаходження та виправлення помилок у коді?", "дебагінг", 20))

    student_name = input("Введіть ваше ім'я для реєстрації в системі: ")
    student = User(student_name)

    system.run_quiz(student)