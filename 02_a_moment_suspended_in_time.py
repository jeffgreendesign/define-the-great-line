"""02 - A Moment Suspended in Time
"""

import sys
import time
import random

# ── ANSI ──────────────────────────────────────────────────────────────────────
RESET       = "\033[0m"
BOLD        = "\033[1m"
DIM         = "\033[2m"
BRIGHT_RED  = "\033[91m"
BRIGHT_CYAN = "\033[96m"
WHITE       = "\033[97m"
YELLOW      = "\033[33m"
MAGENTA     = "\033[35m"

SPENCER  = BRIGHT_RED + BOLD   # raw, screaming — uppercase red
AARON    = BRIGHT_CYAN          # clean, ethereal — cyan
TOGETHER = WHITE + BOLD         # both voices locked together


# ── PRIMITIVES ────────────────────────────────────────────────────────────────

def w(text="", end="\n"):
    sys.stdout.write(text + end)
    sys.stdout.flush()


def tprint(text, color="", delay=0.05, end="\n"):
    """Typewriter: emit each character with a delay."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def glitch(text, color, delay=0.035):
    """Flash a corrupted version of the line, then snap to the real thing."""
    noise = "█▓▒░▀▄▌▐▙▟"
    corrupted = ""
    for ch in text:
        if ch != " " and random.random() < 0.3:
            corrupted += random.choice(noise)
        else:
            corrupted += ch
    sys.stdout.write(MAGENTA + corrupted + RESET)
    sys.stdout.flush()
    time.sleep(0.13)
    sys.stdout.write("\r")
    tprint(text, color, delay)


def flash(times=2, hold=0.06):
    """Invert the terminal video briefly."""
    for _ in range(times):
        sys.stdout.write("\033[?5h")
        sys.stdout.flush()
        time.sleep(hold)
        sys.stdout.write("\033[?5l")
        sys.stdout.flush()
        time.sleep(hold)


def section(name):
    w()
    tprint(f"[ {name} ]", DIM + YELLOW, delay=0.012)
    time.sleep(0.2)


def desk():
    """The place where we wait this out."""
    w()
    w(DIM + "  ┌" + "─" * 47 + "┐" + RESET)
    w(DIM + "  │" + " " * 18 + "[ D E S K ]" + " " * 18 + "│" + RESET)
    w(DIM + "  └" + "─" * 47 + "┘" + RESET)
    w()


# ── VOICES ────────────────────────────────────────────────────────────────────

def spencer(text, delay=0.033):
    tprint(text.upper(), SPENCER, delay)


def aaron(text, delay=0.055):
    tprint("  ♦ " + text, AARON, delay)


def both(text, delay=0.025):
    tprint(text.upper(), TOGETHER, delay)


# ── SONG ──────────────────────────────────────────────────────────────────────

def a_moment_suspended_in_time():

    # ── INTRO ─────────────────────────────────────────────────────────────────
    section("INTRO")
    time.sleep(0.6)

    spencer("Held captive, I'm a prisoner",                                delay=0.07)
    time.sleep(0.25)
    spencer("In the back room where the water leaks and I'm oh, so cold",  delay=0.065)
    time.sleep(0.25)
    spencer("Command me on what to do, but we both know",                  delay=0.07)
    time.sleep(0.2)
    spencer("Neither you or I are in control",                             delay=0.07)
    time.sleep(0.7)
    aaron("There's nothing left for me here",                              delay=0.085)
    time.sleep(0.9)

    # ── VERSE 1 ───────────────────────────────────────────────────────────────
    section("VERSE 1")
    time.sleep(0.3)

    spencer("I'm grabbing on to what's left of this hole",  delay=0.04)
    time.sleep(0.2)
    spencer("It's all too real, this can't be happening",   delay=0.04)
    time.sleep(0.6)

    # ── PRE-CHORUS ────────────────────────────────────────────────────────────
    section("PRE-CHORUS")
    time.sleep(0.3)

    aaron("Never again, ever again will I",                  delay=0.055)
    aaron("Say I'm okay, I'm scared of the fate that will",  delay=0.05)
    time.sleep(0.15)
    both("Become mine, become mine",                         delay=0.025)
    time.sleep(0.15)
    spencer("No time to talk, no time to talk",              delay=0.03)
    spencer("You know the drill",                            delay=0.035)
    time.sleep(0.6)

    # ── CHORUS ────────────────────────────────────────────────────────────────
    section("CHORUS")
    desk()

    spencer("Under my desk, this can't be it",                          delay=0.028)
    glitch("I'm only dreaming,", SPENCER, delay=0.03)
    aaron("I've got to be dreaming",                                     delay=0.045)
    spencer("But I can't get up, no time to talk, not this time",        delay=0.028)
    time.sleep(0.2)
    aaron("This is my place,",                                           delay=0.05)
    spencer("this is where I arrange",                                   delay=0.03)
    time.sleep(0.4)

    aaron("Under my desk, this can't be it",                             delay=0.05)
    aaron("I'm only dreaming,",                                          delay=0.05)
    glitch("I've got to be dreaming", SPENCER, delay=0.028)
    aaron("But I can't get up, no time to talk, not this time",          delay=0.048)
    flash(times=1, hold=0.055)
    time.sleep(0.2)
    spencer("This is my place, this is where I arrange",                 delay=0.028)
    time.sleep(0.8)

    # ── VERSE 2 ───────────────────────────────────────────────────────────────
    section("VERSE 2")
    time.sleep(0.3)

    spencer("It's so funny how we see things so clear",   delay=0.04)
    time.sleep(0.2)
    spencer("When we have no time left to live",          delay=0.04)
    time.sleep(1.5)

    # ── BREAKDOWN ─────────────────────────────────────────────────────────────
    section("BREAKDOWN")
    time.sleep(0.6)

    tprint("So lay back now and take it in",  DIM + WHITE, delay=0.12)
    time.sleep(0.3)
    tprint("I won't say a word",              DIM + WHITE, delay=0.14)
    time.sleep(1.0)
    tprint("So lay back now and take it in",  DIM + WHITE, delay=0.12)
    time.sleep(0.3)
    tprint("And I won't say anything",        DIM + WHITE, delay=0.14)
    time.sleep(1.3)

    # ── BRIDGE ────────────────────────────────────────────────────────────────
    section("BRIDGE")
    time.sleep(0.5)

    aaron("I can't believe how it feels",    delay=0.06)
    time.sleep(0.2)
    aaron("To stand here in this room",      delay=0.06)
    time.sleep(0.2)
    aaron("And feel like it's gonna blow",   delay=0.065)
    time.sleep(0.6)
    aaron("I think we're all gonna blow",    delay=0.08)
    flash(times=2, hold=0.07)
    time.sleep(2.0)

    # ── CHORUS ────────────────────────────────────────────────────────────────
    section("CHORUS")
    desk()

    spencer("Under my desk, this can't be it",                      delay=0.028)
    glitch("I'm only dreaming,", SPENCER, delay=0.03)
    aaron("I've got to be dreaming",                                 delay=0.045)
    spencer("But I can't get up, no time to talk, not this time",    delay=0.028)
    flash(times=1, hold=0.05)
    time.sleep(0.25)
    aaron("This is my place, this is where I arrange",               delay=0.05)
    time.sleep(0.9)

    # ── OUTRO ─────────────────────────────────────────────────────────────────
    section("OUTRO")
    time.sleep(0.5)

    spencer("I've got to be dreaming,",       delay=0.028)
    aaron("I've got to be dreaming",          delay=0.04)
    spencer("We've got to be dreaming,",      delay=0.028)
    aaron("we've got to be dreaming",         delay=0.04)
    aaron("We've got to be",                  delay=0.065)
    time.sleep(0.25)

    spencer("I've got to be dreaming,",       delay=0.028)
    aaron("I've got to be dreaming",          delay=0.04)
    spencer("We've got to be dreaming",       delay=0.028)
    time.sleep(0.4)

    aaron("Please don't wake me up",          delay=0.095)
    time.sleep(2.0)

    # ── THE END ───────────────────────────────────────────────────────────────
    w()
    tprint("this is the end",                              DIM + WHITE,       delay=0.08)
    time.sleep(0.5)
    tprint("THIS IS THE END",                              BRIGHT_RED + BOLD, delay=0.025)
    time.sleep(0.4)
    tprint("T  H  I  S     I  S     T  H  E     E  N  D", WHITE + BOLD,      delay=0.09)
    time.sleep(3.0)
    w()


if __name__ == "__main__":
    a_moment_suspended_in_time()
