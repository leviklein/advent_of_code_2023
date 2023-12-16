import re
import pathlib

def fractionToDecimal(numr, denr):

    # Initialize result
    res = ""
    # Create a map to store already seen
    # remainders. Remainder is used as key
    # and its position in result is stored
    # as value. Note that we need position
    # for cases like 1/6.  In this case,
    # the recurring sequence doesn't start
    # from first remainder.
    mp = {}
    # Find first remainder
    rem = numr % denr
    # Keep finding remainder until either
    # remainder becomes 0 or repeats
    while ((rem != 0) and (rem not in mp)):
        # Store this remainder
        mp[rem] = len(res)
        # Multiply remainder with 10
        rem = rem * 10
        # Append rem / denr to result
        res_part = rem // denr
        res += str(res_part)
        # Update remainder
        rem = rem % denr
    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]

def find_reflection(pattern):
    tmp = {}
    reflection_count = 0
    reflection_beginning = -1
    x_reflection = False
    for x in range(len(pattern)):
        if (pattern[x] in tmp):
            if not x_reflection:
                reflection_beginning = x
                x_reflection = True
                reflection_count = x-1
            else:
                if tmp[pattern[x]] == reflection_count-1:
                    reflection_count -= 1
                    pass
                else:
                    x_reflection = False
                    reflection_beginning = -1
                    reflection_count = 0
                    # break
        else:
            if x_reflection:
                if reflection_count > 0:
                    x_reflection = False
                    reflection_beginning = -1
                    reflection_count = 0
                    # break
                else:
                    break
            tmp[pattern[x]] = x
            reflection_count += 1
    if x_reflection:
        return reflection_beginning
    else:
        return 0
    return reflection_beginning if  x_reflection else 0

def process_pattern(pattern):
    answer = 0
    answer += 100 * find_reflection(pattern)
    answer += find_reflection(list(zip(*pattern)))
    return answer


if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.readline()

    row = 1
    pattern = []
    answer1 = 0
    while a:
        a = a.strip()
        if a:
            pattern.append(a)
        else:
            answer1 += process_pattern(pattern)
            pattern = []

        a = f.readline()
        row += 1
    answer1 += process_pattern(pattern)


    print(f"answer1: {answer1}")