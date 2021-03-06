"""test the shell module using a thread."""

import sys
import os
import threading
# insert parent directory into PYTHONPATH
# sys.path.append(os.path.realpath('..\\gameterm'))
# print(sys.path)

import pygame as pg

from gameterm import terminal
from gameterm.shell import Shell


def test_shell():
    """create and run shell, using three really stupid commands."""
    # initiate pygame, create shell object
    pg.init()
    display = pg.display.set_mode((500, 350))
    shell = Shell(terminal.Terminal(display), display, prompt="> ")

    # make sys.stdout, err, and in the terminal
    # shell.bind()

    # start the thread for handling the shell.
    threading.Thread(target=lambda: shell.mainloop(60), daemon=True).start()

    clock = pg.time.Clock()
    fps = 60

    @shell.command
    def say_hi(hello: "say hello instead of hi" = False):
        """say hi.
        if hello is true, say hello instead.
        """
        print('hello' if hello else 'hi')


    @shell.command
    def add(num1: "first number", num2: "second number"):
        """
        add two numbers.

        note: if num1 is divisible by 8, it will say "howdy" instead.
        """

        if int(num1) % 8 == 0:
            # divisible by 8.
            print('howdy')
        else:
            print(float(num1) + float(num2))

    @shell.command
    def echo():
        """ask user for input, and print it once enter has been pressed."""
        print(input())


    while True:
        for event in pg.event.get():
            # add all events
            shell.add_event(event)
            if event.type == pg.QUIT:
                raise SystemExit

        shell.threaded_update()
        pg.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    test_shell()