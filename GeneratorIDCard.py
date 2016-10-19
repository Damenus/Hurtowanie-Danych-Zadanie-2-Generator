import random
import string

def idCard():
    answer = ''
    for i in range(0,3):
        answer += str(random.choice(string.ascii_uppercase))

    for i in range(0,6):
        answer += str(random.randint(0, 9))

    return answer
