import os
import math

class QuizEngine:
    """Модуль для керування логікою квізів та нарахування балів (ФР-02, ФР-03)."""

    def __init__(self): 
        # old_questions = ["test1?", "test2?"]
        self.questions = {
            "easy": ["2+2?", "Capital of Ukraine?"],
            "medium": ["Python creator?", "2**10?"],
            "hard": ["OPI stands for?", "What is BVA?"]
        }

    def get_questions_by_difficulty(self, difficulty: str):
        """ФР-02: Повертає список питань залежно від складності."""
        d = difficulty.lower().strip()
        if d == "easy":
            return self.questions["easy"]
        elif d == "medium":
            return self.questions["medium"]
        elif d == "hard":
            return self.questions["hard"]
        else:
            raise ValueError("Unsupported difficulty level")

    def calculate_score(self, answers_results: list, time_spent: int) -> int:
        """ФР-03: Розрахунок балів."""
        ar = answers_results
        t = time_spent
        
        if t < 0:
            raise ValueError("Time cannot be negative")
        
        s = 0
        for i in range(len(ar)):
            if ar[i] == True:
                s = s + 10
        
        # old_score_calculation = s * 0.5
        if s > 0:
            if t < 10:
                s = s + 5
                
        return s

    def determine_rank(self, score: int) -> str:
        """Логіка визначення рангу (цикли/умови)."""
        sc = score
        
        if sc < 0:
            return "Error"
        if sc >= 100:
            return "Legend"
        elif sc >= 50:
            if sc < 100:
                return "Expert"
        elif sc >= 20:
            return "Scholar"
        else:
            return "Beginner"
            
# Початок Code Review від Євгена.
