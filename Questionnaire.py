# Dictionary to store the options and corresponding scores for each question
scores = {
    "How many steps do you average in a week?": {
        "<5000": 1,
        "5000-10,000": 2,
        ">10,000": 3
    },
    "How often do you urinate?": {
        "<every 2 hours": 1,
        "2-4 hours": 2,
        ">every 4 hours": 3
    },
    "Why are you doing medicine?": {
        "IDK": 1,
        "why not": 2,
        "it was a mistake": 3
    }
}

# Initialize the total score to 0
total_score = 0

# Ask the questions and add the scores
print("How many steps do you average in a week?")
print("1. <5000")
print("2. 5000-10,000")
print("3. >10,000")
steps = int(input("Enter the number of your choice: "))
total_score += list(scores["How many steps do you average in a week?"].values())[steps-1]

print("How often do you urinate?")
print("1. <every 2 hours")
print("2. 2-4 hours")
print("3. >every 4 hours")
urination = int(input("Enter the number of your choice: "))
total_score += list(scores["How often do you urinate?"].values())[urination-1]

print("Why are you doing medicine?")
print("1. IDK")
print("2. it's good")
print("3. it was a mistake")
medicine = int(input("Enter the number of your choice: "))
total_score += list(scores["Why are you doing medicine?"].values())[medicine-1]

# Print the final score and output based on the total score
print(f"Your final score is: {total_score}")
if total_score < 3:
    print("yeah bro you're healthy")
elif total_score < 6:
    print("oooh do a 5k tomorrow")
else:
    print("Go see your urologist")


#OOP
class HealthSurvey:
    def __init__(self):
        self.total_score = 0
        self.questions = [
            "How many steps do you average in a week?",
            "How often do you urinate?",
            "Why are you doing medicine?"
        ]
        self.choices = [
            ["<5000", "5000-10,000", ">10,000"],
            ["<every 2 hours", "2-4 hours", ">every 4 hours"],
            ["IDK", "why not", "it was a mistake"]
        ]
        self.scores = [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ]

    def ask_questions(self):
        for i, question in enumerate(self.questions):
            print(question)
            for j, choice in enumerate(self.choices[i]):
                print(f"{j + 1}. {choice}")
            response = int(input("Enter the number of your choice: "))
            self.total_score += self.scores[i][response - 1]

    def output_result(self):
        print(f"Your final score is: {self.total_score}")
        if self.total_score < 3:
            print("yeah bro you're healthy")
        elif self.total_score < 6:
            print("ooof do a 5k tomorrow")
        else:
            print("Go see your urologist")

survey = HealthSurvey()
survey.ask_questions()
survey.output_result()


class Student:
    def __init__(self, name, age, gender, major):
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major










