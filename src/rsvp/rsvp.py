import random

from psychopy import visual, core

# -------------
# Experiment Settings
# -------------

target_letter = "E"
non_target_letters = ["A", "B", "C", "E", "L", "M", "O", "R", "S"]

n_trials = 100
target_probability = 0.20

stimulus_duration = 0.1875
interstimulus_interval = 0.09375

# -------------
# Create trial list
# -------------

n_targets = int(n_trials * target_probability)
n_non_targets = n_trials - n_targets

trials = []

# Add targets to list
for _ in range(n_targets):
    trials.append({
        "letter" : target_letter,
        "condition" : "target"
    })

# Add non-targets to list
for _ in range(n_non_targets):
    letter = random.choice(non_target_letters)
    trials.append({
        "letter": letter,
        "condition" : "non_target"
    })

# Randomize order of trials
random.shuffle(trials)

# -------------
# PsychoPy Setup
# -------------

win = visual.Window(size=(800, 600), color="black", units="pix")

# Text stimulus
text_stimulus = visual.TextStim(
    win=win,
    text="",
    color="white",
    height=80,
    pos=(0, 0)
)
text_stimulus.text = target_letter

# Fixation stimulus
fixation_stimulus = visual.TextStim(
    win=win,
    text="+",
    color="white",
    height=80,
    pos=(0, 0)
)

# Independent clock for tracking time
clock = core.Clock()

# Display fixation stimulus at 60 Hz
while clock.getTime() < 1:
    fixation_stimulus.draw()
    # Back buffer becomes visible to screen
    # The previous screen is replaced instantly
    win.flip()

clock.reset()

# Display target stimulus
while clock.getTime() < 0.750:
    text_stimulus.draw()
    win.flip()

clock.reset()

# Gap between target and RSVP sequence
text_stimulus.text = ""
while clock.getTime() < 0.300:
    text_stimulus.draw()
    win.flip()

for trial in trials:
    text_stimulus.text = trial["letter"]

    # Display letter
    clock.reset()
    while clock.getTime() < stimulus_duration:
        text_stimulus.draw()
        win.flip()

    # Inter-stimulus interval
    clock.reset()
    while clock.getTime() < interstimulus_interval:
        fixation_stimulus.draw()
        win.flip()

win.close()
core.quit()








