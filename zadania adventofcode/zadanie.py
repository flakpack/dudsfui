import re

with open('../input.txt', 'r') as input_str:

    lines = input_str.read().splitlines()

    for line in lines:
        samecyfry = re.sub(r'\D', '', input)

        if (len(samecyfry)) == 0:
            print("")
        elif (len(samecyfry)) == 1:
            print(samecyfry * 2)
        else:
            pierwsza = samecyfry[0]
            ostatnia = samecyfry[-1]
            print(pierwsza + ostatnia)