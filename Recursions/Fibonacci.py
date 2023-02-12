# define the fibonacci() function below...
def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
print("fib(5)={0} with runtime is {1}".format(fibonacci(5), fibonacci_runtime))