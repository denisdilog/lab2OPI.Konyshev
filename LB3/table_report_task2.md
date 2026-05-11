### Таблиця проєктування тестів (Завдання 2)

| № | Метод | Вхідні дані | Очікуваний результат | Техніка | Тип |
|:---|:---|:---|:---|:---|:---|
| 1 | `get_questions` | "easy" | `["2+2?", ...]` | EP | Позитивний |
| 2 | `get_questions` | "extreme" | `ValueError` | EP | Негативний |
| 3 | `calculate_score` | `[True, True]`, time=5 | 25 (20 + 5 бонус) | BVA (time < 10) | Позитивний |
| 4 | `calculate_score` | `[True, True]`, time=10 | 20 (без бонусу) | BVA (time = 10) | Позитивний |
| 5 | `calculate_score` | `[True]`, time=-1 | `ValueError` | BVA (time < 0) | Негативний |
| 6 | `calculate_score` | `[]`, time=5 | 0 | EP | Позитивний |
| 7 | `determine_rank` | score = 0 | "Beginner" | BVA | Позитивний |
| 8 | `determine_rank` | score = 20 | "Scholar" | BVA | Позитивний |
| 9 | `determine_rank` | score = 50 | "Expert" | BVA | Позитивний |
| 10 | `determine_rank` | score = 100 | "Legend" | BVA | Позитивний |
| 11 | `determine_rank` | score = -5 | "Error" | EP | Негативний |