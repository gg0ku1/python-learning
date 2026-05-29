from question import Question

question_prompts = [
    "What color is sky?\n(a) Blue\n(b) Green\n",
    "2 + 2?\n(a) 3\n(b) 4\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

