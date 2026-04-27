# Adaptive Stimulus Optimization for EEG-Based BCIs

## Overview
The goal of this project is to test the following hypothesis: does adaptive, subject-specific optimization of 
stimulus parameters (e.g., contrast, duration, and size) using a multi-armed bandit improve the separability of target
vs. non-target EEG responses, compared to a fixed stimulus condition? More specifically, does multi-armed bandit optimization
of stimulus parameters increase the Fisher discriminant score between target and non-target ERP respones in an RSVP-based BCI
paradigm, relative to a non-adaptive stimulus condition? 

## Experiment Setup
- Number of subjects
  - Pilot study: 10
  - Real study: 20-40

## Features
- Stimulus parameter optimization
- Adaptive calibration per subject

## Paradigm
- Pick stimulus parameters (contrast)
- For each "arm" (e.g., low, medium, high):
    - run a short block RSVP (100 trials) 
    - send TTL markers
    - save data
    - analyze with MNE
    - compute reward (fisher's linear discriminant (FLD))
- Update bandit
- Choose the next stimulus parameter 
- Repeat 



