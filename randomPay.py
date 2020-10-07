import random
#Author: Chen Sun
#this function will spread money m to n people by random

def giveAway(m, n):
    plan = []
    pool = m
    for i in range(1, n, 1):
        try:
            give = random.randint(1, pool)
            pool -= give
            print(give)
            plan.append(give)
        except ValueError:
            give = random.uniform(0, pool)
            pool -= give
            plan.append(give)

    plan.append(pool)
    return plan


if __name__ == "__main__":
    print('test')
    new = giveAway(65, 6)
    print(new)
