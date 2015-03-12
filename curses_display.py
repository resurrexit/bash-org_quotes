#!/usr/bin/env python2.7
from quotes import pull_quotes, get_new_quote
import curses, traceback

# Function to set up a screen with general default settings.
def setup():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    if curses.has_colors():
        curses.start_color()
        init_colours()

    stdscr.keypad(True)
    return stdscr

def teardown(stdscr):
    curses.nocbreak()
    curses.curs_set(1)
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# initialises colour combos (foreground, background)
def init_colours():
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

def main(stdscr):
    stdscr.addstr("RANDOM BASH.ORG QUOTES", curses.A_REVERSE)

    stdscr.chgat(-1, curses.A_REVERSE)
    stdscr.addstr(curses.LINES-1, 0, "Press 'R' to request a new quote, 'Q' to quit")
    stdscr.chgat(curses.LINES-1,7, 1, curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(curses.LINES-1,70, 1, curses.A_BOLD | curses.color_pair(1))

    quote_window = curses.newwin(curses.LINES-2, curses.COLS, 1, 0)
    quote_text = quote_window.subwin(curses.LINES-6,curses.COLS-4, 3,2)

    quote_text.addstr("Press 'R' to get your first quote!")
    quotes = pull_quotes()

    quote_window.box()
    stdscr.noutrefresh()            # updating the screen
    quote_window.noutrefresh()
    curses.doupdate()

    while True:
        c = quote_window.getch()

        if c == ord('r') or c == ord('R'):
            quote_text.clear()
            quote_text.addstr("Getting quote...", curses.color_pair(3))
            quote_text.refresh()
            quote_text.clear()

            q = get_new_quote(quotes)

            if q is None:
                quotes = pull_quotes()

            quote_text.addstr(q)


        elif c == ord('q') or c == ord('Q'):
            break

        # refresh from bottom up
        stdscr.noutrefresh()
        quote_window.noutrefresh()
        quote_text.noutrefresh()
        curses.doupdate()

if __name__=='__main__':
    try:
        stdscr = setup()
        main(stdscr)
    except:
        traceback.print_exc()
    finally:
        teardown(stdscr)
