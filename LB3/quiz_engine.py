class QuizEngine:
    """Модуль для керування логікою квізів та нарахування балів (ФР-02, ФР-03)."""

    def __init__(self): 
        self.questions = {
            "easy": ["2+2?", "Capital of Ukraine?"],
            "medium": ["Python creator?", "2**10?"],
            "hard": ["OPI stands for?", "What is BVA?"]
        }

    def get_questions_by_difficulty(self, difficulty: str):
        """ФР-02: Повертає список питань залежно від складності."""
        diff_lower = difficulty.lower().strip()
        if diff_lower not in self.questions:
            raise ValueError("Unsupported difficulty level")
        
        return self.questions[diff_lower]

    def calculate_score(self, answers_results: list, time_spent: int) -> int:
        """
        ФР-03: Розрахунок балів.
        Логіка: +10 за кожну True відповідь. 
        Якщо час < 10 сек — бонус +5 до загального рахунку.
        """
        if time_spent < 0:
            raise ValueError("Time cannot be negative")
        
        score = 0
        for is_correct in answers_results:
            if is_correct:
                score += 10
        
        if score > 0 and time_spent < 10:
            score += 5
            
        return score

    def determine_rank(self, score: int) -> str:
        """Логіка визначення рангу (цикли/умови)."""
        if score < 0:
            return "Error"

        ranks = [(100, "Legend"), (50, "Expert"), (20, "Scholar"), (0, "Beginner")]
        
        for threshold, label in ranks:
            if score >= threshold:
                return label
        return "Beginner"