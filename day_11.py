from functools import partial
from operator import mul
from string import ascii_lowercase
from sys import maxsize

from pulp import LpInteger, LpProblem, LpVariable, PULP_CBC_CMD, lpSum

BASE = len(ascii_lowercase)
ENCODE_TRANSLATION = dict(zip(ascii_lowercase, range(BASE)))
# noinspection PyTypeChecker
DECODE_TRANSLATION = dict(map(reversed, ENCODE_TRANSLATION.items()))


def main():
    password = input()
    next_password = part_1_and_2(password)

    print(next_password)
    print(part_1_and_2(next_password))


def part_1_and_2(password):
    for idx, char in enumerate(password):
        if char in 'ilo':
            password = password[:idx] + chr(ord(char) + 1) + 'a' * len(password[idx + 1:])
            break
    password = list(map(ENCODE_TRANSLATION.get, password))
    powers = list(map(partial(pow, BASE), range(len(password) - 1, -1, -1)))
    password_sum = sum(map(mul, powers, password))
    next_password = [maxsize for _ in range(len(password))]

    for i in range(len(password) - 3):
        for j in (j for j in range(len(password) - 3) if j < i or j > i + 1):
            for k in (k for k in range(len(password) - 1) if (k < i or k > i + 1) and k > j + 1):
                problem = LpProblem()
                variables = [LpVariable(str(n), 0, BASE - 1, LpInteger)
                             for n in range(len(password) - 1, -1, -1)]
                next_password_sum = lpSum(map(mul, powers, variables))

                problem += next_password_sum
                problem += next_password_sum >= password_sum + 1
                problem += variables[i] == variables[i + 1] - 1
                problem += variables[i + 1] == variables[i + 2] - 1
                problem += variables[j] == variables[j + 1]
                problem += variables[k] == variables[k + 1]

                problem.solve(PULP_CBC_CMD(msg=False))

                next_password = min(next_password, list(map(round, map(LpVariable.value, variables))))

    next_password = ''.join(map(DECODE_TRANSLATION.get, next_password))

    return part_1_and_2(next_password) if any(map('ilo'.__contains__, next_password)) else next_password


if __name__ == '__main__':
    main()
