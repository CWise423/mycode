#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in ' + currentLocation)
  #print the current inventory
  print('You have : ' + str(inventory) + 'in your backback')
  #print an item if there is one
  if locations[currentLocation] == locations["Gilmer County"]:
    print('You see a tiny stream of chimney smoke to your East and the beginning of the Appalachian Trail trailhead to your North')
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
locations = {

            'Gilmer County' : {
                  'north' : 'Hiawassee River',
                  'east'  : 'Widow Johnsons Cabin',
                },
            'Hiawassee River' : {
                  'north' : 'Nantahala Mountains',
                  'item'  : 'raft',
                },
            'Widow Johnsons Cabin' : {
                  'west' : 'Gilmer County',
                  'item' : 'apple pie',
                  'item' : 'toilet paper',
               },
            'Nantahala Mountains' : {
                  'south' : 'Hiawassee River',
                  'item'  : 'blackberries',
                },
            'Smoky Mountains' : {
                  'south' : 'Nantahala Mountains',
                  'north' : "Moonshine Still",
               },
            'Moonshine Still' : {
                  'south' : 'Smoky Mountains',
                  'item'  : 'moonshine',
                  }
           }
#start the player in the Hall
currentLocation = 'Gilmer County'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in locations[currentLocation]:
      #set the current room to the new room
      currentLocation = locations[currentLocation][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in locations[currentLocation] and move[1] in locations[currentLocation]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del locations[currentLocation]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentLocation == 'Moonshine Still' and 'moonshine' in inventory:
    print('You won the respect of the Mountain People... They awarded you with a jar of their "good stuff" and it made you feel so good that you levitated to Maine! Congratulations on finishing the Appalachian Trail')
    break

  ## If a player enters a room with a monster
  elif currentLocation == 'Nantahala Mountains' and 'item' in locations[currentLocation] and 'bear' in locations[currentLocation]['item']:
    print('A mama bear mauled you. You died and you will never hike the Appalachian Trail')
    break

  elif currentLocation == 'Widow Johnsons Cabin' and 'item' in locations[currentLocation] and 'apple pie' in locations[currentLocation]['item']:
    print('You hear the click of a double barrel shotgun and realize the pie was not worth it')
    break
