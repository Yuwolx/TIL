import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())  # Number of test cases

for t in range(1, T + 1):
    s = input()
    stack = []        # Stack to track open rods
    count = 0         # Final count of rod pieces

    for i in range(len(s)):
        if s[i] == '(':            # Opening parenthesis
            stack.append('(')
        else:                      # Closing parenthesis
            stack.pop()            # Remove matching '('
            if s[i - 1] == '(':    # Laser detected: '()'
                count += len(stack)  # Add current number of open rods
            else:
                count += 1         # End of one rod: add 1 piece

    print(f"#{t} {count}")         # Output result
