import sys
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()


def execute(commands):
    for cmd, updown in commands:
        if cmd == "sleep":
            time.sleep(updown)
        elif updown == "D":
            keyboard.press(cmd)
        elif updown == "U":
            keyboard.release(cmd)


def ctrl_plus(key):
    return [
        (Key.ctrl, "D"),
        ("sleep", 0.5),
        (key, "D"),
        ("sleep", 0.1),
        (key, "U"),
        (Key.ctrl, "U"),
    ]


if __name__ == "__main__":
    execute(
        [
            ("sleep", 1),
            *ctrl_plus("o"),
            ("sleep", 2),
            (Key.enter, "D"),
            (Key.enter, "U"),
            (Key.esc, "D"),
            (Key.esc, "U"),
            *ctrl_plus("t"),
        ]
    )
