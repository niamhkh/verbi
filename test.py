"""
This script will contain the actual test.

It will import data from other files.
"""

import random
from Verbi import V_are, V_ire, V_ere, create_verb

subjects = ["io", "tu", "lui", "lei", "noi", "voi", "loro"]
verbs = ["ascoltare", "dormire", "uscire", "ascendere", "camminare"]

count = 0

n = 5

rnd_verbs = random.sample(verbs, n)
rnd_subjects = [random.choice(subjects) for _ in range(n)]

for verb, subject in zip(rnd_verbs, rnd_subjects):
    v = create_verb(verb)
    print(f"verb={verb}, subject={subject}")
    u = input("What is the correct conjugation?\n")
    if u == v.present(subject):
        print("Correct!")
        count += 1
    else:
        print("Incorrect :(")

print(f"You got {count} out of {n} correct.")
if count/n >= 0.85:
    print("Nicely done!")
