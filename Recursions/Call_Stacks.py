def sum_to_one(n):
    result = 1
    call_stack = []

    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")

    while len(call_stack) != 0:
        return_value = call_stack.pop()
        print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
        result += return_value['n_value']
    return result, call_stack


sum_to_one(4)