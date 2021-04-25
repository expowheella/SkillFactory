# Пусть у нас есть рекурсивная функция p(n). Мы вызываем ее с аргументом p(5), она вызывает p(4), та, в свою очередь,
# снова уменьшает аргумент и так до нуля. Однако вычисления будут происходить наоборот! Сначала вычисляется p(0),
# затем p(1) доходя до самого первого вызова функции.
# def p(n):
#     if n >= 0:
#         p(n - 1)
#         print(n)
#
#
# p(5)

pars = {")": "(", "[": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


string = pars
print(par_checker_mod(string))
