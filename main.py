# main.py

# This is the main entry point for my awesome app :)

message: str = "Hello World"
a: int = 2
b: str = "2"
def printer(i: str, j: int, k: str):
    # This method adds i+k and prints the result *j number of times
    l = i+k
    print(l*j)

printer(message,a, b)