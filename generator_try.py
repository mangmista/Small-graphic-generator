file = open('generator_dump.py', 'w')
file.write('from random import *\n'
           'from tkinter import *\n'
           '\n'
           'place = 1\n'
           'how_many_places = 999999\n'
           '\n'
           '\n'
           'def dice_roll():\n'
           '    a = randint(1, 6)\n'
           '    add_roll(a)\n'
           '\n'
           '\n'
           'def add_roll(roll):\n'
           '    global place\n'
           '    global how_many_places\n'
           '    rewrite(place, 0)\n'
           '    place = place + roll\n'
           '    if place > how_many_places:\n'
           '        place -= how_many_places\n'
           '    rewrite(place, 1)\n'
           '\n'
           '\n'
           'def rewrite(places, a):\n'
           '    if a == 0:\n'
           '        gange_back = "label_{}.configure(text=\'{}\')".format(places, places)\n'
           '        exec(gange_back)\n'
           '    if a == 1:\n'
           '        show_plaer = "label_{}.configure(text=\'Player\')".format(places)\n'
           '        exec(show_plaer)\n'
           '        root.update()\n'
           '\n'
           '\n'
           'root = Tk()\n')
file.close()


def place_generator(how_many, how_in_row):
    file2 = open('generator_dump.py', 'a')
    i = 1
    i2 = 0
    row = 1
    how_many = int(how_many)
    how_in_row = int(how_in_row)
    while i <= how_many:
        if i2 == how_in_row:
            i2 -= how_in_row
            row += 1
        a1 = "label_{} = Label(root, text='{}')\n".format(i, i)
        file2.write(a1)
        a2 = "label_{}.grid(row={}, column={})\n".format(i, row, i2)
        file2.write(a2)
        i2 += 1
        i += 1
    b1 = "button = Button(root, text='Roll', command=dice_roll)\n"
    file2.write(b1)
    b2 = "button.grid(row={}, column={})\n".format(row + 1, how_in_row + 1)
    file2.write(b2)
    file2.write('root.mainloop()\n')
    file2.close()


how_many_places = input('How many places?')
how_many_in_row = input('How many in row?')
place_generator(how_many_places, how_many_in_row)
f = open('generator_dump.py', 'r')
filedata = f.read()
f.close()
new_data = filedata.replace('how_many_places = 999999', 'how_many_places = {}'.format(how_many_places))
f = open('generator_dump.py', 'w')
f.write(new_data)
f.close()

import generator_dump
