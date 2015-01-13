import sys
import string


def find_balance(line):
    stack = []
    line = line.replace(":(", "!")
    line = line.replace(":)", "!")

    if '!' in line:
        return 'YES'

    for char in line:
        if char in string.lowercase or char in (' ', ':', '!'):
            pass
        elif char == '(':
            stack.append('(')
        elif char == ')':
            try:
                stack.pop()
            except IndexError:
                return 'NO'
        else:
            return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


def main():
    data = sys.stdin.read().splitlines()[1:]
    for i, line in enumerate(data):
        print "Case #%s: %s" % (i+1, find_balance(line))


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    main()
    # find_balance("(:)")