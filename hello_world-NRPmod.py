#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo: show a very basic program: hello world
NRP modified to make another window with some new text.
"""

from __future__ import absolute_import, division, print_function

# Import key parts of the PsychoPy library:
from psychopy import visual, core

# Create a visual window:
win = visual.Window()

# Create (but not yet display) some text:
msg1 = visual.TextStim(win, text=u"Hello world!")  # default position = centered
msg2 = visual.TextStim(win, text=u"\u00A1Hola mundo!", pos=(0, -0.3))

# Draw the text to the hidden visual buffer:
msg1.draw()
msg2.draw()

# Show the hidden buffer--everything that has been drawn since the last win.flip():
win.flip()

# Wait 3 seconds so people can see the message, then exit gracefully:
core.wait(3)


# Write some new text! 
msg3 = visual.TextStim(win, text=u"I hope you're staying at home!") # follow-up to our greeting the world

# Reveal the newly written text
msg3.draw()

win.flip()

# And then let the program close out
core.wait(3)

win.close()

core.quit()

# The contents of this file are in the public domain.
