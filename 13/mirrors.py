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
    candidate_to_del = []
    candidates = {}
    traversed = []
    symmetries = []
    reflection_count = 0
    reflection_beginning = -1
    x_reflection = False
    center = [len(pattern) // 2]
    if len(pattern) % 2:
        center.insert(0, center[0]-1)
                
    for x in range(len(pattern)):
        #check_candidates 
        candidate_to_del = []
        for k,v in candidates.items():
            idx = k
            distance = v["distance"]
            remaining = v["remaining"]
            if pattern[x] == traversed[:idx][idx-x-1]:
                remaining = remaining - 1
                if remaining == 0:
                    symmetries.append((idx, distance))
                    candidate_to_del.append(idx)
                else:
                    candidates[idx] = {"distance": distance,"remaining": remaining}
            else:
                candidate_to_del.append(idx)
        [ candidates.pop(x) for x in candidate_to_del ]


        if traversed:
            if pattern[x] == traversed[x-1]:
                distance = abs(x - center[0])
                remaining = x - 1 
                if remaining == 0:
                    symmetries.append((x, distance))
                    candidate_to_del.append(x)
                else:
                    candidates[x] = {"distance": distance,"remaining": x-1}

        traversed.append(pattern[x])

    for k,v in candidates.items():
        symmetries.append((k,v["distance"]))



    if(symmetries):
        minval = min(symmetries, key=lambda x: x[1])[1]
        minimums = [x for x in symmetries if x[1] == minval]
    return minimums[0][0] if symmetries else 0

    #         if (pattern[x] in tmp):
    #             if not x_reflection:
    #                 reflection_beginning = x
    #                 x_reflection = True
    #                 reflection_count = x-1
    #             else:
    #                 if tmp[pattern[x]] == reflection_count-1:
    #                     reflection_count -= 1
    #                     pass
    #                 else:
    #                     x_reflection = False
    #                     reflection_beginning = -1
    #                     reflection_count = 0
    #                     # break
    #         else:
    #             if x_reflection:
    #                 if reflection_count > 0:
    #                     x_reflection = False
    #                     reflection_beginning = -1
    #                     reflection_count = 0
    #                     # break
    #                 else:
    #                     break
    #             tmp[pattern[x]] = x
    #             reflection_count += 1
    # if x_reflection:
    #     return reflection_beginning
    # else:
    #     return 0

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