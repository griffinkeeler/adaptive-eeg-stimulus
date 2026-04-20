# Adaptive Stimulus Optimization for EEG-Based BCIs

## Overview
The goal of this project is to design a dynamic EEG-based BCI paradigm 
where the stimulus presentation adapts based on subjects' neural responses.
A multi-armed bandit (MAB) algorithm will optimize stimulus attributes by choosing
the attribute that gives the highest "reward" from neural responses. 

## Features
- Stimulus parameter optimization
- Adaptive calibration per subject

## Paradigm
- Pick stimulus parameters (e.g., contrast)
- For each "arm" (e.g., low, medium, high):
    - run a short block RSVP (30–50 trials) 
    - send TTL markers
    - save data
    - analyze with MNE
    - compute reward (fisher's linear discriminant (FLD))
- Update bandit
- Choose the next stimulus parameter 
- Repeat 



