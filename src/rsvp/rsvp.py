import random
import sys

from psychopy import visual, core, event
from pathlib import Path
from omegaconf import OmegaConf

# -------------
# Experiment Settings
# -------------

CONFIG_PATH = Path(__file__).resolve().parents[2] / "configs" / "rsvp.yaml"
args = OmegaConf.load(CONFIG_PATH)


target_letter = "X"
non_target_letters = ["A", "B", "C", "E", "L", "M", "O", "R", "S"]

# Uses parallel port depending on the platform
use_parallel = sys.platform.startswith("win")
if use_parallel:
    from psychopy import parallel
    port = parallel.ParallelPort(address=0x0378)
else:
    port = None

def send_trigger(code):
    if port is not None:
        port.setData(code)
        core.wait(0.005)
        port.setData(0)
    else:
        print(f"[TRIGGER] {code}") # debug output



n_sequences = 100
sequence_length = 20
target_probability = 0.20

stimulus_duration = 0.1875
interstimulus_interval = 0.09375

# -------------
# Create trial list
# -------------

sequences = []

for sequence in range(n_sequences):
    trials = []

    # Add non-targets to list
    for _ in range(sequence_length):
        letter = random.choice(non_target_letters)
        trials.append(letter)
        if sequence < 20:
            trials[0] = target_letter

    # Randomize order of trials
    random.shuffle(trials)
    sequences.append({"sequence": sequence, "trials": trials})

# Randomize order of sequences
random.shuffle(sequences)

# -------------
# PsychoPy Setup
# -------------

win = visual.Window(size=(800, 600), color="black", units="pix")

# Text stimulus
contrast = args["contrast"]["high"]
text_stimulus = visual.TextStim(
    win=win, text="", color="white", height=80, pos=(0, 0), contrast=contrast
)

text_stimulus.text = target_letter

# Fixation stimulus
fixation_stimulus = visual.TextStim(
    win=win, text="+", color="red", height=20, pos=(0, 0)
)

# Independent clock for tracking time
clock = core.Clock()

# -------------
# Pre-Sequence Fixation (2.5 s)
# -------------

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
    fixation_stimulus.draw()
    win.flip()

clock.reset()

# Gap between target and RSVP sequence
text_stimulus.text = ""
while clock.getTime() < 0.750:
    text_stimulus.draw()
    fixation_stimulus.draw()
    win.flip()

# -------------
# Sequence Presentation (762.5 s)
# -------------

for i in range(n_sequences):

    trials = sequences[i]["trials"]
    for trial in trials:
        text_stimulus.text = trial

        # Choose trigger code
        if trial == target_letter:
            trigger = 1
        else:
            trigger = 2

        # Draw the stimulus
        text_stimulus.draw()
        fixation_stimulus.draw()

        # Stimulus appears here
        win.flip()

        # Send one trigger at stimulus onset
        send_trigger(trigger)

        # Keep stimulus on screen for remaining duration
        clock.reset()
        while clock.getTime() < stimulus_duration:
            text_stimulus.draw()
            fixation_stimulus.draw()
            win.flip()

        # Inter-stimulus interval
        clock.reset()
        while clock.getTime() < interstimulus_interval:
            fixation_stimulus.draw()
            win.flip()

        if event.getKeys(["escape"]):
            break

    # Gap between sequences
    while clock.getTime() < 2:
        fixation_stimulus.draw()
        win.flip()
    clock.reset()

win.close()
core.quit()
