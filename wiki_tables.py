import fileinput

start1 = '====== '
start2 = ' ======\n{| class="wikitable"\n|-\n! Show Name\n! Outcome\n|-'
win = '| style="background-color: #90EE90" | '
div = '\n|-'

for line in fileinput.input():
    x = line.split(',,')
    if len(x) == 1:
        if (x[0].strip() == ''):
            print('|}\n')
        else:
            print(start1 + line.rstrip() + start2)
    elif len(x) == 2:
        if x[1].strip() == 'W':
            print(win + x[0].strip() + '\n' + win + x[1].strip() + div)
        else:
            print('| ' + x[0].strip() + '\n| ' + x[1].strip() + div)
print('|}\n')
