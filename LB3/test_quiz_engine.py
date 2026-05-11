import pytest
from quiz_engine import QuizEngine

@pytest.fixture
def engine():
    return QuizEngine()

# --- Тести для get_questions_by_difficulty ---

def test_get_questions_valid(engine):
    # Arrange
    diff = "medium"
    # Act
    result = engine.get_questions_by_difficulty(diff)
    # Assert
    assert "2**10?" in result # EP: Позитивний

def test_get_questions_invalid(engine):
    # Arrange/Act/Assert
    with pytest.raises(ValueError):
        engine.get_questions_by_difficulty("hardcore") # EP: Негативний

# --- Тести для calculate_score ---

def test_score_with_bonus(engine):
    # Arrange
    results = [True, True]
    time = 9 # Межа BVA (менше 10)
    # Act
    total = engine.calculate_score(results, time)
    # Assert
    assert total == 25 # 20 + 5 бонус. Техніка: BVA (позитивний)

def test_score_no_bonus_at_boundary(engine):
    # Arrange
    results = [True, True]
    time = 10 # Межа BVA (рівно 10)
    # Act
    total = engine.calculate_score(results, time)
    # Assert
    assert total == 20 # Техніка: BVA (позитивний)

def test_score_negative_time(engine):
    with pytest.raises(ValueError):
        engine.calculate_score([True], -1) # BVA: Негативний

# --- Тести для determine_rank ---

def test_rank_beginner(engine):
    assert engine.determine_rank(0) == "Beginner" # BVA

def test_rank_scholar(engine):
    assert engine.determine_rank(20) == "Scholar" # BVA

def test_rank_expert(engine):
    assert engine.determine_rank(50) == "Expert" # BVA

def test_rank_legend(engine):
    assert engine.determine_rank(150) == "Legend" # EP: Позитивний

def test_rank_error(engine):
    assert engine.determine_rank(-10) == "Error" # EP: Негативний