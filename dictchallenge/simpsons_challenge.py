#!/usr/bin/python3

challenge = [
  "science",
  "turbo",
  [
    "goggles",
    "eyes"
  ],
  "nothing"
]
# eyes 
eyes = challenge[2][1]

# goggles
goggles = challenge[2][0]

# nothing
nothing = challenge[3]

print(f"My {eyes}! My {goggles} do {nothing}!")


trial = [
  "science",
  "turbo",
  {
    "eyes": "goggles",
    "goggles": "eyes"
  },
  "nothing"
]

# eyes
eyesT = trial[2]["goggles"]

# goggles
gogglesT = trial[2]["eyes"]

# nothing
nothingT = trial[3]

print(f"My {eyesT}! My {gogglesT} do {nothingT}!")
