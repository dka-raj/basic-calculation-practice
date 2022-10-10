from random import randint, choice


def generateInt(len):
    return randint(10**(len-1), 10**(len)-1)


def generate(terms=2, length=2, operations=["+", "-"], neg=False):
    ques = []
    ans = 0
    for i in range(terms):
        if i != 0:
            operation = choice(operations)
            ques.append(operation)
        else:
            operation = "+"

        if operation == "-" and i != 0 and not neg:
            num = randint(10**(len(str(ans))-1), ans)
        else:
            num = generateInt(length)

        ques.append(num)
        if operation == "+":
            ans += num
        elif operation == "-":
            ans -= num
        elif operation == "×":
            ans *= num
        elif operation == "÷":
            ans /= num
    return {
        "question": ques,
        "answer": ans
    }


print(generate(terms=3))