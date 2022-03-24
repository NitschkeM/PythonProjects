#!/usr/bin/env python

# What we have in common - with Rocket League / Other Subject(s)
#       - With Inner Being?


# Clear Goal / Clear Intent
# To 
# Can a Goal/Intent be Both Clear and Open-Ended?
#   Score a Goal
#       How one does it is not specified.
#       It is clear: Knows exactly when the goal would be reached/scored.
#           Measurable?
#               The goal is that an imagined event happens - when the event has been observed it has happned - 
#                   Scientist Wonders: Observation of an Event Completes an Experiment?
#               The goal is that an imagined event happens - when the event has happned has it been observed?
#                   Relates to the Idea of an event happening without being observed.
#                       When a tree falls in the forest and noone is there to hear it - does it make a sound?
#                           Sound is a Subjective Experience - Sound does not exist outside Mind/Experience?
#                               But if I imagine the processing in my brain as playing sounds/music then would that music exist outside experience? outside consciousness?
#                                       Is the Whole Mind Conscious?
#                       Am I on Team Consciousness and Experience and against NotConsciousness and NotExperience?
#                               No
#                               Harmony, Synergy and Cooperation
#                               Feeling and Awareness
#                               Connected to and Aligned with Inner Being
#                               There are not really any teams - all one



# Curiosity! I want to Explore!
#    Seeing where I started the questioning - and where it lead.
#       Is there a connection?
#       Does what "came out" somehow help with what the one who wrote the starting point wondered about/desired?






# import asyncio
# import websockets

# async def hello():
#     async with websockets.connect("ws://localhost:8765") as websocket:
#         await websocket.send("Hello world!")
#         await websocket.recv()

# asyncio.run(hello())



#!/usr/bin/env python

import asyncio
from websockets import connect

async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.run(hello("ws://localhost:8765"))