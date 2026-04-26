import random

from psychopy import visual, core

# -------------
# Experiment Settings
# -------------

target_letter = "X"
non_target_letters = ["A", "B", "C", "D", "E", "F", "G"]

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

stimulus = visual.TextStim(
    win=win,
    text="",
    color="white",
    height=80,
    pos=(0, 0)
)






