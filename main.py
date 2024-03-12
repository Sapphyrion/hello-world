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

test = ["a", "b","c","d"]
print (test[3])
print (test[:])
print (test[-2])
print (test[:2])
print (test[2:])

for num in range(100, 0, -25):
    print (num)

print(1 > 0)
print(1 < 0)

