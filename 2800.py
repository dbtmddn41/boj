form = input()
len_form = len(form)
formulas = set()

stack1 = []
stack2 = []

for i in range(len_form):
    if form[i] == '(':
        stack1.append(i)
    elif form[i] == ')':
        stack2.append((stack1.pop(), i))

bra_num = len(stack2)

for bra_switch in range(1, 1<<bra_num):
    formula = ''
    form_switch = 0
    for sh in range(bra_num):
        if 1<<sh & bra_switch:
            form_switch |= 1<<stack2[sh][0]
            form_switch |= 1<<stack2[sh][1]
    for i in range(len_form):
        if form_switch & 1 == 0:
            formula += form[i]
        form_switch >>= 1
    formulas |= {formula}

print('\n'.join(sorted(list(formulas))))