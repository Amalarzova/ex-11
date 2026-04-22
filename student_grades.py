class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self,index):
        body = self.scores[index]

        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        else:
            return "F"

    def find(self, hledane_body):
        indexy = []

        for i in range(len(self.scores)):
            if self.scores[i] == hledane_body:
                indexy.append(i)
        return indexy

    def get_sorted(self):
        scores = self.scores.copy()

        n = len(scores)

        for i in range(n):
            for j in range (0, n - i - 1):
                if scores[j] > scores[j +1]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]

        return scores


if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())


