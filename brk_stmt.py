mystring = input("Enter the string : ")
print("** BREAK STATEMENTS **\n")
print("break when p occurs ")
for val in mystring:
    if val == "p":
        break
    print(val)
print("End of for loop\n")
n = int(input("Enter a number (3-50): "))
print("breaks when n becomes 2")
while n > 0:
    n = n-1
    if n == 2:
        break
    print(n)
print("End of while loop\n")
print("** CONTINUE STATEMENTS **\n")
print("continues when p occurs instring")
for val in mystring:
    if val == "p":
        continue
    print(val)
print("End of for loop\n")
print("continues when n becomes 2\n")
while n > 0:
    n = n-1
    if n == 2:
        continue
    print(n)
print("End of while loop")
