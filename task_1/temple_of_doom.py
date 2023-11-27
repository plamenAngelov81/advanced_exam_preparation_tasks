from collections import deque

# first tool
tools = deque(map(int, input().split()))

# last substances
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))
is_lost = False

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tool += 1
        substance -= 1
        tools.append(tool)
        if substance > 0:
            substances.append(substance)

    if len(challenges) == 0:
        is_lost = True
        print("Harry found an ostracon, which is dated to the 6th century BCE.")

if not is_lost:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")

if substances:
    print(f"Substances: {', '.join(map(str, substances))}")

if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
