def getLinesFromFile(file: str) -> list[str]:
    file = "input.txt"
    lines = []

    with open(file, 'r') as f:
        for line in f:
            lines.append(line)

    return lines

def getElves(lines: list[str]) -> list[list[int]]:
    elves = []

    while len(lines) > 0:
        try:
            index = lines.index("\n")
            elves.append([int(x) for x in lines[:index]])
            lines = lines[index + 1:]
        except ValueError:
            elves.append([int(x) for x in lines])
            break
    
    return elves

def getTotalCalories(elves: list[list[int]]) -> list[int]:
    calories = []
    
    for elf in elves:
        calories.append(sum(elf))

    return calories

def getMaxCalories(calories: list[int]) -> int:
    return max(calories)

if __name__ == "__main__":
    lines = getLinesFromFile("input.txt")
    elves = getElves(lines)
    calories = getTotalCalories(elves)
    print(getMaxCalories(calories))